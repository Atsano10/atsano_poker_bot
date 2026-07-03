# The profiler reads the action history from the DB and figures out
# what kind of player each opponent is. This is the "reading people" part.
#
# It computes three numbers per player:
#   - VPIP: how often they voluntarily put money in (high = loose, low = tight)
#   - Aggression factor: raises / (raises + calls) — high means aggressive
#   - Fold-to-bet: how often they fold when someone bets at them
#
# From those numbers it assigns an archetype:
#   "bluffer/maniac"  -> high aggression, bets a lot
#   "big bettor"      -> large bet sizes, high aggression
#   "calling station" -> high VPIP, low aggression, rarely folds
#   "nit/rock"        -> low VPIP, folds a lot
#
# After running, it writes the archetype back to player_stats in the DB
# so decision.py can look it up quickly when it needs to act.
#
# Main function something like:
#   update_profile(conn, player) -> reads actions, computes stats, saves archetype
