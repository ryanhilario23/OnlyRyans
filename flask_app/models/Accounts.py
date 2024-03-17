from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re



class Accounts:
    DB = 'onlyryans_schema'
    def __init__(self,data):
        self.user_id = data['user_id']
        self.facebook = data['facebook']
        self.instagram = data['instagram']
        self.twitter = data['twitter']

        self.first_name = data['first_name']
        self.last_name = data['last_name']


    @classmethod 
    def create_account(cls,id):
        query = """
                INSERT INTO accounts (user_id, facebook, instagram, twitter,snapchat)
                VALUES (%(user_id)s,'','','')
                """
        data = {'user_id': id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results

    @classmethod
    def save_accounts (cls,data):
        query = """
                INSERT INTO accounts (user_id, facebook, instagram, twitter,snapchat)
                VALUES (%(user_id)s,%(facebook)s,%(instagram)s,%(twitter)s,%(snapchat)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def update_accounts(cls,data):
        query = """
                UPDATE accounts
                SET facebook = %(facebook)s, instagram=%(instagram)s,
                twitter = %(twitter)s, snapchat =%(snapchat)s
                WHERE user_id = %(user_id)s
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results


    @classmethod
    def get_saved_accounts(cls,id):
        query = """ 
                SELECT *
                FROM accounts
                WHERE user_id = %(user_id)s
                """
        data = {'user_id': id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        if results ==():
            return results
        return results[0]
