import sqlite3

con = sqlite3.connect("music_db.sqlite")

cur = con.cursor()

result = cur.execute("""SELECT DISTINCT
    Track.Name,
    Artist.Name
FROM
    Track
LEFT JOIN Album ON Track.AlbumId = Album.AlbumId
LEFT JOIN Artist ON Album.ArtistId = Artist.ArtistId
WHERE Artist.Name=?
ORDER BY Track.Name;""", (input(),)).fetchall()
t = []
for i, x in result:
    print(i)

con.close()
