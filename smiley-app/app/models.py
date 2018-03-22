from flask import UserMixin
from werkzeug import generate_password_hash,check_password_hash


from app import db, lm


class Employee(UserMixin, db.model):
	'''
		Employee table
	'''

	tablename = 'employees'

	id = db.Column(db.Integer, primary=True)
	email = db.Column(db.String(60), index=True, unique=True)
	first_name = db.Column(db.String(60), index=True, unique=True)
	last_name = db.Column(db.String(60), index=True)
	password_hash = db.Column(db.String(128))

	