# Þurfum þennan
from flask import Flask, json

# Tengjum skrána bekkur.json (verður að vera absolute url c:/Users/gjg/Desktop/Verkefni-2-json/json-daemi/)
with open("bekkur.json","r") as skra:
    bekkur = json.load(skra)

# Kíkjum i breytuna 
print(bekkur)




