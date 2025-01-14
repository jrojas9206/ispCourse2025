from flask import request
from http import HTTPStatus
from flask_restful import Resource

class ReserveRooms(Resource):

    def post(self):
        data = request.get_json()
        return {'message':'approved',
                'userSelection': data}, HTTPStatus.OK