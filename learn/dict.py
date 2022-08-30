# 字典（dictionary）是 Python 中另一个非常有用的内置数据类型。

# 字典是一种映射类型（mapping type），它是一个无序的键值对（key-value）集合。

# 关键字（key）必须使用不可变类型，也就是说list和包含可变类型的 tuple 不能做关键字。

# 在同一个字典中，关键字（key）必须互不相同。
dic = {}
dic = {'a': 1,'t': 1230,'r': 666}
# print(dic[1])
del dic['a']
print('a' in dic)
print(sorted(dic.keys()))
print('s' not in dic)
print(dict(a=1,b=2,c=3))
print(dict([('a',1),('b',2),('c',3)]))
print({
  x: x**2 for x in (2,4,6)
})