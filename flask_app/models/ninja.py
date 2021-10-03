from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.location = data['location']
        self.languages = data['languages']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (name, location, language, comments, created_at,updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comments)s, NOW(),NOW())"
        return connectToMySQL('dojo_survey_users').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        ninja_from_db =  connectToMySQL('dojo_survey_users').query_db(query)
        ninjas =[]
        for ninja in ninja_from_db:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        ninja_from_db = connectToMySQL('dojo_survey_users').query_db(query,data)

        return cls(ninja_from_db[0])

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True # we assume this is true
        if len(ninja['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(ninja['comments']) < 1:
            flash("Please add a comment.")
            is_valid = False
        return is_valid

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE books SET title=%(title)s, num_of_pages = %(num_of_pages)s, updated_at = NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('dojo_survey_users).query_db(query,data)

    # @classmethod
    # def destroy(cls,data):
    #     query = "DELETE FROM books WHERE id = %(id)s;"
    #     return connectToMySQL('dojo_survey_users).query_db(query,data)


    # @classmethod
    # def get_book_with_authors( cls , data ):
    #     query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
    #     results = connectToMySQL('dojo_survey_users).query_db( query , data )
    #     # results will be a list of topping objects with the burger attached to each row. 
    #     book = cls( results[0] )
    #     for row_from_db in results:
    #         # Now we parse the topping data to make instances of toppings and add them into our list.
    #         author_data = {
    #             "id" : row_from_db["authors.id"],
    #             "name" : row_from_db["name"],
    #             "created_at" : row_from_db["authors.created_at"],
    #             "updated_at" : row_from_db["authors.updated_at"]
    #         }
    #         book.fav_authors.append( author.Author( author_data ) )
    #     return book

    # @classmethod
    # def unfavorited_books(cls, data):
    #     query = "SELECT * FROM books WHERE books.id NOT IN (SELECT book_id FROM favorites WHERE author_id = %(id)s);"
    #     results = connectToMySQL('dojo_survey_users).query_db( query , data )
    #     books = []
    #     for row in results:
    #         books.append(cls(row))
    #     return books
