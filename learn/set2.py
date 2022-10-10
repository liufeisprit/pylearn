# 不可变集合
print(frozenset('123'))
s = set('abc')
s.update('d')
s.intersection_update('avcs')
print(s)
s.difference_update('ab')
print(s)
s.symmetric_difference('abc')
print(s)
s.remove('c')
# 删除不存在不会报错
s.discard('f')
# s.pop()
s.clear()
# 可哈希
x = {1,2,3}
#  不可哈希不可作为集合值
# y = {x,4,5}
# y={[1],2,3}
# 不可变集合
y={frozenset(x),4,5}