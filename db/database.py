# Everything that touches the database lives here.
# Other files should never write SQL directly — they call these functions instead.
#
# Functions to build out:
#   connect()                    -> opens (or creates) poker.db, runs schema.sql
#   create_session(conn)         -> inserts a new session row, returns its id
#   create_hand(conn, ...)       -> inserts a new hand row, returns its id
#   insert_action(conn, ...)     -> logs one opponent action to the actions table
#   get_stats(conn, player)      -> returns the player_stats row for one player
#   update_stats(conn, player, vpip, aggression, archetype)  -> upserts their profile
#   all_player_stats(conn)       -> returns all player profiles (used by streamlit)
#
# SQLite is built into Python (import sqlite3), so no install needed.
# The DB file is poker.db in the project root — it's gitignored so it
# doesn't clutter the repo, but it persists between runs so the bot
# remembers opponents across sessions.
