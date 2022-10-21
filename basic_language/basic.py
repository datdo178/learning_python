mylist = ["b", "a", "c", "c"]
myValue = (1, 2, 3)
mylist = list(dict.fromkeys(mylist))
print(mylist)

print(dict.fromkeys(mylist, 1))