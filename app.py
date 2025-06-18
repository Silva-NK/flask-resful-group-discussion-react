from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate

from main import db, create_app  
from main.resources.student import StudentListResource, StudentResource
from main.resources.course import CourseListResource, CourseResource
from main.resources.enrollment import EnrollmentListResource, EnrollmentResource

app = create_app() 
api = Api(app)
migrate = Migrate(app, db)


class Home(Resource):
    def get(self):
        return {"Welcome message": "Welcome............"}


# Register resources
api.add_resource(Home, '/')
api.add_resource(StudentListResource, '/students')
api.add_resource(StudentResource, '/students/<int:id>')
api.add_resource(CourseListResource, '/courses')
api.add_resource(CourseResource, '/courses/<int:id>')
api.add_resource(EnrollmentListResource, '/enrollments')
api.add_resource(EnrollmentResource, '/enrollments/<int:id>')


if __name__ == "__main__":
    app.run(port=5555, debug=True)