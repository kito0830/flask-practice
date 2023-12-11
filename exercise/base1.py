#1 
num = 10

#2
print(type(num))

# 3
num_str = str(num)

# 4
num_list = [num_str, '20', '30']
print(num_list)

# 5
num_list.append('40')

# 6
num_tuple = tuple(num_list)

# 7
val = input()
num_tuple += (val,)

# 8
num_set = {'40', '50', '60'}

print('num_tuple = {}'.format(num_tuple))
print('num_set = {}'.format(num_set))

# 9

