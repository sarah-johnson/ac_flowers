DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS flower_pair;
DROP TABLE IF EXISTS flower_pair_offspring;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  nintendo_id TEXT,
  island_name TEXT
);

CREATE TABLE flower_pair (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  flower_type TEXT NOT NULL,  -- enum with 8 possible values
  creator_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT NOT NULL,
  description TEXT,
  parent1_color TEXT, -- enum
  parent2_color TEXT, -- enum
  FOREIGN KEY (creator_id) REFERENCES user (id)
);

CREATE TABLE flower_pair_offspring (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  flower_pair_id INTEGER,
  FOREIGN KEY (flower_pair_id) REFERENCES flower_pair (id)
);
