from flask import request
from http import HTTPStatus
from flask_restful import Resource

class Poems(Resource):

    def __init__(self, db=None):
        self._db = db 

    def put(self):
        data = request.get_json()
        poem = data.get('poem')
        user_id = data.get('user_id')
        poem_id = data.get('poem_id')
        if self.userIdExist(user_id) or self.poemExist(poem_id):
            if self.updatePoem(poem, poem_id):
                        return {'message':'The update of your poem has been done!'}, HTTPStatus.OK                
        return {'message':'The update of your poem can not be done!'}, HTTPStatus.BAD_REQUEST

    def post(self):
        data = request.get_json()
        poem = data.get('poem')
        user_id = data.get('user_id')
        if self.userIdExist(user_id):
            if self.addPoem(poem, user_id):
                return {'message':'Poem added successfuly'}, HTTPStatus.CREATED
            return {'message':'There was a problem adding your poem!'}, HTTPStatus.BAD_REQUEST
        return {'message':'User not found'}, HTTPStatus.NOT_FOUND

    def get(self):
        data = request.get_json()
        user_name = data.get('name')
        user_pass = data.get('password')
        
        '''
            To improve your API and the frontend think about how will you be able to return the 
            list of poems that a user have 

            Also think about how to use an authentfication token to not request the loging procedure all the time
            as it not possible in a more complicated app 
        '''
        return {'message': 'Here you have the list of poems for the user'}, HTTPStatus.OK

    def updatePoem(self, poem, poem_id):
        SQL_updatePoem = f"UPDATE poems SET poem = '{poem}' WHERE poem_id = '{poem_id}';"
        updateOk = False
        with self._db.cursor() as cursor:
            try:
                cursor.execute(SQL_updatePoem) 
                updateOk = True 
            except Exception as err:
                print(err)
                updateOk = False 
        if not updateOk:
            self._db.rollback()
        self._db.commit()
        return updateOk

    def poemExist(self, poem_id):
        # How will you reduce this peace of replicated code?
        SQL_getPoemId = f"SELECT poem_id FROM poems WHERE poem_id = {poem_id}"
        userExist = False
        with self._db.cursor() as cursor:
            cursor.execute(SQL_getPoemId) 
            try:
                cursor.fetchone()[0]
                userExist = True 
            except Exception as err :
                print(f"Error: {err}")
                userExist = False
        return userExist        

    def addPoem(self, poem, user_id):
        newPoemId = self.getLastPoemId() + 1
        SQL_addPoem = f"INSERT INTO poems(poem_id, poem, user_id) VALUES('{newPoemId}', '{poem}', '{user_id}')"
        poemAdded = False
        with self._db.cursor() as cursor:
            try:
                cursor.execute(SQL_addPoem)
                poemAdded = True  
            except Exception as err:
                # Use print is a bad programing practice to keep an idea of the errors
                # look how to use the package logging
                # https://docs.python.org/3/library/logging.html
                print(err)
                poemAdded = False 
        if poemAdded:
            self._db.commit()
        return poemAdded

    def getLastPoemId(self):
        SQL_getLastPoemId = f"SELECT MAX(poem_id) FROM poems;"
        id2return = -1
        with self._db.cursor() as cursor:
            cursor.execute(SQL_getLastPoemId) 
            try:
                id2return = cursor.fetchone()[0]
            except IndexError:
                id2return = 0
        if isinstance(id2return, type(None)):
            return 0
        return id2return
            
    def userIdExist(self, user_id):
        SQL_getUserId = f"SELECT user_name FROM users WHERE user_id = {user_id}"
        userExist = False
        with self._db.cursor() as cursor:
            cursor.execute(SQL_getUserId) 
            try:
                cursor.fetchone()[0]
                userExist = True 
            except Exception as err :
                print(f"Error: {err}")
                userExist = False
        return userExist
