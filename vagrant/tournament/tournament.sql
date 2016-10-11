-- The following is where the initial database will be created for the rest of the project

CREATE DATABASE Tournament

-- The following is the table is where the name will be stored and associated with an id

CREATE TABLE Players(id SERIAL PRIMARY KEY,
                      name TEXT)

CREATE TABLE Records(id SERIAL REFERENCES Players(id),
                      wins INTEGER,
                      losses INTEGER)

-- The following is the table is where the players wins and loses will be stored
CREATE TABLE Matches(id SERIAL PRIMARY KEY,
                      player_id INT SERIAL REFERENCES Players(id),
                      winner INT SERIAL REFERENCES Players(id),
                      loser INT SERIAL REFERENCES Players(id))
