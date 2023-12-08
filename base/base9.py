# リストのメソッド
list_a = [1, 2, 3, 4, 5]

list_b = list_a[3:]
print(list_b)

# append, insert, extend, clear
list_a.append('apple')
print(list_a)
list_a.extend(['banana', 'melon'])
print(list_a)
list_a.insert(1, 'grape')
print(list_a)
# list_a.clear()
# print(list_a)

# pop, remove, count, index
list_a = [1, 2, 3, 4, 5, 3]
list_a.remove(3)

