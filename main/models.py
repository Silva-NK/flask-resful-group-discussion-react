from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from main import db

class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    enrollments = db.relationship('Enrollment', back_populates='student', cascade='all, delete-orphan')
    courses = db.relationship('Course', secondary='enrollments', viewonly=True)

    # Prevent circular serialization
    serialize_rules = ('-enrollments.student', '-courses')

    def __repr__(self):
        return f"<Student {self.name}>"


class Course(db.Model, SerializerMixin):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    enrollments = db.relationship('Enrollment', back_populates='course', cascade='all, delete-orphan')
    students = db.relationship('Student', secondary='enrollments', viewonly=True)

    # Prevent circular serialization
    serialize_rules = ('-enrollments.course', '-students')

    def __repr__(self):
        return f"<Course {self.title}>"


class Enrollment(db.Model, SerializerMixin):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String)

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')

    serialize_rules = ('-student.enrollments', '-course.enrollments')

    def __repr__(self):
        return f"<Enrollment {self.student_id} Course={self.course_id} Grade={self.grade}>"
