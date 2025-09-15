# 튜플 -> 리스트 리ㅡ트 ->튜플

list_a = [1,2,3]
print(f'type(list_a) = {type(list_a)}')
tuple_a = (10,20,30)
print(f'type(tuple_a) = {type(tuple_a)}')

print(type(tuple(list_a)))  
list_a = tuple(list_a)
