# enumirate, zip, while

fruits = ['apple', 'banana', 'orange']

for index, value in enumerate(fruits):
  print(index, value)

classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Kenta', 'Akari', 'Makoto']

for a, b in zip(classA, classB):
  print(a, b)


count = 0
while count < 5: # countが5未満の間ループ
  print(count)
  count += 1
