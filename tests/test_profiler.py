# Tests for bot/profiler.py
#
# The goal: make sure the profiler correctly identifies player types
# from their action history. Two clear cases to start with:
#
#   1. A "bluffer/maniac" — feed in a history where the player raises constantly,
#      rarely folds, and puts in big amounts. The profiler should label them
#      as 'bluffer' or 'maniac', not 'nit'.
#
#   2. A "nit/rock" — a history of mostly folds, rarely entering a pot,
#      and small bet sizes when they do. Should come out labeled 'nit'.
#
# To keep tests self-contained, use an in-memory SQLite database (:memory:)
# instead of the real poker.db file, and insert fake action rows directly.
# That way the tests don't depend on any saved game data to pass.
