# This file is the "table" — it wraps rlcard so we don't have to
# deal with the annoying rules stuff ourselves (side pots, all-ins, etc.).
# RLCard already handles all of that; our job here is just to plug
# our bot and our observer into its loop.
#
# What needs to happen here:
#   - set up the rlcard Texas Hold'em environment
#   - on each step, pass the game state to bot/decision.py to get an action
#   - also pass every opponent action to bot/observer.py so it gets logged
#   - return the result of each hand (who won, pot size) back to main.py
#
# Think of this file as the glue between rlcard (the borrowed table)
# and our own code (the brain). It shouldn't make any decisions itself.
