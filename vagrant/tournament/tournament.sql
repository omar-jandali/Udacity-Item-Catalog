-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--------------------------------------------------------------------------------

-- the following will clear all of the databases if they already exists
drop database if exists tournament;

-- the is the creation of the entire tournaments database
create database tournament;

-- the following are a list of tables that are going to be used in this project

-- this table will store all of the players in the tournament
create table players(
  id serial primary key,
  name text
);

create table records(
  id int references players(id),
  wins int,
  loses int
)

create table matches(
  rotation serial primary key,
  player_1 int references player(id),
  player_2 int references player(id)
)

create view standings as
  select players.id, records.wins, records.loses
    from players and records
    order by records.wins and players.id asc