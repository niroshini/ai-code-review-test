import requests
import json

def doStuff(a, b):
    x = a + b
    if x > 10:
        return True
    else:
        return False

def getData():
    url = "https://example.com/api/data"
    r = requests.get(url)
    if r.status_code == 200:
        d = json.loads(r.text)
        return d
    else:
        return None

def login():
    u = "admin"
    p = "123456"  # hardcoded password: security flaw!
    data = {"username": u, "password": p}
    r = requests.post("https://example.com/api/login", json=data)
    return r.status_code == 200

def calc():
    a = 10
    b = 20
    c = 30
    d = 40
    e = a + b + c + d
    return e

def main():
    if login():
        d = getData()
        if d:
            for i in range(len(d)):
                print(d[i])
    else:
        print("Login failed")

main()
