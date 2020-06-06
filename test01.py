# _*_coding utf-8 -*-
#开发人员:dcl
#开发时间:2020/6/615:59
x =b'ABC'
print(x)

print('ABC'.encode('ascii'))
print('ABC'.encode('UTF-8'))

print('中文'.encode('utf-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


