from typing import List
from core.extensions import db

def create_allocation_query(group_size: int, theater_id: int, section_id: int=None) -> List[int]:
    query = "SELECT id FROM seat WHERE rank \
                >= (SELECT a.rank FROM seat a LEFT JOIN seat b ON \
                a.rank < b.rank \
                AND b.rank < a.rank +:group_size \
                AND b.reserved_by IS NULL \
                AND a.row_number = b.row_number \
                AND a.section_id = b.section_id \
                WHERE a.reserved_by IS NULL \
                AND a.theater_id = :theater_id "

    if section_id:
        query += f" AND a.section_id = {section_id} "
        
    query += "GROUP BY a.rank \
                HAVING COUNT(b.rank)+1 = :group_size \
                LIMIT 1) LIMIT :group_size"

    sql = db.text(query).bindparams(group_size=group_size, theater_id=theater_id)
    results = db.session.execute(sql).fetchall()
    ids = [ x.id for x in results ]
    return ids
