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