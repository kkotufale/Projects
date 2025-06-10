### S12_PySQL_StarterFile.py  v4
#  K.Schmitz (c) 2022,2023, 2024
#  Starter File for CIS2010 Session 12, Structured Query Language
##################Initialization information, do not modify ################
from cis2010utils4 import StartHere, EndHere, runsql
##from colorama import Fore
import pandas as pd
import sqlite3
############################################################################
#
# Task 2a
StartHere( "Kike Otufale", "S12w", "Spring 2025")
#
#
# Open up the database  ########## Do not modify these instructions#########
db_name =  "Movies2023x4.db"
db_conn = sqlite3.connect(db_name)
sqltxt = "pragma table_info('movies')" ; t1 = pd.read_sql(sqltxt, db_conn) ; print("movies table\n", t1)
sqltxt = "pragma table_info('crew')" ; t2 = pd.read_sql(sqltxt, db_conn) ; print("crew table\n", t2)
sqltxt = "pragma table_info('lang')" ; t3 = pd.read_sql(sqltxt, db_conn) ; print("lang table\n", t3)
sqltxt = "pragma table_info('genre')" ; t4 = pd.read_sql(sqltxt, db_conn) ; print("genre table\n", t4)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
############################################################################
#
#
# Task w3a
sqlw3a = """
SELECT year FROM movies 
"""
w3a = runsql( sqlw3a, db_conn, False)

#
# Task w3c
sqlw3c = """
SELECT DISTINCT year FROM movies 
"""
w3c = runsql( sqlw3c, db_conn, False)

#
# Task w4a
sqlw4a = """
SELECT year, title, revenue
FROM movies
WHERE title = 'Barbie'
"""
w4a = runsql( sqlw4a, db_conn, True)

#
# Task w4b
sqlw4b = """
SELECT year, title, revenue
FROM movies
WHERE title LIKE '%Barbie%'
"""
w4b = runsql( sqlw4b, db_conn, True)

#
# Task w4c
sqlw4c = """
SELECT year, title, revenue
FROM movies
WHERE title LIKE '%indiana jones%'
ORDER BY revenue
"""
w4c = runsql( sqlw4c, db_conn, True)

#
# Task w5a  
sqlw5a = """
SELECT year, title, actor
FROM movies
WHERE title LIKE '%indiana jones%'
ORDER BY revenue
"""
#w5a = runsql( sqlw5a, db_conn, False)

#
# Task w5b
sqlw5b = """
SELECT * FROM crew
"""
w5b = runsql( sqlw5b, db_conn, False)

# Task w5c
sqlw5c = """
SELECT year, title, actor
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE title LIKE '%indiana jones%'
"""
w5c = runsql( sqlw5c, db_conn, False)

# Task w5d
sqlw5d = """
SELECT year, title, actor
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE title LIKE '%indiana jones%' AND actor = 'John Rhys-Davies'
"""
w5d = runsql( sqlw5d, db_conn, True)
#AND actor LIKE '%Banderas%'

#
# Task w6a
sqlw6a = """
SELECT year, title, actor, MAX(REVENUE)
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE actor = 'Zoe Saldana'
"""
w6a = runsql( sqlw6a, db_conn, True)

#
# Task w6b
sqlw6b = """
SELECT actor, SUM(REVENUE)
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE actor = 'Zoe Saldana'
"""
w6b = runsql( sqlw6b, db_conn, True)

#
# Task w7a
sqlw7a = """
SELECT DISTINCT genre
FROM movies JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE '%Avatar%'
"""
w7a = runsql( sqlw7a, db_conn, False)

#
# Task w7c
sqlw7c = """
SELECT g.title, g.genre
FROM genre g
JOIN movies m ON g.title = m.title
WHERE m.title LIKE '%Indiana Jones%';
"""
w7c = runsql( sqlw7c, db_conn, False)


# Workshop END
#
###########################################################
# Collaboration Challenge
pd.set_option('display.max_rows', 32)
#
# S12ccq Q4
StartHere( "Kike Otufale", "S12wcc", "Spring 2025")

