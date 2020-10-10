# searching for an item in an unordered list
# sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    idx =0
    flag = 0
    for i in itemlist:
        idx +=1
        if i == item:
            flag = 1
            return (f"Item found at position {idx}")
    if idx == len(itemlist) and flag == 0:
        return "Item not in list"

print(find_item(87, items))
print(find_item(900, items))
