# 1. Connect to DB, create session
# 2. Loop over hands:
#  - Create hand
#  - Loop over actions (preflop → flop → turn → river):
#      - Make decision
#    - Log action (observer)
#  - Update hand (winner, pot size)
#  - Update profiler for each opponent
# 3. End
