from flask import Flask, request, jsonify
import jwt
#setup

app=Flask(__name__)


#routes

#create

@app.route('/user', methods=['POST'])
def details():
    uname=request.json['uname']
    pswrd=request.json['pswrd']
    authent=request.json['authent']

    return jsonify(jwt.encode({'user':[{'uname':uname},{'pswrd':pswrd}]}, authent))


#verify
@app.route('/user', methods=['GET'])
def verify():
    token=request.json['token']
    auth=request.json['auth']
    ret=jwt.decode(token,auth,algorithms="HS256")
    return jsonify(ret)


#run
if __name__ == '__main__':
    app.run(debug=True)
