from typing import List
from sqlalchemy.sql import text
from werkzeug.exceptions import abort
from core.modules.theater.models import Seat, Section, Theater
from core.extensions import db
from core.modules.theater.queries import create_allocation_query

class AllocationService:
    @staticmethod
    def allocate(data) -> Theater:
        theater_id = data["theater_id"]
        theater = Theater.query.get(theater_id)

        if not theater:
            raise Exception(f'theater_id {theater_id} does not exist')
        
        groups_sorted_by_rank = sorted(data["groups"], key=lambda x: x["group_rank"])
        seat_ids = []
        user_ids = []
        for group in groups_sorted_by_rank:
            section = Section.query.get(group["section_id"]) if "section_id" in group else None
            section_id = section.id if section else None

            results = create_allocation_query(len(group["user_ids"]), theater_id, section_id)
            user_ids.extend(group["user_ids"])
            seat_ids.extend(results)

        
        seats_users_mapping = []
        for index, value in enumerate(seat_ids):
            seats_users_mapping.append({"id": value, "reserved_by": user_ids[index]})
        
        try:
            db.session.bulk_update_mappings(Seat, seats_users_mapping)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)
        
        return Theater.query.get(theater_id)


class TheaterService:
    @staticmethod
    def get_seat_by_user_id(id: int) -> Seat:
        try:
            seat = Seat.query.get(id)
            if not seat:
                abort(404)
            return seat
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def get_one(id: int) -> Theater:
        try:
            theater = Theater.query.get(id)
            if not theater:
                abort(404)
            return theater
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def get_all(page, per_page=10) -> List[Theater]:
        return Theater.query.paginate(page, per_page, error_out=False).items

    @staticmethod
    def create_theater(data) -> Theater:
        new_theater = Theater(name=data["name"])
        for i in data["seats"]:
            new_theater.seats.append(Seat(**i))

        db.session.add(new_theater)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

        return new_theater



class SectionService:
    @staticmethod
    def get_all(page, per_page=10) -> List[Section]:
        return Section.query.paginate(page, per_page, error_out=False).items


    @staticmethod
    def create_section(data) -> Section:
        new_section = Section(**data)
        db.session.add(new_section)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

        return new_section
