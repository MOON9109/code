#Shallow copy & Deep copy

#객체의 복사 종류 : copy, shallow copy, deep copy

#Ex1 -copy , call by reference

a_list=[1,2,3,[4,5,6],[7,8,9]]

b_list=a_list

b_list[2]=100

print('Ex1',id(a_list))
print('Ex1',id(b_list))

print('Ex1',a_list)
print('Ex1',b_list)

b_list[3][2]=100

print('Ex1',a_list)
print('Ex1',b_list)

#immutable : int, str, float, bool, unicode...

#Ex2 -shallow copy
import copy

c_list=[1,2,3,[4,5,6],[7,8,9]]
d_list=copy.copy(c_list)

print('Ex2',id(c_list))
print('Ex2',id(d_list))

d_list[1]=100

print('Ex2',c_list)
print('Ex2',d_list)

#얕은 복사는 밖에 있는 리스트의 id만 바꿔주기 때문에 내부의 리스트 id는 그대로 사용
d_list[3].append(1000)
d_list[4][1]=10000
print('Ex2',c_list)
print('Ex2',d_list)

#Ex3

e_list=[1,2,3,[4,5,6],[7,8,9]]
f_list=copy.deepcopy(e_list)

print('Ex2',id(e_list))
print('Ex2',id(f_list))

f_list[3].append(1000)
f_list[4][1]=10000

print('Ex3',e_list)
print('Ex3',f_list)
