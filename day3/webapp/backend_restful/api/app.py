from flask import Flask 
from config import Config
from flask_cors import CORS
from flask_restful import Api
from resources.user import LoginUsers
from resources.rooms import ReserveRooms
from resources.user import UserLuggage

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/*": {"origins": "*"}})
    register_resources(app)
    return app

def register_resources(app):
    api = Api(app)
    api.add_resource(LoginUsers, '/loging')
    api.add_resource(ReserveRooms, '/room')
    api.add_resource(UserLuggage, '/upload')

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)