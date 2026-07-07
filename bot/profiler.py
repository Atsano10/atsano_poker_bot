from db.database import update_stats, get_player_actions

def update_profile(conn, player):
    player_actions = get_player_actions(conn, player) #make a list of every action

    preflop_actions = [row for row in player_actions if row[4] == 'preflop'] # make a list of only the preflop 
    preflop_calls = len([ x for x in preflop_actions if x[1] == 'call']) # count how many calls in preflop
    preflop_raises = len([ x for x in preflop_actions if x[1] == 'raise']) # count how many raises in preflop
    total_hands = len(set(row[3] for row in player_actions)) # count the total amount of unique hand_ids
    # calculate vpip
    if total_hands == 0: vpip = 0
    else:vpip = (((preflop_calls)+(preflop_raises))/(total_hands))


    total_calls = len([x for x in player_actions if x[1] == 'call']) # counts amount of calls
    total_raises = len([x for x in player_actions if x[1] == 'raise']) #counts amount of raises
    # calculate aggresion
    if total_calls + total_raises == 0 : aggression = 0
    else:aggression = (total_raises)/(total_raises + total_calls)

    # calculate PFR
    if total_hands == 0: PFR = 0
    else: PFR = preflop_raises/total_hands

    # calculate 3-Bet (add later after basic game is completed, requires tracking decisions)

    # classifies as an archetype (add more when including more info)
    if (vpip < .18 and PFR < .14 and aggression > 0.25 and aggression < 0.55):
        archetype = "Rock"
    elif (vpip < .18 and vpip > .12 and PFR < .23 and PFR > .17 and aggression > 0.55):
        archetype = "TAG"
    elif (vpip < .35 and vpip > .25 and PFR < .28 and PFR > .20 and aggression > 0.55):
        archetype = "LAG"
    elif (vpip < .35 and vpip > .25 and PFR < .14 and aggression < 0.40):
        archetype = "Calling Station"
    elif (vpip > .35 and PFR < .14 and aggression > 0.70):
        archetype = "Maniac"
    elif(vpip < .35 and vpip > .25 and PFR < .08 and aggression < 0.40):
        archetype = "Fish"
    else:
        archetype = "Unknown"
        
    update_stats(conn, player, aggression, archetype, vpip, total_hands, PFR, 0)
    return  