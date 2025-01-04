from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME
import logging

class MongoDBConnection:
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        try:
            # Create a MongoClient to the running mongod instance
            self.client = MongoClient(MONGO_URI)
            # Connect to the database
            self.db = self.client[DATABASE_NAME]
            logging.info("Connected to MongoDB successfully.")
        except Exception as e:
            logging.error(f"Error connecting to MongoDB: {e}")
            raise

    def get_database(self):
        if self.db is None:
            logging.error("Database connection is not established.")
            raise ConnectionError("Database connection is not established.")
        return self.db

    def close(self):
        if self.client:
            self.client.close()
            logging.info("MongoDB connection closed.")
