# Future
# account for all players not only one

from equity import estimate_equity
from db.database import get_stats

def decide(pocket_cards, community_cards, pot, to_call, player_id, num_opponents, conn):
    simulations = 500 #hardcoded sims

    equity = estimate_equity(pocket_cards, community_cards, num_opponents, simulations)
    stats = get_stats(conn, player_id)

    # If no one has bet first.
    if to_call == 0:
        if equity > 0.65:
            return ('Raise', 0, f"Since equity {equity:.0%} is strong and it's free to act, we bet for value.")
        return ('Check', 0, f"Since equity {equity:.0%} isn't strong enough to bet, we check.")

    pot_odds = to_call / (pot + to_call)

    #If we havent gotten enough data yet
    if stats[5] < 10:
        if pot_odds < equity:
            return ('Call', 0, "just call based on odds")
        else:
            return ('Fold', 0, "just fold based on odds")

    # We have crafted data on people and can decide based on that
    elif stats[5] >= 10:

        # If opponenent is a Rock
        if stats[3] == "Rock":
            if to_call < pot * 0.3: # small bet size
                threshold = pot_odds * 0.7
                if equity < threshold:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, we fold because they dont bluff.")
                else:
                    if community_cards == []: # if in pre-flop
                        return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, we steal their call because they over-fold.")
                    else:
                        return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, we play safe and call, hand is still good.")

            elif to_call > pot * 0.6: # large bet size
                threshold = pot_odds * 1.4
                if equity > threshold:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, we call since they probably have a monster too.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, we fold because they probably have a better hand and dont bluff.")

            else:  # medium bet 30-60%
                threshold = pot_odds * 1.1
                if equity > threshold:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, medium bet from Rock is likely value — call cautiously.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, medium bet from Rock signals strength — fold.")

        # If opponenent is a TAG
        elif stats[3] == "TAG":
            if to_call < pot * 0.3:
                threshold = pot_odds * 0.85
                if equity < threshold:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, might be bluffing but better to be safe and fold.")
                else:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, we call because it might be a bluff and we have a good hand.")

            elif to_call > pot * 0.6:
                threshold = pot_odds * 1.5
                if equity > threshold:
                    return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, we have a really good hand so we raise because they might be bluffing.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, probably not a bluff so might as well fold.")

            else:  # medium bet 30-60%
                threshold = pot_odds * 1.15
                if equity > threshold:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, TAG medium bet is value — call if hand is solid.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, TAG medium bet signals strength — fold.")

        # If opponenent is a LAG
        elif stats[3] == "LAG":
            if to_call < pot * 0.2:
                threshold = pot_odds * 0.65
                if equity < threshold:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, have to be careful of good hands, fold.")
                else:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, let them bluff their way into a hole, call.")

            elif to_call > pot * 0.5:
                threshold = pot_odds * 0.75
                if equity > threshold:
                    return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, we have a really good hand so we raise to take the pot.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, might be a bluff but safer to just fold.")

            else:  # medium bet 20-50%
                threshold = pot_odds * 0.9
                if equity > threshold:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, LAG likely bluffing on medium bet — call.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, even for a LAG this medium bet could be real — fold.")

        # If opponenent is a Calling Station
        elif stats[3] == "Calling Station":
            if to_call < pot * 0.2:
                threshold = pot_odds * 0.55
                if equity < threshold:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, fold, as they might call or raise either way.")
                else:
                    return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, raise to get money out of their relentless calls.")

            elif to_call > pot * 0.55:
                threshold = pot_odds * 0.70
                if equity > threshold:
                    return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, drain them with their own calls, raise.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, just fold because they will call either way.")

            else:  # medium bet 20-55%
                threshold = pot_odds * 0.60
                if equity > threshold:
                    return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, Calling Station will call our raise — value bet.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, not enough equity to raise a Calling Station — fold.")

        # If opponenent is a Maniac
        elif stats[3] == "Maniac":
            if to_call < pot * 0.3:
                threshold = pot_odds * 0.35
                if equity < threshold:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, just fold because we dont know what they could have.")
                else:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, call and let them raise the pot themselves.")

            elif to_call > pot * 0.6:
                threshold = pot_odds * 0.60
                if equity > threshold:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, lure them in by calling.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, just fold because we dont know what they could have.")

            else:  # medium bet 30-60%
                threshold = pot_odds * 0.50
                if equity > threshold:
                    return ('Call', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, Maniac probably bluffing medium too — call.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, not enough equity even accounting for Maniac bluffs — fold.")

        # If opponenent is a Fish
        elif stats[3] == "Fish":
            if to_call < pot * 0.3:
                threshold = pot_odds * 0.55
                if equity < threshold:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, just fold, they probably have something if they bet.")
                else:
                    return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, scare them when you have something and raise.")

            elif to_call > pot * 0.6:
                threshold = pot_odds * 0.70
                if equity > threshold:
                    return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, raise them and make them scared.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, just fold, they probably have at least a hit.")

            else:  # medium bet 30-60%
                threshold = pot_odds * 0.65
                if equity > threshold:
                    return ('Raise', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, Fish medium bet is likely weak — raise to scare them off.")
                else:
                    return ('Fold', 0, f"Since equity {equity:.0%} vs threshold {threshold:.0%}, Fish hit something on medium bet — fold.")

    # safety net
    return ('Fold', 0, "No rule matched — defaulting to fold")
