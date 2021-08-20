import sqlalchemy
import pandas as pd

db = 'postgresql://postgres@localhost:5432/netology'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# genres = [(1,'pop'),(2,'rock'),(3,'jazz'),(4,'hiphop'),(5,'indie'),(6,'blues')]
# artists = [(3, 'AC/DC'),(4, 'Bon Jovi'),(5, 'Moby'),(6, 'Morgue Vanguard'),(7, 'Da Molotov'),
# (8, 'Океан Эльзы'),(9, 'Eminem')]
# albums = [(1,'Long Ambients 2',2019),(2,'Demi Masa',2018),(3,'Everything Was Beautiful, and Nothing Hurt', 2018),
#           (4,'Kamikaze',2018),(5,'Con Todo Respeto',2004),(6,'Songs of Faith and Devotion',1993),
#           (7,'St. Anger',2003),(8,'Back in Black',1998),(9,'New Jersey',1988)]
# track = [
# (1,'LA12',2820,1),
# (2,'LA13',1620,1),
# (3,'LA14',2340,1),
# (4,'LA15',1920,1),
# (5,'LA16',1800,1),
# (6,'LA17',2520,1),
# (7,'Junta Titimangsa',139,2),
# (8,'Breakadawn',275,2),
# (9,'CSDB FM feat. Iwa K',351,2),
# (10,'Testamen',297,2),
# (11,'Buckshot Funk feat. Mr.EP & Sarkasz',137,2),
# (12,'Rotasi Baja (Interlude)',58,2),
# (13,'Di Hadapan Babylon',266,2),
# (14,'Check Your People',287,2),
# (15,'Demi Masa',187,2),
# (16,'Sans Temps Mort',141,2),
# (17,'Testamen [Novum Testamentum]',265,2),
# (18,'Check Your People (Remix)',247,2),
# (19,'Frantic',350,7),
# (20,'St. Anger',441,7),
# (21,'Some Kind of Monster',505,7),
# (22,'Dirty Window',325,7),
# (23,'Invisible Kid',510,7),
# (24,'My World',346,7),
# (25,'Shoot Me Again',430,7),
# (26,'Sweet Amber',327,7),
# (27,'The Unnamed Feeling',428,7),
# (28,'Purify',314,7),
# (29,'All Within My Hands',528,7),
# (30,'Lay Your Hands on Me',358,9),
# (31,'Bad Medicine',316,9),
# (32,'Born to Be My Baby',280,9),
# (33,'Living in Sin',279,9),
# (34,'Blood on Blood',376,9),
# (35,'Homebound Train',310,9),
# (36,'Wild Is the Wind',308,9),
# (37,'Ride Cowboy Ride',85,9),
# (38,'Stick to Your Guns',285,9),
# (39,'Ill Be There for You',346,9),
# (40,'99 in the Shade',269,9),
# (41,'Love for Sale',138,9),
# (42,'Mere Anarchy',315,3),
# (43,'Like a Motherless Child',277,3),
# (44,'The Last of Goodbyes',263,3),
# (45,'The Ceremony of Innocence',136,3),
# (46,'The Tired and the Hurt',268,3),
# (47,'Welcome to Hard Times',308,3),
# (48,'The Sorrow Tree',268,3),
# (49,'Falling Rain and Light',286,3),
# (50,'The Middle Is Gone',313,3),
# (51,'This Wild Darkness',249,3),
# (52,'A Dark Cloud Is Coming',324,3)
# ]

# genre_artist = [(1, 1, 1),(2, 1, 2),(3, 2, 2),(4, 3, 2),(5, 4, 2),(6, 5, 1),(7, 5, 2),(8, 6, 1),(9, 6 ,4)]
# artist_album = [(1, 5, 1),(2,	6, 2),(3, 5, 3),(4,	9, 4),(5, 7, 5),]

# for elm in artists:
#      ins = connection.execute(f"INSERT into artist VALUES ({elm[0]},'{elm[1]}');")

# for elm in genres:
#     ins = connection.execute(f"INSERT into genre VALUES ({elm[0]},'{elm[1]}');")

# for elm in albums:
#     ins = connection.execute(f"INSERT into album VALUES ({elm[0]},'{elm[1]}',{elm[2]});")
# for elm in track:
#     ins = connection.execute(f"INSERT into track VALUES ({elm[0]},'{elm[1]}',{elm[2]},{elm[3]});")

# for elm in genre_artist:
#     ins = connection.execute(f"INSERT into genreartist VALUES ({elm[0]},{elm[1]},{elm[2]});")

# for elm in artist_album:
#     ins = connection.execute(f"INSERT into artistalbum VALUES ({elm[0]},{elm[1]},{elm[2]});")

release_date_2018 = connection.execute("SELECT title, release_date from album WHERE release_date = 2018;").fetchall()
print(pd.DataFrame(release_date_2018))
print()
longest_track = connection.execute("SELECT title, duration from track ORDER BY duration DESC LiMIT 1;").fetchall()
print(longest_track)
print()
duration_3_5_min = connection.execute("SELECT title, duration from track WHERE duration > 210 "
                                      "ORDER BY duration DESC;").fetchall()
print(pd.DataFrame(duration_3_5_min))
print()
artist_name_1 = connection.execute("SELECT name from artist WHERE name NOT LIKE '%% %%';").fetchall()
print(artist_name_1)
print()
my_track = connection.execute("SELECT title from track WHERE title LIKE '%%My%%' OR title LIKE '%%my%%' "
                              "OR title LIKE '%%мой%%' OR title LIKE '%%Мой%%';").fetchall()
print(my_track)
