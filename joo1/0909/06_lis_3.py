list_a = [1,2,3]
list_b = [4,5,6]
last_name = '홍'
first_name = '길동'
# 리스트 연산
print(f'list_a + list_b = {list_a + list_b}')
print(f'list_a*2 = {list_a*2}')

print(f'last_name +first_name = {last_name+first_name}')
print(f'last_name * 2 = {last_name * 2}')

list_a[0] 

# append()
# list_a.append(요소)
print('# 리스트 뒤에 요소 추가')
list_a.append(4)
list_a.append(5)
print(list_a)
print('-'*30)
# insert
# list_a.insert(위치,요소)
print('# 요소 중간에 삽입')
list_a.insert(0, 10)
print(list_a)
print('@'*30)
# exrend
list_a = [1,2,3]
list_a.append([4,5,6])
print(list_a)
print('-'*30)
list_a = [1,2,3]
list_a.extend([4,5,6])
print(list_a)
print('$'*20)
list_a = [1,2,3]
list_a += [4,5,6]
print(list_a)
