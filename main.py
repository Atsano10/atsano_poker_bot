# 1. Connect to DB, create session
# 2. Loop over hands:
#  - Create hand
#  - Run game (bot vs opponent, heads-up)
#  - Update hand (winner, pot size)
# 3. End

from db.database import connect, create_hand, create_session, update_hand
from engine.game import game, BOT #import BOT constant to check winner

conn = connect()
session_id = create_session(conn)

for i in range(20): #run 20 hands
    hand_id = create_hand(conn, session_id) #always heads-up, hardcoded in create_hand
    winner, pot_size = game(conn, hand_id)

    if winner == BOT: #check if our bot won
        outcome = "Win"
    else:
        outcome = "Loss"

    update_hand(conn, hand_id, outcome, winner, pot_size)