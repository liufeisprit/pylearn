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
# 不同时存在
print(b^a)

