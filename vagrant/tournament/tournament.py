#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

#The following function is where the initial database connection will be made
def connect():
    return psycopg2.connect("dbname=tournament")

# the following function is where all of the
#   connections will be made
#   query will be executed
#   changes will be commited
#   and database connection will be closed
def execute(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.commit()
    connection.close

    return results

#the following function is used to set the default values for the players records at the beginning of the game_count
def default_table():
    execute("UPDATE Matches SET wins")

#the following function will be used to delete all of the current matches
def deleteMatches():
    execute("UPDATE record SET wins=0, losses=0")

    execute("DELETE FROM Matches")

# the following function will be used to delete all of the players from the database
def deletePlayers():
    execute("DELETE FROM players")

# the following will count and return how many players are registered
def countPlayers():
    execute("SELECT count(id) FROM Players")

# the following function will be called when a new player is being registered for the
#   tournament
#
#   Arguments = name as users name
def registerPlayer(name):
    execute("INSERT INTO Players VALUES ('%s')", (name,))

# the following fucntion will return a list of the players records in order of wins
#
# arguments:
#   id: players id
#   name: players name
#   wins: players wins
#   matches: the total number of matches for the player
def playerStandings():
    execute("""SELECT Players.id, Players.name, Records.wins, Matches.player_id, Matches.winner, Matches.loser
            FROM Players LEFT JOIN records ON Players.id = Records.id
                LEFT JOIN Matches ON Players.id = Matches.player_id
            ORDER BY wins """)

# the following functino will save eatch matchs winer and looser between the two players
#
# argunments:
#   winner: the player id that won
#   loser: the player id that lost
def reportMatch(winner, loser):
    execute("INSERT INTO Matches (winners, losers) VALUES (%s, %s)", (winner,loser,))
    execute("UPDATE Records SET wins += 1 WHERE id = %s", (winner,))
    execute("UPDATE Records SET losses += 1 WHERE id = %s", (loser,))

# the following function is what will decide the pairing of the the two players of each match
# in the tournament based on the swiss pairing Swiss-system
#
# arguments:
#   first players id
#   first players name
#   second players id
#   second players name
#
#   This function will go though the standing and match the top two players together, then move to the
#   folowing two and match them. this will keep happening until all the players are matched
def swissPairings():
    matchups = []
    players = playerStandings()
    matchups.append(
            for i in range(0, len(players)):
                if players[i] % 1 = 0:
                    players[i][0]
                elif players[i] % 1 = 1:
                    players[i][1]
        )

    return matchups
