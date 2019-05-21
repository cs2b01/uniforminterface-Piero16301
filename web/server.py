from flask import Flask, render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alumnos')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.Alumno)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_test_alumnos', methods = ['GET'])
def create_test_alumnos():
    db_session = db.getSession(engine)
    alumno = entities.Alumno(nombre="Piero", apellido="Morales", carrera="Ciencia de la computacion")
    db_session.add(alumno)
    db_session.commit()
    return "Test alumnos created!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run()