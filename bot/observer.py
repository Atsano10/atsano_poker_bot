from db.database import insert_decision

def log_action(conn, hand_id, player_id, street, actions, amount): #logs all the opponent info
    insert_decision(conn, actions, player_id, hand_id, street, amount) #writes it to the decision table
    return

# FUTURE
# validate street and actions