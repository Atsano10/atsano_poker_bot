##
# ARCHETYPES
# 1. Aggressor: Raises pre flop, enters many hands, call to fold ratio would be high
# 2. Calling station # highest amount of hands, re raises on safe hands onnly otherwise call, low post flop aggression
# 3. Rock (only plays safe hands) low call to fold ratio plays only premiums, not alot of hands
# 4. Big better like aggressor but higher pot size
# 5. Shark (re raises you after he checked initially) most balanced player check raise will be high
# ##
from db.database import get_stats, update_stats, get_player_actions

def update_profile(conn, player):
    return