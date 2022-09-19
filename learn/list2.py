print([1,2,3]+[1,2,3])
s = [1,2]
s*=2
print(id(s))
# in 序列中包含某个元素 字符串 list 元祖 not in
print('ab' in 'abc')
print(1 in [1,2,3])
# del删除对象 序列里元素
x = [1,2,3,4,5]
del x[1:4]
print(x)
x = [1,2,3,4,5]
del x[::2]
print(x)
x = [1,2,3,4,5]
del x[:]
print(x)
# 判断序列每个是否为真
print(all([1,0,1]))
# 返回List 元组和索引
print(list(enumerate((1,2,3),10)))
# 返回list 矩阵
print(list(zip([1,2,3],[4,5])))
print(list(zip([1,2,3],'li')))
import itertools
from sys import intern
from timeit import repeat
# 不会丢掉短的序列
print(list(itertools.zip_longest([1,2,3],'li')))
print(list(map(pow,[1,2,3],[2,4,1])))
print(list(filter(str.islower,'lIawa')))
y = iter(list('123'))
print(next(y))
print(next(y))
print(next(y))
print(next(y,'没了'))