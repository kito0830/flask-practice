# セット
s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

u = s.union(t) # 和集合
print(u)

u = s.intersection(t) # 積集合
print(u)

u = s.difference(t) # 差集合
print(u)

u = s.symmetric_difference(t) # 対象差
print(u)

s |= t # sをtに更新
print(s)

# issuperset, issubset, isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(u)) # sがtの部分集合かTrue/False
print(s.issuperset(t)) # tがsの上位集合かTrue/False
print(t.isdisjoint(s)) # sとtが交わっているかTrue/False

