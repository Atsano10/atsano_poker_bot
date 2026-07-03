-- These are the five tables that form the bot's memory.
-- Run this once to set up the database (database.py handles that on connect).

-- tracks each play session (one session = one run of main.py)

-- tracks individual hands within a session

-- every single action any opponent takes goes here — this is the raw history
-- street is 'preflop', 'flop', 'turn', or 'river'
-- action is 'fold', 'call', or 'raise'

-- one row per opponent, updated after each hand by the profiler
-- vpip, aggression, and archetype are what decision.py reads when it acts
