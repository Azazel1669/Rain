import sqlite3
import csv
import sqlite3

name = input()

con = sqlite3.connect(name)  # guilt.db

d = input()

g = input()

if g == 'good':
    g = 1
else:
    g = 0

cur = con.cursor()

result = cur.execute('''SELECT fact, pixie_id FROM Facts
WHERE good = ? AND happened = ?''', (g, d)).fetchall()
con.close()
with open("admissions.csv", mode="w", encoding='utf-8', newline='') as w_file:
    file_writer = csv.writer(w_file, delimiter=":")
    file_writer = csv.writer.writerow(["no", "name", "fact", "good"])
    c = 0
    for a in result:
        c += 1
        con = sqlite3.connect(name)
        cur = con.cursor()
        result = cur.execute('''SELECT name FROM Pixies
        WHERE Pixies.id = ?''', (a[1],)).fetchone()
        con.close()
        file_writer.writerow([c, result[0], a[0], g])
