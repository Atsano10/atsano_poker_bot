from treys import Card, Deck, Evaluator
import numpy as np


def estimate_equity(pocket_cards, community_cards, num_opponents, simulations):
    wins = 0 # count for our wins
    evaluator = Evaluator() #creates the evaluator

    # runs evaluator a simulations amount of times to get a better approximate helping our decision per board change
    for j in range(simulations):
        won = True
        board = community_cards.copy()

        deck = Deck() #creates the deck    
        deck.cards = [x for x in deck.cards if x not in pocket_cards] #filters out pocket_cards from deck
        deck.cards = [x for x in deck.cards if x not in board] #filters out community_cards from deck

    
        # draws cards for opponents
        opponent_cards = []
        for i in range (num_opponents):
            opponent_cards.append(deck.draw(2))

        # draws cards if the stage requires so
        while len(board) < 5:
            board += deck.draw(1) #draw automatically removes

        # evaluates our hand and remembers score
        my_score = evaluator.evaluate(board,pocket_cards)

        # evaluates opponent hands and checks vs my_score
        for hand in opponent_cards:
            opponent_score = evaluator.evaluate(board,hand)
            if opponent_score < my_score:
                won = False
                break
        
        # gives us a point if we actually beat everyone
        if won == True:
            wins += 1
        
    return wins/simulations
