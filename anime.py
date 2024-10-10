import json 

with open("jojo.json", encoding='utf-8') as meu__json:
    jojo = json.load(meu__json)

def line():
    print("-----------------------------------")

"""
print(jojo)
"""

#*chaves
for c in jojo:
    print(c)
line()

#*itens
for i in jojo.items():
    print(i)
line()

#*valores
for v in jojo.values():
    print(v)
line()

#*nome do autor
print(jojo["autor"])
line()

#*detalhes
for d in jojo["detalhes"].values():
    print(d)
line()
