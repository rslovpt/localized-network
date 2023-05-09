from flask import Flask, render_template, request
from server_protocol import server_protocol
from database_handle import db_handler
import json

app = Flask(__name__)
serv_protcl = server_protocol()
db_handlr = db_handler()

@app.route('/db', methods = ['POST', 'GET'])
def db():
    return_statement = 'None'
    if request.method == 'GET':
        auth_passed = False
        if serv_protcl.defineKey(request.args.get('AUTH_KEY')): auth_passed = True
        if request.args.get('data') == "createKey":
            return_statement = serv_protcl.createKey()
        elif request.args.get('data') == "checkKey":
            if serv_protcl.defineKey(request.args.get('AUTH_KEY')):
                return_statement = "accept"
            else: return_statement = "deny"
    else:
        auth_passed = False
        if serv_protcl.defineKey(request.args.get('AUTH_KEY')): auth_passed = True
        if request.args.get('data')[:request.args.get('data').find(':')] == "createDB" and auth_passed:
            DB_ID = str(request.args.get('data')[request.args.get('data').find(':')+1:])
            DB_DATA = json.loads(request.args.get('insertData'))
            return_statement = db_handlr.createDataBase(ID=DB_ID, AUTH_ID=request.args.get('AUTH_KEY'), dataSet=DB_DATA)
        else:
            pass
            
    return return_statement

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)