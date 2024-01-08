from pymongo import MongoClient

db_users_client = MongoClient("mongodb+srv://manu25061994:txyirNewOqtZbRXe@cluster0.vphjuur.mongodb.net/?retryWrites=true&w=majority").users_db
db_lotr_characters_client = MongoClient("mongodb+srv://manu25061994:txyirNewOqtZbRXe@cluster0.vphjuur.mongodb.net/?retryWrites=true&w=majority").lotr_characters_db