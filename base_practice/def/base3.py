# 関数
def print_animal():
  global animal
  animal = 'Cat'
  print('関数内ではanimal = {}, id = {}'.format(animal, id(animal)))

# animal = 'Dog'

print_animal()
print('関数外ではanimal = {}, id = {}'.format(animal, id(animal)))

