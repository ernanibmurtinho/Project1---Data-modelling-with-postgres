# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays( 
songplay_id VARCHAR, 
start_time VARCHAR, 
user_id VARCHAR, 
level VARCHAR, 
song_id VARCHAR, 
artist_id VARCHAR, 
session_id VARCHAR, 
location VARCHAR, 
user_agent VARCHAR)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id VARCHAR, 
first_name VARCHAR, 
last_name VARCHAR, 
gender CHAR, 
level VARCHAR
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
song_id VARCHAR, 
title VARCHAR, 
artist_id VARCHAR, 
year VARCHAR, 
duration VARCHAR
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
artist_id VARCHAR, 
artist_name VARCHAR, 
location VARCHAR, 
latitude VARCHAR, 
longitude VARCHAR
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_time BIGINT, 
hour BIGINT, 
day BIGINT, 
week BIGINT, 
month BIGINT, 
year BIGINT, 
weekday BIGINT
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, song_id, artist_id, start_time, user_id, level, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, artist_name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT 
s.song_id, a.artist_id
FROM songs s
INNER JOIN artists a ON s.artist_id = a.artist_id
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]