#
# S12ccq Q5
sqlcc5 = """
SELECT title, COUNT(title)
FROM movies
WHERE title LIKE 'Frozen%'
"""
cc5 = runsql( sqlcc5, db_conn, False)

#
# S12ccq Q6
sqlcc6 = """
SELECT title, COUNT(title)
FROM movies
WHERE budget > 100000000 AND title LIKE 'Frozen%'
"""
cc6 = runsql( sqlcc6, db_conn, False)

#
# S12ccq Q7
sqlcc7 = """
SELECT title, actor
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE actor = 'Idina Menzel' AND title LIKE 'Frozen%'
"""
cc7 = runsql( sqlcc7, db_conn, False)

#
# S12ccq Q8
sqlcc8 = """
SELECT g.title, g.genre
FROM genre g
JOIN movies m ON g.title = m.title
WHERE m.title LIKE 'Frozen%';
"""
cc8 = runsql( sqlcc8, db_conn, False)

#
# S12ccq Q9
sqlcc9 = """
SELECT title, COUNT(title)
FROM movies
WHERE title LIKE '%Spider%'
"""
cc9 = runsql( sqlcc9, db_conn, False)

#
# S12ccq Q10
sqlcc10 = """
SELECT title, actor, year
FROM movies JOIN crew ON movies.mid = crew.movieID
WHERE title LIKE '%Spider%' AND year = 2002

"""
cc10 = runsql( sqlcc10, db_conn, False)

#
# S12ccq Q11
sqlcc11 = """
SELECT movies.year, movies.title, genre.genre
FROM movies
JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE '%Black Panther%' 
"""
cc11 = runsql( sqlcc11, db_conn, False)

#
# S12ccq Q12
sqlcc12 = """
SELECT movies.title, genre.genre
FROM movies JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE '%Shrek%'
"""
cc12 = runsql( sqlcc12, db_conn, False)

#
# S12ccq Q13
sqlcc13 = """
SELECT title, year
FROM movies
WHERE title LIKE '%Shrek%'
"""
cc13 = runsql( sqlcc13, db_conn, False)


#Collaboration Challenge End
###########################################################
# Individual Challenge
#
# S12ccq Q1
StartHere( "Kike Otufale", "S12wccic", "Spring 2025")

#
# S12icq Q2
sqlic2 = """
SELECT * FROM lang
"""
ic2 = runsql( sqlic2, db_conn, False)

#
# S12icq Q3
sqlic3 = """
SELECT orig_lang
FROM movies
JOIN lang ON movies.mid = lang.mid
WHERE title LIKE '%The Pope: Answers%' 
"""
ic3 = runsql( sqlic3, db_conn, False)

#
# S12icq Q4
sqlic4 = """
SELECT title, actor, MAX(budget)
FROM movies
JOIN crew on movies.mid = crew.movieID
WHERE actor = 'Whoopi Goldberg'
"""
ic4 = runsql( sqlic4, db_conn, False)

#
# S12icq Q5
sqlic5 = """
SELECT title, year
FROM movies
WHERE title = 'Titanic'
"""
ic5 = runsql( sqlic5, db_conn, False)

#
# S12icq Q6
sqlic6 = """
SELECT title, country
FROM movies
JOIN lang ON movies.mid = lang.mid
WHERE title = 'Mafia Mamma'
"""
ic6 = runsql( sqlic6, db_conn, False)

#
# S12icq Q7
sqlic7 = """
SELECT movies.title, movies.year, genre.genre
FROM movies
JOIN genre ON movies.title = genre.title
WHERE movies.title = 'Luca'
"""
ic7 = runsql( sqlic7, db_conn, False)


###########################################################
#
#Individual Challenge: End
db_conn.close()
EndHere(globals())
#exit();
############################################################
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
 #Atr`$>-LPNPJ%TYZKFQJ%4ZXJWX4PNPJTYZKFQJlSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$>-LPNPJ%TYZKFQJ%4ZXJWX4PNPJTYZKFQJlSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
