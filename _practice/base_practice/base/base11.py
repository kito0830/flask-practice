# 辞書型のメソッド
car = { 'brand': 'Toyota', 'model': 'Prius', 'year': 2015 }

temp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

car.update(temp_car)
# print(car)

car['city'] = 'Toyota-shi'
car['year'] = 2017
# print(car)

value = car.popitem()
# print(car)
# print(value)

value = car.pop('model')
# print(car)
# print(value)

car.clear
print(car)

del car
print(car)  
