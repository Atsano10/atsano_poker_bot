# Tests for bot/equity.py
#
# The main thing to verify: pocket aces (As Ah) against one random opponent
# preflop should win roughly 85% of the time. That's a known correct answer,
# so if our simulation spits out something wildly different, the code is broken.
#
# Other good cases to test:
#   - two pair on a paired board (should have decent equity)
#   - a busted flush draw on the river (equity = 0, we already lost)
#   - heads-up vs 3 opponents (equity should drop as more players are added)
#
# These tests don't need to be exact — Monte Carlo has variance — so check
# that the result lands within a reasonable range (e.g. 0.82 to 0.88 for aces).
