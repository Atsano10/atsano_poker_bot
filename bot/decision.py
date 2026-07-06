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
        if stats[3] == "Rock":
            return
        elif stats[3] == "TAG":
            return
        elif stats[3] == "LAG":
            return
        elif stats[3] == "Calling Station":
            return
        elif stats[3] == "Maniac":
            return
        elif stats[3] == "Fish":
            return
        
    return