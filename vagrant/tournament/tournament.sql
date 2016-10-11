-- The following is where the initial database will be created for the rest of the project

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE Tournament;
\c tournament

-- The following is the table is where the name will be stored and associated with an id

CREATE TABLE Players(id SERIAL PRIMARY KEY,
                      name TEXT);

-- The following is the table is where the players wins and loses will be stored
CREATE TABLE Matches(id SERIAL PRIMARY KEY,
                      winner INT REFERENCES Players(id),
                      loser INT REFERENCES Players(id));
