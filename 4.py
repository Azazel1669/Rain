import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""
SELECT films.title
FROM   films
JOIN   genres
ON
       films.genre = genres.id
WHERE (films.year BETWEEN 1995 AND 2000) AND genres.title = 'детектив' """).fetchall()

for (title, ) in result:
    print(title)