# ! let's get started ! #
import pyperclip
from user_info User, import User, Info

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''

	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)

def verify_user(first_name,password):
	'''
	Function that verifies the exictance of the user before  creating the Info
	'''
	checking_user = Info.check_user(first_name,password)
	return checking_user

def generate 
