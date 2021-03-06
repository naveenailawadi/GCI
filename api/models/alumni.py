from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import db

'''

app = Flask(__name__)

app.config['SECRET_KEY'] = '45e2b67051014e2ba07df47f533c1f14'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alumni.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

'''

class AlumniModel(db.Model):

    __tablename__ = 'alumni'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    linkedin_url = db.Column(db.String(100), nullable = True)
    job_title = db.Column(db.String(100), nullable = True)
    job_title_role = db.Column(db.String(100), nullable = True)
    job_company = db.Column(db.String(100), nullable = True)
    job_company_industry = db.Column(db.String(100), nullable = True)
    job_company_locations_locality = db.Column(db.String(100), nullable = True)
    phone_numbers = db.relationship("PhoneNumberModel", backref="alumni")
    emails = db.relationship("EmailModel", backref="alumni")
    interests = db.relationship("InterestModel", backref="alumni")
    experiences = db.relationship("ExperienceModel", backref="alumni")
    education = db.relationship("SchoolModel", backref="alumni")

    def __repr__(self):
        return '<Alumni %r>' % self.first_name


class PhoneNumberModel(db.Model):
    __tablename__ = "phone_number"
    id = db.Column(db.Integer, primary_key=True)
    ph_number = db.Column(db.String(12), nullable = True)
    alumni_id = db.Column(
        db.Integer, db.ForeignKey("alumni.id"))


class EmailModel(db.Model):
    __tablename__ = "email"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable = True)
    alumni_id = db.Column(
        db.Integer, db.ForeignKey("alumni.id"))


class InterestModel(db.Model):
    __tablename__ = "interest"
    id = db.Column(db.Integer, primary_key=True)
    interest = db.Column(db.String(100), nullable = True)
    alumni_id = db.Column(
        db.Integer, db.ForeignKey("alumni.id"))


class ExperienceModel(db.Model):
    __tablename__ = "experience"
    id = db.Column(db.Integer, primary_key=True)
    company = db.relationship("CompanyModel", backref="experience")
    start_date = db.Column(db.DateTime, nullable = True)
    end_date = db.Column(db.DateTime, nullable = True)
    title_name = db.Column(db.String(100), nullable = True)
    title_role = db.Column(db.String(100), nullable = True)

    alumni_id = db.Column(
        db.Integer, db.ForeignKey("alumni.id"))


class CompanyModel(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = True)
    location = db.relationship("LocationModel", backref="company")
    experience_id = db.Column(
        db.Integer, db.ForeignKey("experience.id"))


class LocationModel(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable = True)
    state = db.Column(db.String(100), nullable = True)
    country = db.Column(db.String(100), nullable = True)
    zipcode = db.Column(db.Integer, nullable = True)
    locality = db.Column(db.String(100), nullable = True)

    company_id = db.Column(
        db.Integer, db.ForeignKey("company.id"))


class SchoolModel(db.Model):
    __tablename__ = "school"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = True)
    start_date = db.Column(db.DateTime, nullable = True)
    end_date = db.Column(db.DateTime, nullable = True)
    majors = db.relationship("MajorModel", backref="school")
    minors = db.relationship("MinorModel", backref="school")

    alumni_id = db.Column(
        db.Integer, db.ForeignKey("alumni.id"))


class MajorModel(db.Model):
    __tablename__ = "major"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = True)

    school_id = db.Column(
        db.Integer, db.ForeignKey("school.id"))


class MinorModel(db.Model):
    __tablename__ = "minor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = True)

    school_id = db.Column(
        db.Integer, db.ForeignKey("school.id"))
