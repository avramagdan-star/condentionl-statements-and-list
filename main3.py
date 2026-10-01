lst = ['Apple', 'Gauva', 'Mango', 'Banana', 'Kiwi']

print("Length of list:", len(lst))
print("Fist Element:", lst [0])
print("Last Element:", lst[-1])

lst.append('Papaya')
print("Updated List :", lst)

lst.remove('Guava')
print("Updated list :", lst)

lst.sort()
print("Sorted List :", lst)

lst.pop(1)
print("Updated list :", lst)

lst.reverse()
print("Reversed List :", lst)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()
print("Updated List :", lst)