import sqlite3
from datetime import datetime

def connect():
    conn = sqlite3.connect('db/poker.db') #opens the database file or creates it, returns a connection object
    with open ("db/schema.sql", "r") as database: #opens schema.sql in read mode
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
def create_hand(conn, session_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hands(session_id, num_players, position) VALUES (?, ?, ?)", (session_id, 2, 0)) #always heads-up, bot is position 0
    conn.commit()

    hand_id = cursor.lastrowid
    return hand_id

#updates the hand after the round is done 
def update_hand(conn, hand_id, outcome, winner_id, pot_size):
    cursor = conn.cursor()
    cursor.execute("UPDATE hands SET outcome = ?, winner_id = ?, pot_size = ? WHERE hand_id = ?",(outcome, winner_id, pot_size, hand_id)) #updates hands with values
    conn.commit()
    
    hand_id = cursor.lastrowid
    return

# logs one opponent decision to the decision table
def insert_decision(conn, actions, player_id, hand_id, street, pot_size, amount):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO decisions (actions, player_id, hand_id, street, pot_size, amount) VALUES (?,?,?,?,?,?)", (actions, player_id, hand_id, street, pot_size, amount))
    conn.commit()

    decision_id = cursor.lastrowid
    return decision_id


# upserts their profile
def update_stats(conn, player_id, aggression, playstyle, vpip, hands_played, PFR, three_bet):
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO stats (player_id, aggression, playstyle, vpip, hands_played, PFR, three_bet) VALUES (?,?,?,?,?,?,?)", (player_id, aggression, playstyle, vpip, hands_played, PFR, three_bet))
    conn.commit()

    stats_id = cursor.lastrowid
    return 

# returns the player_stats row for one player
def get_stats(conn, player_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stats WHERE player_id = ?", (player_id,)) #reads data from db

    stats_id = cursor.fetchone() #retrieves only one row from the query
    return stats_id

# returns all player profiles (used by streamlit)
def all_player_stats(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stats")

    return cursor.fetchall() #rettrieves all rows and returns them

# returns the players actions
def get_player_actions(conn,player_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * from decisions WHERE player_id = ?", (player_id,))

    return cursor.fetchall()
