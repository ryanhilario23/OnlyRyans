from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


class Posting:
    DB = 'onlyryans_schema'
    def __init__(self,data):
        self.post_id = data['post_id']
        self.post = data['post']
        self.user_id = data['user_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.likes = data['likes']

    @classmethod
    def create_post(cls,data):
        query = """ 
                INSERT INTO postings (user_id, post)
                VALUES (%(user_id)s,%(post)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def ryan_likes(cls,data):
        query = """
        INSERT INTO likes (user_id,post_id)
        VALUES (%(user_id)s,%(post_id)s)
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results


    @classmethod
    def delete_post(cls,post_id):
        query = """
                DELETE FROM posting
                WHERE post_id = %(post_id)s
                """
        data = {'post_id': post_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results