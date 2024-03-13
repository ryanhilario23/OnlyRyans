from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWOR_REGEX = re.compile(r'a-zA-Z0-9.+_-')


class Ryan:
    DB = 'onlyryans_schema'
    def __init__(self,data):
        self.id = data['user_id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.password = data['password'],
        self.passowrd_c = data['password_c']

    @classmethod
    def login_ryan(cls,data):
        query = """
                SELECT *
                FROM users
                WHERE email = %(email)s
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(results)
        return results[0]

    @classmethod
    def get_user(cls,data):
        query = """ 
                SELECT *
                FROM users
                WHERE user_id = %(user_id)s
                """
        user = {'user_id': data}
        results = connectToMySQL(cls.DB).query_db(query,user)
        return results[0]


# Save data to DB 
    @classmethod
    def save_ryan(cls,data):
        query = """
                INSERT INTO users (first_name, last_name, email, password)
                VALUES (%(ryan_name)s,%(last_name)s,%(email)s,%(password)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results

    @classmethod
    def submit_ryan_entry(cls,data):
        query = """
                INSERT INTO ryan_entrys (name,email)
                VALUES (%(name)s,%(email)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
# No Brian checks
    @classmethod
    def brian_check(cls,data):
        query = """
                SELECT name
                FROM brians
                WHERE name = %(ryan_name)s
                LIMIT 1;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(results)
        if results:
            flash('No Brians allowed.', 'ryan_register')
            flash('No Brians allowed.', 'register')
        return results
    
# Valid Ryan check
    @classmethod
    def ryan_name_check(cls,data):
        print('ryancheck')
        query = """
                SELECT name
                FROM ryans
                WHERE name = %(ryan_name)s
                LIMIT 1;
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        if results == 1:
            flash('Valid Ryan names only. Register your ryan name to validate','register')
        return results
    
# Check for email already registered
    @classmethod
    def registered_ryan(cls,data):
        print('emailcheck')
        query = """
                SELECT email
                FROM users
                WHERE email = %(email)s
                LIMIT 1; 
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        print('here',results)
        if results:
            flash('email already taken','register')
        return results


#Static Methods
    @staticmethod
    def validate_register(form):
        info_valid = True
        print(form)
        if form['ryan_name'] == '':
            flash('Please fill out form', 'register')
            info_valid = False
            return info_valid
        if len(form['ryan_name']) < 3:
            flash('Please insert your Ryan name','register')
            info_valid = False
        if len(form['last_name']) < 3:
            flash('Please insert your Last name','register')
            info_valid = False
        if len(form['email']) < 5:
            flash('Please insert your email','register')
            info_valid = False
            if not EMAIL_REGEX.match(form['email']):
                flash('Invalid email address','register')
                info_valid = False
        if len(form['password']) < 8:
            flash('Password must be at least 8 characters long', 'register')
            info_valid = False
        if form['password'] != form['password_check']:
            flash('Password does not match', 'register')
        return info_valid

    @staticmethod
    def validate_login(form):
        info_valid = True
        if len(form['email']) < 3 or len(form['password']) < 3:
            flash('Please insert email and password', 'login')
            info_valid = False
        return info_valid
    
    @staticmethod
    def invalid_account():
        flash('invalid email/password Ryan', 'login')
        return

    @staticmethod 
    def validate_name(form):
        info_valid = True
        if len(form['ryan_name']) < 3 or len(form['email']) < 3:
            flash('Please insert your name and email.','ryan_register')
            info_valid = False
        print('name check')
        return info_valid
    