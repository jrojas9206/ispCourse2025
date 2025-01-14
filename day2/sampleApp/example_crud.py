from flask import Flask
from flask import jsonify
from flask import request

from http import HTTPStatus

db_table = {
    cKey : cValue for cKey, cValue in enumerate(['a'*i for i in range(10)])
}

'''
Created table  
{
0: '',
 1: 'a', 
 2: 'aa', 
 3: 'aaa', 
 4: 'aaaa', 
 5: 'aaaaa', 
 6: 'aaaaaa', 
 7: 'aaaaaaa', 
 8: 'aaaaaaaa', 
 9: 'aaaaaaaaa'
 }
'''

app = Flask(__name__)

@app.route('/show', methods=['GET'])
def showTable():
    return jsonify(db_table)

@app.route('/search/<int:tableid>', methods=['GET'])
def search(tableid):
    if tableid not in list(db_table.keys()):
        return jsonify({'message':'Index not found'})
    return jsonify({'result':db_table[tableid]})

@app.route('/addvalue', methods=['POST'])
def addValue():
    data = request.get_json()
    id2add = int(data.get('id'))
    value2add = data.get('value')
    print(type(id2add),id2add, value2add)
    if id2add not in list(db_table.keys()):
        db_table[id2add] = value2add
    else:     
        return jsonify({'message':'Index already exist'}), HTTPStatus.OK
    return jsonify({'message':'New index created',
                    'table':db_table}), HTTPStatus.CREATED


if __name__ == '__main__':
    app.run(debug=True)