import os 
import psycopg2
from pathlib import Path
from flask import request
from http import HTTPStatus 
from flask_restful import Resource

class LoginUsers(Resource):

    def __init__(self, db=None):
        self._db = db

    def post(self):
        data = request.get_json()
        user_name = data.get('name')
        user_pass = data.get('password')
        SQL_query = f"SELECT user_password, user_id FROM users WHERE user_name = '{user_name}'" 
        userid = -1
        isAccepted = False
        with self._db.cursor() as cursor:
            cursor.execute(SQL_query)
            userInfo = cursor.fetchone()
            print(userInfo)
            pass2verify = userInfo[0]
            userid = userInfo[1]

            if isinstance(pass2verify, type(None)):
                isAccepted = False
            else:
                if pass2verify == user_pass:
                    isAccepted = True 
                    
                else:
                    isAccepted = False
        if isAccepted:
            return {'message':'Loging Successful',
                'auth_token':userid }, HTTPStatus.OK 
        return {'message':'Access not granted'}, HTTPStatus.FORBIDDEN       
    
class Singup(Resource):

    def __init__(self, db=None):
        self._db = db 

    def post(self):
        data = request.get_json()
        user_name = data.get('name')
        user_lastname = data.get('lastname')
        user_avatar_name = data.get('avatar_name')
        user_password = data.get('password')
        if self.userExist(user_name, 
                          user_lastname,
                          user_avatar_name):
            return {'message':'User already exists!'}, HTTPStatus.NOT_ACCEPTABLE
        else:
            newid = self.getLastUserId()+1
            if self.addUser(user_name, 
                          user_lastname,
                          user_avatar_name,
                          user_password,
                          newid):  
                return {'message':'User added'}, HTTPStatus.CREATED
            return {'message':'There was a problem adding the new user!'}, HTTPStatus.EXPECTATION_FAILED

    def addUser(self, user_name, 
                      user_lastname,
                      user_avatar_name,
                      user_password,
                      user_id):
        SQL_query = f"INSERT INTO users(user_name, user_last_name, user_avatar_name, user_password, user_id)\
             VALUES('{user_name}', '{user_lastname}', '{user_avatar_name}', '{user_password}', '{user_id}')"
        addedSuccessfully = False
        with self._db.cursor() as cursor:
            try:
                cursor.execute(SQL_query) 
                addedSuccessfully = True
            except Exception as error:
                addedSuccessfully = False
                print(f'error: {error}')
        if addedSuccessfully:
            self._db.commit()
            return True
        self._db.rollback()
        return False
              
    def getLastUserId(self):
        SQL_last_id = "SELECT MAX(user_id) FROM users;"
        with self._db.cursor() as cursor:
            cursor.execute(SQL_last_id) 
            lastId = cursor.fetchone()[0]
        if isinstance(lastId, type(None)):
            return 0
        return lastId

    def userExist(self, user_name, user_lastname, user_avatar_name):
        SQL_query = f"SELECT * FROM users WHERE user_name = '{user_name}' AND user_last_name = '{user_lastname}'\
             AND user_avatar_name = '{user_avatar_name}';"
        userExist = False 
        with self._db.cursor() as cursor:
            try:
                cursor.execute(SQL_query)
                userData = cursor.fetchone()
                if isinstance(userData, type(None)):
                    userExist = False
                else:
                    userExist = True 
            except psycopg2.errors.InFailedSqlTransaction:
                self._db.rollback()
                userExist = False
        return userExist
    
class FileManagement(Resource):

    ROOT_FOLDER = Path(__file__).parent.absolute()

    def __init__(self, db=None):
        self.db = db 
        self.uploadsPath = os.path.join(self.ROOT_FOLDER, 'uploads')
        if not os.path.exists(self.uploadsPath):
            os.mkdir(self.uploadsPath)
        

    def post(self):
        auth_header = request.headers.get('Authorization')
        # if not auth_header:
        #     return {'message':'Not user auth token detected'}, HTTPStatus.UNAUTHORIZED
        '''
            If you want to related the file and be able to returned in the future
            you can create a table called login that will contain the authorized tokens and the 
            related userid 

            try to add this, so you will be able to keep login sessions or look for the Flask-JWT for
            a more authomatized way 
        '''
        if 'fileInput' not in request.files:
            return {"error": "No file part"}, HTTPStatus.BAD_REQUEST
        file = request.files['fileInput']
        if file.filename == '':
            return {"error": "No selected file"}, HTTPStatus.BAD_REQUEST
        # be attentive this is a relative path... How will you make it more robust?
        path2save = os.path.join(self.uploadsPath, file.filename)
        file.save(path2save)
        return {"message": "File uploaded successfully!"}, HTTPStatus.OK
