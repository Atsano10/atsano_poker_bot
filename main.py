# 1. Connect to DB, create session
# 2. Loop over hands:
#  - Create hand
#  - Loop over actions (preflop → flop → turn → river):
#      - Make decision
#    - Log action (observer)
#  - Update hand (winner, pot size)
#  - Update profiler for each opponent
# 3. End

from db.database import connect, create_hand, create_session, update_hand
from engine.game import game

conn = connect() 
session_id = create_session(conn) 

num_players = int(input("How many players are in this game:"))
position = 1 #placeholder value

for i in range(20):
    hand_id = create_hand(conn,session_id,num_players,position) 
    winner, pot_size = game(conn, num_players, hand_id,)

    if winner == position:
        outcome = "Win"
    else:
        outcome = "Loss"
        
    update_hand(conn, hand_id, outcome, winner, pot_size)