import json 

with open("jojo.json", encoding='utf-8') as meu__json:
    jojo = json.load(meu__json)

def line():
    print("-----------------------------------")


print(jojo)

