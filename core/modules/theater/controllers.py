from typing import List
from flask import request
from core.extensions import api
from flask_restx import Resource, Namespace
from core.modules.theater.models import Section, Theater
from core.modules.theater.schemas import AllocationSchema, SeatSchema, SectionSchema, TheaterSchema
from flask_accepts import accepts, responds
from core.modules.theater.services import AllocationService, SectionService, TheaterService
from core.utils.exception_handler import handle_exception

theater = Namespace('theater')
parser = api.parser()
parser.add_argument("page", type=int, required=True)
parser.add_argument("per_page", type=int, required=False)



@theater.route('seat/user/<int:id>')
class GetUserSeat(Resource):
    @theater.errorhandler
    @responds(schema=SeatSchema(only=["seat_number"]))
    def get(self, id: int) -> Theater:
        """Gets one seat by user Id"""

        return TheaterService.get_seat_by_user_id(id)


@theater.route('/<int:id>')
class GetOneTheater(Resource):
    @theater.errorhandler
    @responds(schema=TheaterSchema())
    def get(self, id: int) -> Theater:
        """Gets one theater by Id"""

        return TheaterService.get_one(id)


@theater.route('/')
class TheaterController(Resource):
    @theater.errorhandler
    @responds(schema=TheaterSchema(many=True))
    def get(self) -> List[Theater]:
        """Gets all Theaters"""

        args = dict(filter(lambda sub: sub[1], parser.parse_args(strict=True).items()))
        return TheaterService.get_all(**args)

    @theater.errorhandler
    @accepts(schema=TheaterSchema(exclude=["id", "seats.id", "seats.reserved_by", "seats.theater_id"]))
    @responds(schema=TheaterSchema())
    def post(self):
        """Creates a Theater"""

        data = request.parsed_obj
        return TheaterService.create_theater(data)


@theater.route('/section')
class SectionController(Resource):
    @theater.errorhandler
    @responds(schema=SectionSchema(many=True))
    def get(self) -> List[Section]:
        """Gets all Sections"""

        args = dict(filter(lambda sub: sub[1], parser.parse_args(strict=True).items()))
        return SectionService.get_all(**args)


    @theater.errorhandler
    @accepts(schema=SectionSchema(exclude=["id"]))
    @responds(schema=SectionSchema())
    def post(self):
        """Creates a Section"""

        data = request.parsed_obj
        return SectionService.create_section(data)


@theater.route('/allocate')
class AllocationController(Resource):
    @theater.errorhandler
    @accepts(schema=AllocationSchema())
    @responds(schema=TheaterSchema())
    def post(self) -> Theater:
        """Allocates seats of a theater"""

        data = request.parsed_obj
        return AllocationService.allocate(data)
