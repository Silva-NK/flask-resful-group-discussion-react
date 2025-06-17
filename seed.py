# seed.py
from main.models import db, Student, Course, Enrollment
from app import app

with app.app_context():
    print("Seeding data...")

    # Clear existing data
    Enrollment.query.delete()
    Student.query.delete()
    Course.query.delete()

    # Create students
    s1 = Student(name="Alice")
    s2 = Student(name="Bob")
    s3 = Student(name="Charlie")

    # Create courses
    c1 = Course(title="Mathematics")
    c2 = Course(title="History")
    c3 = Course(title="Biology")

    db.session.add_all([s1, s2, s3, c1, c2, c3])
    db.session.commit()

    # Create enrollments
    e1 = Enrollment(student_id=s1.id, course_id=c1.id, grade="A")
    e2 = Enrollment(student_id=s1.id, course_id=c2.id, grade="B")
    e3 = Enrollment(student_id=s2.id, course_id=c2.id, grade="A")
    e4 = Enrollment(student_id=s3.id, course_id=c3.id, grade="C")

    db.session.add_all([e1, e2, e3, e4])
    db.session.commit()

    print("Done seeding!")