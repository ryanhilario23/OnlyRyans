from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWOR_REGEX = re.compile(r'a-zA-Z0-9.+_-')


class Ryan:
    def __init__(self,data):
        self.id = data['user_id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.password = data['password'],
        self.passowrd_c = data['password_c']

    @classmethod
    def login_ryan(cls,data):
        if not EMAIL_REGEX.match(data['email']):
            return False
        query = """
                SELECT *
                FROM users
                WHERE email = %(email)s
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results[0]
    





    @classmethod
    def submit_ryan_entry(cls,data):
        query = """
                INSERT INTO ryan_entrys (name,email)
                VALUES (%(name)s,%(email)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results

#Static Methods

    @staticmethod
    def validate_login(form):
        info_valid = True
        if len(form['email']) < 3 and len(form['password']) < 3:
            flash('Please insert email and password', 'login')
            info_valid = False
        return info_valid
    
    @staticmethod
    def invalid_account():
        flash('invalid email/password Ryan', 'login')
        return
    

    @staticmethod
    def brian_check(form):
        # Can I do a SQL check for table of Bryans name.
        info_valid = True
        if form['name'] == 'Brian' or form['name'] == 'Bryan':
            flash('No Brians allowed.', 'ryan_register')
            info_valid = False
        return info_valid

    @staticmethod 
    def validate_name(form):
        info_valid = True
        if len(form['ryan_name']) < 3 and len(form['email']) < 3:
            flash('Please insert your name and email.','ryan_register')
            info_valid = False
        return info_valid
    