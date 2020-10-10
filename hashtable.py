# demonstrate hashtable usage
# Coded with referenec to Joe Marini's course on linkedIn 


# TODO: create a hashtable all at once
items = dict({"key1":1,"key2":2,"key3": 3})
print(items)

# TODO: create a hashtable progressively
items1 = {}
items1["key1"]=1
items1["key2"]=2
items1["key3"]=3
print(items1)

# TODO: try to access a nonexistent key
#print(items1["key4"])

# TODO: replace an item
items1["key2"]= "blahblah"
print(items1)

# TODO: iterate the keys and values in the dictionary
for key,value in items1.items():
    print( f"key: {key}, value: {value}")