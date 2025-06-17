from flask_restful import Resource
from flask import request
from main.models import db, Enrollment


class EnrollmentListResource(Resource):
    def get(self):
        enrolments = Enrollment.query.all()

        if not enrolments:
            return {"error": "Enrollments not found"}
        return [enrolment.to_dict() for enrolment in enrolments], 200


class EnrollmentResource(Resource):
    def get(self, id):
        enrollment = Enrollment.query.filter_by(id=id).first()

        if not enrollment:
            return {"error": "enrollment resourse not found"}
        
        return enrollment.to_dict(), 200
