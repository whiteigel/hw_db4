import sqlalchemy
# import psycopg2

db = 'postgresql://postgres@localhost:5432/netology'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# genres = [(1,'pop'),(2,'rock'),(3,'jazz'),(4,'hiphop'),(5,'indie'),(6,'blues')] #sample
# artists = [(7, 'Da Molotov'),(8, 'Океан Эльзы'),(9, 'Eminem')] #sample
# albums = [(7,'St. Anger',2003),(8,'Back in Black',1998),(9,'New Jersey',1988)] #sample
# track = [(50,'The Middle Is Gone',313,3),(51,'This Wild Darkness',249,3),(52,'A Dark Cloud Is Coming',324,3)] #sample
# genre_artist = [(1, 1, 1),(2, 1, 2),(3, 2, 2),(4, 3, 2),(5, 4, 2),(6, 5, 1),(7, 5, 2),(8, 6, 1),(9, 6, 4)] #sample
# artist_album = [(1, 5, 1),(2,	6, 2),(3, 5, 3),(4,	9, 4),(5, 7, 5),] #sample

# for elm in genres:
#     ins = connection.execute(f"INSERT into genre VALUES ({elm[0]},'{elm[1]}');")

# for elm in artists:
#      ins = connection.execute(f"INSERT into artist VALUES ({elm[0]},'{elm[1]}');")

# for elm in albums:
#     ins = connection.execute(f"INSERT into album VALUES ({elm[0]},'{elm[1]}',{elm[2]});")

# for elm in track:
#     ins = connection.execute(f"INSERT into track VALUES ({elm[0]},'{elm[1]}',{elm[2]},{elm[3]});")

# for elm in genre_artist:
#     ins = connection.execute(f"INSERT into genreartist VALUES ({elm[0]},{elm[1]},{elm[2]});")

# for elm in artist_album:
#     ins = connection.execute(f"INSERT into artistalbum VALUES ({elm[0]},{elm[1]},{elm[2]});")

release_date_2018 = connection.execute("SELECT title, release_date from album WHERE release_date = 2018;").fetchall()
print(release_date_2018)

longest_track = connection.execute("SELECT title, duration from track ORDER BY duration DESC LiMIT 1;").fetchall()
print(longest_track)

duration_3_5_min = connection.execute("SELECT title, duration from track WHERE duration > 210 ORDER BY duration DESC;").fetchall()
print(duration_3_5_min)

artist_name_1 = connection.execute("SELECT name from artist WHERE name NOT LIKE '%% %%';").fetchall()
print(artist_name_1)

my_track = connection.execute("SELECT title from track WHERE title LIKE '%%My%%' OR title LIKE '%%my%%' OR title LIKE '%%мой%%' OR title LIKE '%%Мой%%';").fetchall()
print(my_track)