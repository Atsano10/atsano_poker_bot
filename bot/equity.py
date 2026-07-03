# Equity = how often our hand wins if we run the rest of the cards out.
# We figure this out the lazy-but-smart way: Monte Carlo simulation.
# Deal random cards to opponents and random community cards thousands of times,
# count how often we win, and that fraction is our equity.
#
# The main function here should look something like:
#   estimate_equity(hole_cards, community_cards, num_opponents, simulations=5000)
#   -> returns a float between 0 and 1 (e.g. 0.85 for pocket aces preflop)
#
# We use treys to evaluate who wins each simulated runout — it's fast
# and handles all the hand-ranking logic so we don't have to.
# numpy helps shuffle and deal cards quickly across thousands of sims.
#
# The sanity check: pocket aces vs one random hand should come out around 85%.
# If it doesn't, something's wrong with the simulation.
