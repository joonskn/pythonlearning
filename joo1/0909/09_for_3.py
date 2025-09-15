# remove
list_a = [1,1,1,2]
# list_a.remove(1)
# print(list_a)

# 해법1 del을 이용하되 인덱스가 바뀌는 걸 감안하여 역순으로 지움
for i in range(len(list_a)-1,-1,-1):
    if list_a[i] == 1:
        del list_a[i]
print(list_a)

# 해법2 remove 활용
list_a = [1,1,1,2,2,2,2,2,2]
for i in range(len(list_a)):
    print('*')
    if 1 in list_a:
        list_a.remove(1)
    else:
        break
print(list_a)
