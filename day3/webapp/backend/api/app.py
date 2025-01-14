from flask import Flask 
from flask import request 
from flask import jsonify
from flask_cors import CORS
from http import HTTPStatus

usersTable = {
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
}

app = Flask(__name__)
CORS(app) # Ensure the correct headers 

def logInUser(userData:dict) -> bool:
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
    idsList = list(usersTable.keys())
    for userId in idsList:
        cUser = usersTable[userId]
        if(cUser.get('userPassword') == userData.get('userPassword') and 
           cUser.get('userLastName') == userData.get('userLastName')) :
            return True
    return False

@app.route('/loging', methods=['POST'])
def loging():
    data = request.get_json()
    if logInUser(data):
        return jsonify({"message": "Login successful"}), HTTPStatus.OK
    return jsonify({"message": "Invalid Credentials"}), HTTPStatus.FORBIDDEN

@app.route('/room', methods=['POST'])
def selectedRooms():
    data = request.get_json()
    return jsonify({'message':'approved',
                    'userSelection': data}), HTTPStatus.OK

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'fileInput' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['fileInput']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    # be attentive this is a relative path... How will you make it more robust?
    file.save(f"./uploads/{file.filename}")
    return jsonify({"message": "File uploaded successfully!"})

if __name__ == "__main__":
    app.run(debug=True)