import abc


a = {1,2,3,4,'5','5'}
print(1 in a)
print(a)
# t e s t四个元素 t重复了
a = set('test')
b = set('test2')
# 差集
print(b-a)
# 并集
print(b|a)
# 交集
print(b&a)
# 不同时存在 对称差集
print(b^a)
for each in a:
  print(each)
# 是否不相关 没有交集
print(set('test').isdisjoint(set('t')))
print(set('test').isdisjoint('t123'))
# 是否是另一个集合的子集
print(set('ts').issubset('tes'))
# 是否是另一个集合的超集
print(set('ts').issubset('tes'))
# 并集
print(set('a').union({1,2,3}))
# 交集
print(b.intersection(a))
# 差集
print(b.difference(a))
# 对称差集
print(a.symmetric_difference(b))