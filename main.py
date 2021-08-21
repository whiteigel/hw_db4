import sqlalchemy
import pandas as pd

db = 'postgresql://postgres@localhost:5432/netology'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

genres = [(1,  'pop'), (2, 'rock'), (3, 'jazz'), (4, 'hiphop'), (5, 'indie'), (6, 'blues')]

artists = [(3, 'AC/DC'), (4, 'Bon Jovi'), (5, 'Moby'), (6, 'Morgue Vanguard'), (7, 'Da Molotov'),
           (8, 'Океан Эльзы'), (9, 'Eminem')]

albums = [(1, 'Long Ambients 2', 2019), (2, 'Demi Masa', 2018), (3, 'Everything Was Beautiful, and Nothing Hurt', 2018),
          (4, 'Kamikaze', 2018), (5, 'Con Todo Respeto', 2004), (6, 'Songs of Faith and Devotion', 1993),
          (7, 'St. Anger', 2003), (8, 'Back in Black', 1998), (9, 'New Jersey', 1988)]

track = [(1, 'LA12', 2820, 1), (2, 'LA13', 1620, 1), (3, 'LA14', 2340, 1), (4, 'LA15', 1920, 1), (5, 'LA16', 1800, 1),
         (6, 'LA17', 2520, 1), (7, 'Junta Titimangsa', 139, 2), (8, 'Breakadawn', 275, 2),
         (9, 'CSDB FM feat. Iwa K', 351, 2), (10, 'Testamen', 297, 2),
         (11, 'Buckshot Funk feat. Mr.EP & Sarkasz', 137, 2), (12, 'Rotasi Baja (Interlude)', 58, 2),
         (13, 'Di Hadapan Babylon', 266, 2)]

compilation = [
    (1, 'The White Stripes Greatest Hits', 2020), (2, 'RAM Drum & Bass Annual 2020', 2020),
    (3, 'Neil Young Archives Vol. II: 1972–1976', 2020), (4, 'Kate Bush Remastered Part I', 2018),
    (5, 'John Maus', 2018), (6, 'Civilisation Kero Kero Bonito', 2021),
    (7, 'Limp Pumpo Full Discography', 2021), (8, 'David Bowie A New Career in a New Town [1977 - 1982]', 2017)]

genre_artist = [(1, 1, 1), (2, 1, 2), (3, 2, 2), (4, 3, 2), (5, 4, 2), (6, 5, 1), (7, 5, 2), (8, 6, 1), (9, 6, 4)]

artist_album = [(1, 5, 1), (2, 6, 2), (3, 5, 3), (4, 9, 4), (5, 7, 5)]

track_compilation = [(1, 53, 1), (2, 54, 1), (3, 55, 1), (4, 56, 1), (5, 57, 1), (6, 58, 1), (7, 59, 1)]

for elm in artists:
     ins = connection.execute(f"INSERT into artist VALUES ({elm[0]},'{elm[1]}');")

for elm in genres:
    ins = connection.execute(f"INSERT into genre VALUES ({elm[0]},'{elm[1]}');")

for elm in albums:
    ins = connection.execute(f"INSERT into album VALUES ({elm[0]},'{elm[1]}',{elm[2]});")

for elm in track:
    ins = connection.execute(f"INSERT into track (id, title, duration) VALUES ({elm[0]},'{elm[1]}',{elm[2]});")

for elm in compilation:
    ins = connection.execute(f"INSERT into compilation (id, title, release_date) VALUES
    ({elm[0]},'{elm[1]}',{elm[2]});")


for elm in genre_artist:
    ins = connection.execute(f"INSERT into genreartist VALUES ({elm[0]},{elm[1]},{elm[2]});")

for elm in artist_album:
    ins = connection.execute(f"INSERT into artistalbum VALUES ({elm[0]},{elm[1]},{elm[2]});")

for elm in track_compilation:
    ins = connection.execute(f"INSERT into trackcompilation VALUES ({elm[0]},{elm[1]},{elm[2]});")


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

compilation_2018_2020 = connection.execute("SELECT title from compilation WHERE release_date BETWEEN 2018 AND 2020;").fetchall()
print(compilation_2018_2020)
print()

artist_name_1 = connection.execute("SELECT name from artist WHERE name NOT LIKE '%% %%';").fetchall()
print(artist_name_1)
print()

my_track = connection.execute("SELECT title from track WHERE title LIKE '%%My %%' OR title LIKE '%% my %%' "
                              "OR title LIKE '%% мой %%' OR title LIKE '%%Мой %%';").fetchall()
print(my_track)
