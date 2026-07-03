# The observer watches what opponents do and writes it all to the database.
# It doesn't make any decisions — it just pays attention and takes notes.
#
# Every time an opponent acts (folds, calls, raises, and how much),
# this file should log that action to the actions table via db/database.py.
# That raw history is what the profiler later turns into a player profile.
#
# The key info to capture per action:
#   - which player
#   - what street (preflop, flop, turn, river)
#   - what they did (fold / call / raise)
#   - how much they put in
#
# engine/game.py will call into this file after each opponent move,
# so the interface should be simple — probably just one function:
#   log_action(conn, hand_id, player, street, action, amount)
