# The visual demo — run this with: streamlit run app/streamlit_app.py
# This is what you show recruiters so they can see the bot in action
# without reading any code.
#
# What it should display:
#   - a live hand: hole cards, community cards, pot size, whose turn it is
#   - the bot's decision with its reasoning ("equity 58% > 21% needed, raise")
#   - a sidebar or table showing each opponent's profile:
#       name | archetype | VPIP | aggression | hands seen
#   - a running chip count chart so you can see the bot winning over time
#
# Streamlit makes this surprisingly easy — you mostly just call st.write(),
# st.table(), and st.line_chart() and it handles the layout.
# Pull data from the DB using the functions in db/database.py.
#
# Nice-to-have later: a "play one hand" button that steps through a hand
# one action at a time so you can watch the reasoning update live.
