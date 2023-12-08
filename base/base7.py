# 文字列型

fruit = 'apple'
print(fruit)
# print(type(fruit))


# print(fruit * 10)

# new_fruit = fruit + ' banana'
# print(new_fruit)

fruit = 'banana'
# print(fruit[2])

# encode, decode => bytes型
# byte_fruit = fruit.encode('utf-8')
# print(byte_fruit)
# print(type(byte_fruit))

# str_fruit = byte_fruit.decode('utf-8')
# print(str_fruit)
# print(type(str_fruit))

# count
msg = 'ABCDEABC'
print(msg.count('ABCCC'))

# startswith, endswith
print(msg.startswith('ABB'))
print(msg.endswith('C'))

# strip（両端）, rstrip（右端）, lstrip（左端）
msg = ' ABC '
print(msg.strip())# デフォルトでは空白を削除

# upper, lower, swapcase, replace, capitalize
msg = 'abcABC'
print(msg.lower()) # 小文字に変換
print(msg.upper()) # 大文字に変換
print(msg.swapcase()) # 大文字と小文字を入れ替える

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF', 1) #第三引数に指定した数だけ置換する（左から数えて）
print(msg_r)


msg = 'hello WoRld'
print(msg.capitalize()) # 先頭の文字を大文字にする, それ以外は小文字にする


# 文字列の一部取得、format, islower, isupper
msg = 'hello, my name is taro'
print(msg[1:10:3])
print('hello {}'.format('Taro'))

msg = 'APPLE'
print(msg.isupper())

# find, index, rfind, rindex
msg = 'ABCDEABC'
print(msg.find('ABC')) 
print(msg.rfind('ABC'))

print(msg.index('ABC')) 
print(msg.rindex('ABC'))
