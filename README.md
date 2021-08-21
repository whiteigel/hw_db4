# SQL Requests and Results

В данном файле только запросы типа SELECT и результаты этих сапросов. Запросы INSERT, так же как и SELECT, в файле main.py.

1. Название и год выхода альбомов, вышедших в 2018 году;
```
SELECT title, release_date from album WHERE release_date = 2018;
```
```
"Demi Masa"	2018
"Everything Was Beautiful, and Nothing Hurt"	2018
"Kamikaze"	2018
```

2. Название и продолжительность самого длительного трека;
```
SELECT title, duration from track ORDER BY duration DESC LiMIT 1;
```

```
"LA12"	2820
```

3. Название треков, продолжительность которых не менее 3,5 минуты;

```
SELECT title, duration from track WHERE duration > 210 ORDER BY duration DESC;
```

```
"LA12"	2820
"LA17"	2520
"LA14"	2340
"LA15"	1920
"LA16"	1800
"LA13"	1620
"All Within My Hands"	528
"Invisible Kid"	510
"Some Kind of Monster"	505
"Mithras"	456
"St. Anger"	441
"Ball and Biscuit"	439
"Shoot Me Again"	430
"The Unnamed Feeling"	428
"Blood on Blood"	376
"Black Mamba"	373
"13"	359
"Lay Your Hands on Me"	358
"CSDB FM feat. Iwa K"	351
"Frantic"	350
"My World"	346
"Ill Be There for You"	346
"Conflicted"	345
"Lights"	341
"Take It 2 Your Face"	340
"Seen Savage"	337
"Eastern Promise"	333
"UV Rays"	330
"Badline"	329
"Ultraviolet"	327
"Sweet Amber"	327
"Concrete Jungle"	325
"Dirty Window"	325
"A Dark Cloud Is Coming"	324
"Kilauea"	323
"Lost Souls"	320
"Obsidian"	318
"Bad Medicine"	316
"Mere Anarchy"	315
"Made in Detroit"	315
"Arp Tune VIP"	314
"Nowhere to Run"	314
"Purify"	314
"The Middle Is Gone"	313
"Bassline Secret [Skantia Remix]"	312
"Voices"	310
"Homebound Train"	310
"Welcome to Hard Times"	308
"Wild Is the Wind"	308
"Inertia"	303
"Spectrum"	300
"Animal"	300
"Terminal"	299
"Take Control"	298
"Serpent"	298
"Testamen"	297
"There for You [Breakage Remix]"	297
"Only You"	296
"Lock Stock"	291
"Funk Flicks"	288
"Wispers"	288
"Overstep"	287
"Check Your People"	287
"Falling Rain and Light"	286
"Stick to Your Guns"	285
"Born to Be My Baby"	280
"LDN Bass"	280
"Living in Sin"	279
"Back & Forth"	278
"Like a Motherless Child"	277
"My Life"	276
"Breakadawn"	275
"I am Slowly Turning Into You"	275
"Forgotten"	273
"Deep Breath"	272
"Down with You"	271
"Paradigm"	271
"Death Letter"	270
"Bad Boy Selection"	269
"99 in the Shade"	269
"Cyclone"	268
"The Tired and the Hurt"	268
"The Sorrow Tree"	268
"Party Move"	267
"Di Hadapan Babylon"	266
"Testamen [Novum Testamentum]"	265
"The Last of Goodbyes"	263
"Lift You Up"	262
"Illuminate (feat. Tom Cane) [Extended Mix]"	261
"One Last Chance (feat. Skyelle) [Remix]"	261
"Puzzle"	260
"Cowards"	260
"Pressure"	260
"War Dub"	259
"All for You (feat. Karen Harding) [Extended Mix]"	257
"Renaissance"	256
"Icky Thump"	255
"Cluster"	251
"Rust"	251
"Wont Hold Back"	251
"This Wild Darkness"	249
"Check Your People (Remix)"	247
"Lonely Day (feat. Spiralus)"	244
"My Doorbell"	242
"Till Dawn"	237
"Kenya"	231
"Funk Me"	231
"No Answer"	223
"Schematic"	220
```

4. Названия сборников, вышедших в период с 2018 по 2020 год включительно;

```
SELECT title from compilation WHERE release_date BETWEEN 2018 AND 2020;
```

```
"The White Stripes Greatest Hits"
"RAM Drum & Bass Annual 2020"
"Neil Young Archives Vol. II: 1972–1976"
"Kate Bush Remastered Part I"
"John Maus"
```

5. Исполнители, чье имя состоит из 1 слова;

```
SELECT name from artist WHERE name NOT LIKE '%% %%';
```

```
"Metalica"
"AC/DC"
"Moby"
"Eminem"
```

6. Название треков, которые содержат слово "мой"/"my".

```
SELECT title from track WHERE title LIKE '%%My %%' OR title LIKE '%% my %%' OR title LIKE '%% мой %%' OR title LIKE '%%Мой %%';
```

```
"My World"
"All Within My Hands"
"Born to Be My Baby"
"The Big Three Killed My Baby"
"My Doorbell"
"My Life"
```