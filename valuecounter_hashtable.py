# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = None
filter = dict()
for item in items:
    filter[item]=0

# iterate over each item and increment the count for each one
for i in items:
    filter[i] = filter[i] +1

# print the results
print(filter)
