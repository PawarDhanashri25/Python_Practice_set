import pickle

freinds1={'Dan': [20, "Landon", 3467898], "Maria": [25, "Paris", 34364756]}
freinds2={"Andheri":[35, "Mumbai", 346572], "Naina": [40, "Pune", 2433567]}

freinds=(freinds1, freinds2)

#data serialization using pickle to store the dict data in file 
with open("freinds.dat", 'wb') as f:
    pickle.dump(freinds, f)


with open("freinds.dat", 'rb') as f:
    obj= pickle.load(f)
    print(type(obj))
    print(obj)
    
