from flask_restful import Resource
from flask import make_response, jsonify
from main.models import db, Course


class CourseListResource(Resource):
    def get(self):
        courses = Course.query.all()

        if not courses:
            return {"error":"no courses found!"}
        
        return [course.to_dict() for course in courses],200
    
class CourseResource(Resource):
    def get(self, id):
        course = Course.query.filter_by(id=id).first()
        return course.to_dict(), 200
