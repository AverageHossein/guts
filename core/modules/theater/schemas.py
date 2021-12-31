from marshmallow import Schema, fields

class SeatSchema(Schema):
    id = fields.Integer()
    seat_number = fields.Integer(required=True)
    row_number = fields.Integer(required=True)
    rank = fields.Integer(required=True)
    reserved_by = fields.Integer()
    theater_id = fields.Integer()
    section_id = fields.Integer()

class SectionSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)


class TheaterSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    seats = fields.List(fields.Nested(SeatSchema), required=True)


class GroupSchema(Schema):
    user_ids = fields.List(fields.Integer(), required=True)
    section_id = fields.Integer()
    group_rank = fields.Integer(required=True)
    

class AllocationSchema(Schema):
    theater_id = fields.Integer()
    groups = fields.List(fields.Nested(GroupSchema), required=True)