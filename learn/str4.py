# 列表 元祖都可以
print('->'.join(['1','2','3']))
print('->'.join(('1','2','3')))
print('1'*2)
# join拼接速度快
print(''.join((['s']*2)))
# 格式化字符串
print('今天星期{}'.format('天'))
print('今天星期{1},明天星期{0}'.format('天','六'))
print('我是{name},我爱{fav}'.format(name='l',fav='y'))
print('{},{},{}'.format(1,'{}',2))
print('{},{{}},{}'.format(1,2))
print('{:^10}'.format(123))
print('{1}{0:>10}'.format(520,250))
print('{0:010}'.format(520))
print('{0:%^10}'.format(520))
# 只对数字有效
# print('{0:010}'.format('test'))