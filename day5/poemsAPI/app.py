import psycopg2
from flask import Flask 
from config import Config
from flask_cors import CORS
from flask_restful import Api
# Endpoints - classes 
from resources.users import LoginUsers
from resources.users import Singup
from resources.poems import Poems

conn = psycopg2.connect(Config.DB_URL)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/*": {"origins": "*"}})
    register_resources(app)
    return app

def register_resources(app):
    api = Api(app)
    api.add_resource(LoginUsers, 
                     '/login',
                     resource_class_kwargs={'db': conn})
    api.add_resource(Singup, 
                    '/singup',
                    resource_class_kwargs={'db': conn})
    api.add_resource(Poems, 
                    '/addpoem',
                    resource_class_kwargs={'db': conn},
                    endpoint="add_poems")
    api.add_resource(Poems, 
                    '/updatepoem',
                    resource_class_kwargs={'db': conn},
                    endpoint="update_poems")
    
    return api

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)