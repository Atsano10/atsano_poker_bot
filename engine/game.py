import rlcard
import numpy as np
from bot.decision import decide
from bot.profiler import update_profile
from bot.observer import log_action

BOT = 0 #our bot is always player 0
OPPONENT = 1 #opponent is always player 1

def game(conn, hand_id): #takes in connection and hand_id, heads-up only now
    env = rlcard.make('no-limit-holdem', config={'game_num_players': 2}) #creates a heads-up no-limit holdem table
    state,player_id = env.reset() # split env.reset() to know whos turn it is

    while not env.is_over(): #keep looping until the hand is over
        raw = state['raw_obs'] #save raw for convenience
        pocket_cards = raw['hand'] #extract hand from raw
        community_cards = raw['public_cards'] #extract community cards from raw
        pot = raw['pot'] #extract pot from raw
        to_call = max(raw['all_chips']) - raw['my_chips'] #calculate amount needed to call
        street = str(raw['stage']) #extract street from raw

        if player_id == BOT: #our turn, make a smart decision
            action_str,amount,reason = decide(pocket_cards, community_cards, pot, to_call, player_id, conn)
            action_int = {"Fold": 0, "Check": 1, "Call": 1, "Raise": 2}[action_str]
        else: #opponents turn, pick a random legal action
            legal_actions = list(state['legal_actions'].keys())
            action_int = int(np.random.choice(legal_actions))
            action_str = {0: "Fold", 1: "Call", 2: "Raise"}.get(action_int, "Call")
            amount = 0

        log_action(conn, hand_id, player_id, street, action_str, pot, amount) #log the action for both players
        state,player_id = env.step(action_int) #step the environment forward

    payoffs = env.get_payoffs() #stores what each players profit was in the hand
    pot_size = sum([abs(x) for x in payoffs]) #sum the abs of each players profit

    update_profile(conn, OPPONENT) #only profile the opponent not ourselves

    return int(np.argmax(payoffs)), pot_size
