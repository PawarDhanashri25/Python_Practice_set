import json

freinds={"Dan": [20, "london", 33546], "Maria": [25, "Madrid", 34567]}

# data serialization using json 
with open('freinds.json', 'w') as f:
    json.dump(freinds, f, indent=4)


json_string=json.dumps(freinds,  indent=4)

print(json_string)
