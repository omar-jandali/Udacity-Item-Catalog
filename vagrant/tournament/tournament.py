import psycopg2

#The following function is where the initial database connection will be made
def connect(database_name="tournament"):
    try:
        connection = psycopg2.connect("dbname={database_name}")
        cursor = connection.cursor()
        return connection, cursor
    except:
        print("<error message>")

# the following function is where all of the
#   connections will be made
#   query will be executed
#   changes will be commited
#   and database connection will be closed
def execute(query):
    connection = connect()
    cursor = connect()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.commit()
    connection.close
    return results

#this functions will be used for deleting records, when deleting records,
#   there are no results that are passed
def execute_delete(query):
    connection = connect()
    cursor = connect()
    cursor.execute(query)
    connection.commit()
    connection.close()

def execute_default(query):
    connection = connect()
    cursor = connect()
    cursor.execute(query)
    results = cursor.fetchone()[0]
    connection.commit()
    connection.close()
    return results


#the following function is used to set the default values for the players records at the beginning of the game_count
def default_table():
    execute("UPDATE Matches SET wins")

#the following function will be used to delete all of the current matches
def deleteMatches():
    execute_delete("DELETE FROM Matches Returning *")

# the following function will be used to delete all of the players from the database
def deletePlayers():
    execute_delete("DELETE FROM players RETURNING *")

# the following will count and return how many players are registered
def countPlayers():
    execute_default("SELECT count(*) FROM Players")

# the following function will be called when a new player is being registered for the
#   tournament
#
#   Arguments = name as users name
def registerPlayer(name):
    execute_default("INSERT INTO Players VALUES ('%s')", (name,))

# the following fucntion will return a list of the players records in order of wins
#
# arguments:
#   id: players id
#   name: players name
#   wins: players wins
#   matches: the total number of matches for the player
def playerStandings():
    execute("""SELECT Players.id, Players.name, Records.wins, Matches
            FROM Players LEFT JOIN Records ON Players.id = Records.id
                LEFT JOIN Matches ON Players.id = Matches.id
            ORDER BY wins """)

# the following functino will save eatch matchs winer and looser between the two players
#
# argunments:
#   winner: the player id that won
#   loser: the player id that lost
def reportMatch(winner, loser):
    execute("INSERT INTO Matches (winners, losers) VALUES (%s, %s)", (winner,
                                                                      loser,))
    execute("UPDATE Records SET wins += 1 WHERE id = %s", (winner,))
    execute("UPDATE Records SET losses += 1 WHERE id = %s", (loser,))

# the following function is what will decide the pairing of the the two players
#   of each match
# in the tournament based on the swiss pairing Swiss-system
#
# arguments:
#   first players id
#   first players name
#   second players id
#   second players name
#
#   This function will go though the standing and match the top two players
#    together, then move to the
#   folowing two and match them. this will keep happening until all the
#    players are matched
def swissPairings():
    next_round = []
    standings = playerStandings()
    for i in range(0, len(standings), 2):
        next_round.append((standings[i][0],
                            standings[i][1],
                            standings[i+1][0],
                            standings[i+1][1]))
    return next_round
