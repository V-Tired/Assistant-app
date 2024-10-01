import mysql.connector
from mysql.connector import Error
import os

"""A module to handle the database that controls events and their dates."""

USER_PWORD = os.environ['USER_PWORD']
USER_NAME = os.environ['USER_NAME']


class DbMaker:
    def __init__(self):
        self.host = "localhost"
        self.user_name = USER_NAME
        self.user_pword = USER_PWORD
        self.db_name = "scheduled_events"

        con = self.create_server_connection()
        self.create_database(con)
        connection = self.create_db_connection()
        self.connection = connection
        self.initialize_event_table(self.connection)

    def create_server_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user_name,
                passwd=self.user_pword
            )
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def create_database(self, connection):
        query = "CREATE DATABASE IF NOT EXISTS scheduled_events"
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Error as err:
            print(f"Error: '{err}'")

    def create_db_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user_name,
                passwd=self.user_pword,
                database=self.db_name
            )
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    def execute_query(self, connection, query: str):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
        except Error as err:
            print(f"Error:'{err}'")

    def initialize_event_table(self, connection):
        create_event_table = """
             CREATE TABLE IF NOT EXISTS events(
             id INT PRIMARY KEY,
             note VARCHAR(500) NOT NULL,
             month INT NOT NULL,
             day INT NOT NULL);"""
        self.execute_query(connection, create_event_table)

    def add_to_events(self, note: str, month: str, day: str):
        """Takes user inputted note, month, and day, and adds it as a new entry in the database at the bottom
         of the list."""
        num = self.read_data(self.connection)[-1][0] + 1
        connection = self.create_db_connection()
        event = f"""INSERT INTO events VALUES
        ({num}, '{note}', {month}, {day});"""
        self.execute_query(connection, query=event)

    def read_data(self, connection) -> list:
        """Pulls all the data from events and return them to be displayed."""
        query = """SELECT * FROM events;"""
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def delete_entry(self, entry_id: str):
        """Takes user inputted id number and deletes the corresponding entry."""
        delete_entry = f"""
        DELETE FROM events 
        WHERE id = {entry_id};
        """
        self.execute_query(self.connection, delete_entry)


