import csv
import json

with open("danger.csv") as in_file:
    reader = csv.DictReader(in_file, delimiter=";")
    w = {}
    for line in reader:
        w.setdefault(line['monster'], [])
        w[line['monster']].append(line['danger'])
for i in w:
    l = w[i]
    l.sort(reverse=True)
    w[i] = l
h = dict(sorted(w.items(), key=lambda x: x[0], reverse=True))
with open('monsters.json', "w") as out_file:
    json.dump(h, out_file)
