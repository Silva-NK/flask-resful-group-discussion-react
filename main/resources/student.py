from flask_restful import Resource
from flask import request, make_response, jsonify
from main.models import Student, db

class StudentListResource(Resource):
    def get(self):
        print("Fetching students...")
        students = Student.query.all()
        return [student.to_dict() for student in students],200
    
    def post(self):
        data = request.get_json()

        name = data.get("name")

        if not name :
            return {"error": "Invalid name"},400
        
        student = Student(name=name)
        db.session.add(student)
        db.session.commit()
        return student.to_dict(),201
    

class StudentResource(Resource):
    def get(self, id):
        student = Student.query.filter_by(id=id).first()
        if not student:
            return {"Error": f"Resource not found for id {id}"},404
        return make_response(jsonify(student.to_dict()), 200)
    



