thisdict ={
    "brand": "Ford",
    "model": "Mustang",
    "year": 2002,
    "color": ["red", "while","blue"]
}
print(len(thisdict))
print(type(thisdict))

mydict = dict(name = "tu" , age = 21 ,country = "vn")
print(mydict)
x = mydict["name"]
y = mydict.get("age")
z = mydict.keys()
print(x)
print(y,z)