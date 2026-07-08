import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from db.database import connect, all_player_stats

conn = connect() #connect to the db
stats = all_player_stats(conn) #store all stats in a variable

st.title("Poker Bot Dashboard") # give a title

table = []
for row in stats:
    table.append({"Player": row[1], "Archetype": row[3], "VPIP": row[4], "Aggresion": row[2], "Hands Seen": row[5]})

st.table(table)
