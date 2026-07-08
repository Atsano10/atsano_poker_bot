import rlcard 
from bot.decision import decide
from bot.profiler import update_profile
from bot.observer import log_action

def game(conn, num_opponents, hand_id): # function that takes in connection, num_opponents, hand_id
    env = rlcard.make('no-limit-holdem') #creates a no-limit Texas Hold'em table
    state,player_id = env.reset() # split env.reset() in order to know the current game state to make a decision on how to move on.

    while(env.is_over() != True): #while the game state is not done keep looping
        raw = state['raw_obs'] #save raw for convenience
        pocket_cards = raw['hand'] #extract hand from raw
        community_cards = raw['public_cards'] #extract community_cards from raw
        pot = raw['pot'] #extract pot from raw
        to_call = max(raw['all_chips']) - raw['my_chips'] #calculate amount needed to call
        street = str(raw['stage']) #extract street from raw

        actions_str,amount,reason = decide(pocket_cards, community_cards, pot, to_call, player_id, num_opponents, conn) # split decision for convenience
        actions = {"Fold": 0, "Check": 1, "Call": 1, "Raise": 2} # dictionary to convert str -> int for usage

        state,player_id = env.step(actions[actions_str]) #pass the integer value to acknowledge action
        log_action(conn, hand_id, player_id, street, actions_str,pot, amount) #log the actions

    payoffs = env.get_payoffs() # stores what each players profit was in the hand
    pot_size = sum([abs(x) for x in payoffs]) #sum the abs of each players profit

    update_profile(conn, player_id) #update the profile to create archetype

    return payoffs.index(max(payoffs)), pot_size 
