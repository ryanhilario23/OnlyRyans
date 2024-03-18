from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Survey:
    DB ='onlyryans_schema'
    def __int__(self,data):
        self.entry = data['entry'] #amount of entries
        self.name = data['ryan_name']#The name to be questioned

# Creating the entry name
    @classmethod
    def submit_entry(cls,data):
        query = """
                INSERT INTO entrys (name,email)
                VALUES (%(ryan_name)s, %(email)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        flash('Your Ryan name has been submitted.', 'ryan_register')
        return results

    @classmethod
    def view_all_entry(cls):
        query = """ 
                SELECT name, entrys.entry_id,
                COUNT(CASE WHEN vote = 'Yes' THEN 1 END) AS 'yes',
                COUNT(CASE WHEN vote = 'No' THEN 1 END) AS 'no'
                FROM vote
                LEFT JOIN entrys ON entrys.entry_id = vote.entry_id
                GROUP BY name,entrys.entry_id
                """
        results = connectToMySQL(cls.DB).query_db(query)
        return results

# user casting a vote
    @classmethod
    def submit_vote(cls,data):
        query = """ 
                INSERT INTO vote (entry_id,vote,user_id)
                VALUES (%(entry_id)s,%(vote)s,%(user_id)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
# See the votes casted
# Votes are based True and false ()
    @classmethod
    def viewed_votes(cls,entry_id):
        query = """ 
                SELECT entrys.name, COUNT(vote.vote) as vote 
                FROM entrys
                Left JOIN vote ON entrys.entry_id = vote.entry_id
                LEFT JOIN users on users.user_id = vote.entry_id
                WHERE entrys.entry_id = %(entry)s
                GROUP BY vote.vote
                """
        data ={'entry_id': entry_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def check_name_submitted(cls,data):
        query = """
                SELECT *
                FROM entrys
                WHERE name = %(ryan_name)s
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        if results:
            flash('Your Ryan name has already submitted.', 'ryan_register')
            return results
        else:
            return results
        


    @staticmethod
    def survey_email(form):
        info_valid = True
        if len(form['email']) < 5:
            flash('Please insert your email','register')
            flash('Please insert your email','ryan_register')
            info_valid = False
            if not EMAIL_REGEX.match(form['email']):
                flash('Invalid email address','register')
                flash('Invalid email address','ryan_register')
                info_valid = False
        return info_valid