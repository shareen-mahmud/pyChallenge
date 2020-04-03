list1 = (["blue", "pink", "orange", "red"])
iterator = iter(list1)
print(iterator)
length = len(list1)
i = 0
while i < length:
    print(next(iterator))
    i = i+1