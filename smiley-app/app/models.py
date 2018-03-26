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

	department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	is_admin = db.Column(db.Boolean, default=False)


	@property
	def password(self):
		# prevent password from being accessed
		raise AttributeError('Password is not a readable attribute')

	@password.setter
	def password(self, password):
		# Set hashed password

		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		# Verify password

		return check_password_hash(password_hash)
	def __repr(self):

		return '<Employee: {}'.format(self.username>)



# User loader setup
@lm.user_loader
def load_user(user_id):
	return Employee.query.get(int(user_id))

class Department(db.model):
	'''
	Department table creation

	'''

	__tablename__ = 'departments'

	id = db.Column(db.Integer, primary = True) 
	name = db.Column(db.String(100), unique = True)
	description = db.Column(db.String(1000))
	employees = db.relationship('Employee', backref = 'department', lazy='dynamic')


	def __repr__(self):
		return 'Department: {}'.format(self.name)


class Role(object):
	
	__tablename__ = 'roles'

	id = db.Column(db.Integer, unique=True)
	name = db.Column(db.String(100), unique = True)
	description = db.Column(db.String(1000))
	employees = db.relationship('Employee', backref = )

	def __repr__(self):
		return 'Roles: {}'.format(self.name)
		


