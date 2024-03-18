from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.Accounts import Accounts
from flask_app.models.Postings import Posting
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWOR_REGEX = re.compile(r'a-zA-Z0-9.+_-')


class Ryan:
    DB = 'onlyryans_schema'
    def __init__(self,data):
        self.id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.ryan_account = []
        self.ryan_posts =[]
        self.table = []

    @classmethod
    def login_ryan(cls,data):
        query = """
                SELECT *
                FROM users
                WHERE email = %(email)s
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        if results == ():
            Ryan.invalid_account()
            return
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
        query = """
                SELECT email
                FROM users
                WHERE email = %(email)s
                LIMIT 1; 
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        if results:
            flash('email already taken','register')
        return results

# Profile gathering
    @classmethod
    def ryan_details(cls,id):
        query = """ 
                SELECT users.user_id, users.first_name,users.last_name,users.email,users.password, accounts.facebook, accounts.instagram, accounts.snapchat, accounts.twitter,                 
                COUNT(DISTINCT postings.post_id) AS posts,
                COUNT(DISTINCT likes.likes_id) AS likes
                FROM users
                LEFT JOIN accounts ON users.user_id = accounts.user_id
                LEFT JOIN postings ON users.user_id = postings.user_id
                LEFT JOIN likes ON users.user_id = likes.user_id
                WHERE users.user_id = %(user_id)s
                GROUP BY users.user_id, users.first_name, accounts.facebook, accounts.instagram, accounts.snapchat, accounts.twitter;
                """
        data = {'user_id': id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(results[0])
        account = cls(results[0])
        for details in results:
            account_details = {
                'user_id': details['user_id'],
                'first_name': details['first_name'],
                'last_name': details['last_name'],
                'facebook': details['facebook'],
                'instagram': details['instagram'],
                'twitter': details['twitter'],
                'snapchat': details['snapchat'],
            }
        account.ryan_account.append(Accounts(account_details))
        return results[0]



    @classmethod
    def show_all_post(cls):
        query = """
                SELECT postings.post_id,postings.post , COUNT(likes.user_id) as likes,users.user_id,users.first_name,users.last_name,users.email,users.password
                FROM users
				RIGHT JOIN postings ON postings.user_id = users.user_id
                LEFT JOIN likes on likes.post_id = postings.post_id
                group by post_id;
                """
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        post = cls(results[0])
        for ryan in results:
            ryans_post ={
                'post_id': ryan['post_id'],
                'post': ryan['post'],
                'user_id': ryan['user_id'],
                'first_name': ryan['first_name'],
                'last_name': ryan['last_name'],
                'likes': ryan['likes']
            }
        post.ryan_posts.append(Posting(ryans_post))
        return results
    

    @classmethod
    def who_likes_this(cls,post_id):
        query = """ 
                SELECT users.user_id,users.first_name, users.last_name, COUNT(likes.user_id) AS like_count
                FROM postings
                LEFT JOIN likes ON likes.post_id = postings.post_id
                LEFT JOIN users ON likes.user_id = users.user_id
                WHERE postings.post_id = %(post_id)s
                GROUP BY users.user_id, users.first_name, users.last_name;
                """
        data = {'post_id': post_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
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
        flash('invalid email/password', 'login')
        return

    @staticmethod 
    def validate_name(form):
        info_valid = True
        if len(form['ryan_name']) < 3 or len(form['email']) < 3:
            flash('Please insert your name and email.','ryan_register')
            info_valid = False
        print('name check')
        return info_valid
    