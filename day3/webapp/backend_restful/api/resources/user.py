from flask import request
from http import HTTPStatus
from flask_restful import Resource

class LoginUsers(Resource):

    DB = {
        0 : {
            'userName' : 'Pablo',
            'userLastName' : 'Rojas',
            'userPassword' : 'qwerty123!'
        },
        1 : {
            'userName' : 'Vladimir',
            'userLastName' : 'Mamutov',
            'userPassword' : 'sk2025'
        },
    } # Fake database to verify the loggin 

    def post(self):
        data = request.get_json()
        if self.logInUser(data):
            return {"message": "Login successful"}, HTTPStatus.OK
        return {"message": "Invalid Credentials"}, HTTPStatus.FORBIDDEN

    def logInUser(self, userData:dict) -> bool:
        '''
            Validate that the user is registered and that the pass is correct

            Parameters
            -----------
                userData : dict, User logging data. e.g: {'userName' : '**',
                                                        'userLastName' : '**', 'userPassword' : '**'},
            
            Return 
            -------
                bool 
                    True if user exist and pass is correct 
                    False if user does not exist or pass is incorrect
        '''
        idsList = list(self.DB.keys())
        for userId in idsList:
            cUser = self.DB[userId]
            if(cUser.get('userPassword') == userData.get('userPassword') and 
            cUser.get('userLastName') == userData.get('userLastName')) :
                return True
        return False

class UserLuggage(Resource):

    def post(self):
        if 'fileInput' not in request.files:
            return {"error": "No file part"}, 400
        file = request.files['fileInput']
        if file.filename == '':
            return {"error": "No selected file"}, 400
        # be attentive this is a relative path... How will you make it more robust?
        file.save(f"./uploads/{file.filename}")
        return {"message": "File uploaded successfully!"}