##
# ARCHETYPES
# 1. Aggressor: Raises pre flop, enters many hands, call to fold ratio would be high
# 2. Calling station # highest amount of hands, re raises on safe hands onnly otherwise call, low post flop aggression
# 3. Rock (only plays safe hands) low call to fold ratio plays only premiums, not alot of hands
# 4. Big better like aggressor but higher pot size
# 5. Shark (re raises you after he checked initially) most balanced player check raise will be high
# ##
from db.database import get_stats, update_stats, get_player_actions

def update_profile(conn, player):
    player_actions = get_player_actions(conn, player)

    preflop_actions = [row for row in player_actions if row[4] == 'preflop'] # make a list of only the preflop 
    preflop_call = [ x for x in preflop_actions if x[1] == 'call'] # count how many calls in preflop
    preflop_raise = [ x for x in preflop_actions if x[1] == 'raise'] # count how many raises in preflop
    total_hands = len(set(row[3] for row in player_actions)) # count the total amount of unique hand_ids

    # calculate vpip
    vpip = ((len(preflop_call)+len(preflop_raise))/(total_hands))

    # calculate aggresion
    


    return