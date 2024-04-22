import requests
import json

def pixie(w, host='127.0.0.1', same=0):
    sp = []
    a = w.split(',')
    url = f"http://{host}:5000"
    # response = requests.get(url).json()
    with open('2.json') as in_file:
        response = json.load(in_file)
    for res in response:
        for q in res['persons']:
            b = res['persons'][q].split(', ')
            c = 0
            for e in b:
                if e in a:
                    c += 1
            if c <= same:
                r = [q, res['place']]
                sp.append(r)
    sp.sort(key=lambda a: a[0])
    sp.sort(key=lambda a: len(a[1]))
    return sp

print(pixie('freckled, short, large-headed, boots, pointy-nosed', host='localhost'))
