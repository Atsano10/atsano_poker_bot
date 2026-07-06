# Future
# account for all players not only one

from equity import estimate_equity
from db.database import get_stats

def decide(pocket_cards,community_cards, pot, to_call, player_id, num_opponents, conn):
    simulations = 500 #hardcoded sims

    equity = estimate_equity(pocket_cards, community_cards, num_opponents, simulations) # runs Monte Carlo for W%
    stats = get_stats(conn, player_id) # fetches profile stats

    pot_odds = (to_call)/(pot + to_call) # calculates minimum equity needed to justify calling

    if stats[5] < 10: # if we havent really profiled our players go based of math
        if pot_odds < equity:
            actions = "Call"
            return
        elif pot_odds > equity:
            actions = "Fold"
            return
        
    elif stats[5] > 10: # as accurate stats come in go based off stats

        if stats[3] == "Rock": #checks if player is a Rock
            if(to_call < pot * (0.3)): #checks if it is a small bet
                threshold = pot_odds * 0.7 #if it is small bet lowers the threshold 
                if(equity < threshold): # if the W% is still not good then fold
                    return ('Fold',0, f" Since equity { equity: .0%} vs threshold {threshold: .0%}, then we fold because they dont Bluff")
                
                else: # if it is good enough then raise to steal their blind
                    if(community_cards == []):#check if its in preflop and decide
                        return ('Raise',0,f"Since equity { equity: .0%} vs threshold {threshold: .0%}, then we steal their call because they over-fold")
                    else:
                        return ('Call',0, f" Since equity { equity: .0%} vs threshold {threshold: .0%}, we play safe and call, because our hand is still good.")
                    
            elif (to_call > pot * (0.6)): # large == becareful only go with very good hand
                threshold = pot_odds * 1.4 #if it is a big bet increase the bar required to bet
                if(equity > threshold): # if the W% is good enough then we call them
                    return ('Call',0, f"Since equity {equity: .0%} vs threshold {threshold: .0%}, we play safe and call since they probably have a monster too")
                
                else: # if its not the we run away
                    return('Fold',0,f"Since equity {equity: .0%} vs threshold {threshold: .0%}, we play fold because they probably have a better hand than us, and dont bluff")
                
        elif stats[3] == "TAG": #checks if player is a Tight Aggresive
            return
        elif stats[3] == "LAG": #checks if player is a Loose Aggresive
            return
        elif stats[3] == "Calling Station": #checks if player is a Calling Station
            return
        elif stats[3] == "Maniac": #checks if player is an extreme LAG
            return
        elif stats[3] == "Fish": #checks if player is a Fish
            return
        
    return