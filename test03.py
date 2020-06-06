# -*- coding: utf-8 -*-
# @Author:dcl
# @Time:2020/6/618:33
# @Version:
# @Function:
L = [0,1,2,3,4,5]
sum = 0
for x in L:
    sum = sum + x
    print(sum)
    print('dhadajkdhakdjakhdahdka')

print('bb分支来了')
print('hahahahaa')


sun = 0
for y in list(range(6)):
    sun = sun + y
    print('sun=',sun)

print(list(range(6)))
print('-----------------------------------------')

s = 0
n = 100
while n > 0:
    s = s + n
    n = n - 1
print('s =',s)

n = 0
while n <= 100:
    print('n:',n)
    n = n + 1

print('------------------------------------')
m=0
while m <= 100:
    if m > 10:
        break;
    print('m:',m)
    m = m + 1

print('------------------------------------')
v = 0
while v <= 100:
    if v < 10:
        v = v + 1
        continue
    print('v:', v)
    v = v + 1

print('-------------------------------------')
a = 1
while a < 10:
    if a % 2 == 0:
        a = a + 1
        continue
    print(a)
    a = a + 1

