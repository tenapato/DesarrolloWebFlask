from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient, cursor

app = Flask(__name__) 

con = MongoClient('localhost', 27017)
db = con.Escuela
cuentas = db.alumno

@app.route('/')
def index():
    cursor = cuentas.find()
    user = []
    
    for doc in cursor:
        user.append(doc)
        
    return render_template('/users.html', data=user)
    #return redirect(url_for('test', data="Pato"))
    #return render_template('/login.html', data="Pato")

@app.route('/login', methods=["POST"])
def login():
    password = request.form["password"]
    return "tu password es: %s" % password

@app.route('/test/<data>')
def test(data=None):
    return "Hola %s" % data


if __name__ == '__main__':
    app.run(debug=True)