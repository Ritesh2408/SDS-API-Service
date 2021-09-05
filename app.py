import os
from flask import Flask,  request, jsonify
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from flask_jwt import JWT ,jwt_required
from flask_migrate import Migrate

app = Flask(__name__)
#configuring and setting up database
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/Ritesh Chaudhari/Desktop/SDS_API/sds.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db)
#jwt = JWT(app, authenticate, identity)
api = Api(app)

#CREATING models

class SDS(db.Model):

    id = db.Column(db.Integer,primary_key=True, nullable=True)
    name = db.Column(db.String(80))
    mis = db.Column(db.Integer())
    email = db.Column(db.String())


    def __init__(self,name,mis,email):
        self.name=name
        self.mis=mis
        self.email=email

    def json(self):
        return {'name: ': self.name,'MIS: ':self.mis,'Email: ':self.email}

    def __str__(self):
        return f" Name of registered student: {self.name}\nMIS: {self.mis}\nEmail: {self.email}"

#Setting up routes
@app.route('/')
def Index():
    students = SDS.query.all()

    return render_template("index.html", students = students)

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        mis = request.form['mis']


        my_data = SDS(name, email, mis)
        db.session.add(my_data)
        db.session.commit()

        flash("Student Inserted Successfully")

        return redirect(url_for('Index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = SDS.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.mis = request.form['mis']

        db.session.commit()
        flash("Student Updated Successfully")

        return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = SDS.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Student Deleted Successfully")

    return redirect(url_for('Index'))


#RESIURCESSS

class SDSResource(Resource):
    def get(self,name,mis,email):

        obj = SDS.query.filter_by(name=name,mis=mis,email=email).first()


        if obj:
            return obj.json()
        else:

            return {'name':'not found'}, 404

    def post(self,name,mis,email):

        obj = SDS(name=name,mis=mis,email=email)
        db.session.add(obj)
        db.session.commit()

        return obj.json()


    def delete(self,name,mis,email):

        obj = SDS.query.filter_by(name=name,mis=mis,email=email).first()
        db.session.delete(obj)
        db.session.commit()

        return {'note':'delete successful'}


class AllStudents(Resource):

    #@jwt_required()
    def get(self):
        # return all the students data
        students = SDS.query.all()

        # return json of students  into a list.
        return [obj.json() for obj in students]



api.add_resource(SDSResource, '/user/<string:name>/<int:mis>/<string:email>')
api.add_resource(AllStudents,'/students')

if __name__ == "__main__":
    app.run(debug=True)
