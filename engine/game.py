import rlcard 

def game(conn, num_opponents):
    env = rlcard.make('no-limit-holdem') #creates a no-limit Texas Hold'em table
    env.reset() #starts a new hand, deals card

    while(env.is_over() != True): #keeps playing until the hand is finished
        env.step(1) #makes a decision

    payoffs = env.get_payoffs() #saves the payouts in a list

    pot_size = sum([abs(x) for x in payoffs]) #for every value in list add the abs value of it

    return payoffs.index(max(payoffs)), pot_size #return the winner and the potsize

#FUTURE STEPS
# make an actual decision
# pass states and actions for stats