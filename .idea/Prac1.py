import json

person={
    "name":"JACK",
    "age":22
}

with open("info.json", "r") as f:
    json.dump(person, f)

with open("info.json", "r") as f:
    print(json.load(f)["name"])



#def firstlast(number,list):




#firstlast(number,list)

