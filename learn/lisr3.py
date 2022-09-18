# 可迭代对象变成列表
print(list('123'))
print(tuple('123'))
print(str(list('123')))
print(min([4,3,5,1]))
print(max([4,3,5,1],[100]))
print(max(1,2,3,5,8))
print(sum((1,2,3,5,8)))
print(len((1,2,3,5,8)))
print(sum((1,2,3,5,8),100))
s = [4,3,5,1]
# 全新列表
print(sorted(s,reverse=True))
print(sorted(['ab','c','d']))
# key 用len返回值排序
print(sorted(['ab','c','d'],key=len))
print(sorted(('FishC','Apple'),key=len))
s=[1,2,5,8,0]
# 返回迭代器
print(list(reversed(s)))