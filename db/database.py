import sqlite3
from datetime import datetime

def connect():
    conn = sqlite3.connect('db/poker.db') #opens the database file or creates it, returns a connection object
    with open ("schema.sql", "r") as database: #opens schema.sql in read mode
        content = database.read() #saves the sql file into a string
        conn.executescript(content) #runs the sql
    return conn 

def create_session(conn): #takes in the connection to define db
    cursor = conn.cursor() #creates a cursor to send SQL commands
    cursor.execute("INSERT INTO sessions(start_time) VALUES (?)", (datetime.now(),)) #sends INSERT
    conn.commit() #saves the INSERT

    session_id = cursor.lastrowid #saves the id of the last INSERT
    return session_id 

# inserts a new hand row, returns its id
def create_hand():
    return 0
# logs one opponent action to the actions table
def insert_action():
    return 0

# returns the player_stats row for one player
def get_stats():
    return 0

# upserts their profile
def update_stats():
    return 0

#returns all player profiles (used by streamlit)
def all_player_stats():
    return 0
