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
        self.table = []

    @classmethod
    def create_post(cls,data):
        query = """ 
                INSERT INTO postings (user_id, post)
                VALUES (%(user_id)s,%(post)s)
                """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def view_post(cls,post_id):
        query = """ 
                SELECT post, first_name, last_name
                FROM postings
                LEFT JOIN users on postings.user_id = users.user_id
                WHERE postings.post_id = %(post_id)s
                group by first_name, last_name
                """
        data = {'post_id': post_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results[0]
    
    @classmethod
    def ryan_likes(cls,data):
        query = """
        INSERT INTO likes (user_id,post_id)
        VALUES (%(user_id)s,%(post_id)s)
        """
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results

    @classmethod
    def delete_likes(cls,post_id):
        query = """
                DELETE FROM likes
                WHERE post_id = %(post_id)s;
                """
        data = {'post_id': post_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results


    @classmethod
    def delete_post(cls,post_id):
        query = """
                DELETE FROM postings
                WHERE post_id = %(post_id)s;
                """
        data = {'post_id': post_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results