import json

friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}

with open('freinds2.json', 'w') as f:
    json.dump(friends, f, indent=3)



#Deserailization from file into object

with open('freinds2.json', 'rt') as f:
    obj=json.load(f)
    print(type(obj))
    print(obj)

#loading json encoded string into a python object


json_string= """{
    "Dan": [
        20,
        "London",
        13242252
    ],
    "Maria": [
        25,
        "Madrid",
        34232424
    ]
}"""

obj= json.loads(json_string)
print(type(obj))
print(obj)
