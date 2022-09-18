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