CREATE TABLE IF NOT EXISTS sessions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_time INTEGER
);

CREATE TABLE IF NOT EXISTS hands(
    hand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
    pot_size INTEGER,
    num_players INTEGER,
    outcome INTEGER,
    winner_id INTEGER,
    position INTEGER
);

CREATE TABLE IF NOT EXISTS decision(
    decision_id INTEGER PRIMARY KEY AUTOINCREMENT,
    actions TEXT,
    player_id INTEGER,
    hand_id INTEGER,
    street TEXT,
    pot_size INTEGER
);

CREATE TABLE IF NOT EXISTS stats(
    stats_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER,
    aggression REAL,
    playstyle TEXT,
    vpip REAL,
    hands_played INTEGER
);