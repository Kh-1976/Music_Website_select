import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:1234@localhost:5432/Music_Website')
connection = engine.connect()

print('Нзвание и год выхода альбомов, вышедших в 2018 году')
sel = connection.execute("""SELECT name, year FROM album 
                                WHERE year = 2018""").fetchall()
for i in sel:
    print(*i)
print('\nНазвание и продолжительность самого длительного трека')
sel = connection.execute("""SELECT name, duration FROM track 
                                ORDER BY duration DESC """).fetchone()
print(*sel)
print('\nНазвание треков, продолжительность которых не менее 3,5 минуты')
sel = connection.execute("""SELECT name FROM track 
                                WHERE duration >= '00:03:30'""").fetchall()
for i in sel:
    print(*i)
print('\nНазвания сборников, вышедших в период с 2018 по 2020 год включительно')
sel = connection.execute("""SELECT name FROM collection 
                                WHERE year BETWEEN 2018 AND 2020""").fetchall()
for i in sel:
    print(*i)
print('\nИсполнители, чье имя состоит из 1 слова')
sel = connection.execute("""SELECT name FROM performer 
                                WHERE (LENGTH(name)-LENGTH(REPLACE(name,' ','')))=0""").fetchall()
for i in sel:
    print(*i)
print('\nНазвание треков, которые содержат слово "Me" или "My"')
sel = connection.execute("""SELECT name FROM track 
                                WHERE name LIKE '%%Me%%' 
                                    OR name LIKE '%%My%%'""").fetchall()
for i in sel:
    print(*i)
