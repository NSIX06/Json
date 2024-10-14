import json 

with open("streaming.json", encoding='utf-8') as meu__json:
    streaming = json.load(meu__json)

def line():
    print("-----------------------------------")


print(streaming)

