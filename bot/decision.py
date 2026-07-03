# This is where the bot actually decides what to do: fold, call, or raise.
# It combines three things:
#   1. our equity (from equity.py) — how likely we are to win
#   2. pot odds — the minimum equity we need to justify calling
#   3. the opponent's archetype (from the DB) — who we're up against
#
# The baseline logic is: if equity > pot odds needed, call or raise.
# The adaptive layer adjusts that based on who's sitting across from us:
#
#   vs bluffer/maniac  -> lower our threshold to call, don't get pushed off
#   vs big bettor      -> trap with strong hands, fold marginal ones to pressure
#   vs calling station -> never bluff, only bet strong hands for value
#   vs nit/rock        -> steal their blinds often, fold the second they raise back
#
# The function signature should be something like:
#   decide(hole_cards, community_cards, pot, to_call, opponent, conn)
#   -> returns ('fold'|'call'|'raise', amount, reason_string)
#
# The reason_string matters — printing "equity 62% > 25% needed, raising"
# is what makes the bot explainable, which is the whole resume story.
