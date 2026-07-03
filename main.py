# This is the starting point — run this file to kick off a session.
# It should set up the database, create a game, and loop through hands
# until the session is done. Think of it as the "director" that tells
# all the other pieces when to do their thing.
#
# Rough flow:
#   1. connect to the DB (db/database.py handles that)
#   2. spin up a game session (engine/game.py)
#   3. run N hands in a loop
#   4. after each hand, trigger the profiler to update opponent stats
#   5. print a small summary at the end (chips won/lost, who was at the table)
#
# Keep this file short — if logic starts piling up here, it probably
# belongs in one of the bot/ or engine/ files instead.
