a = 10
b = 10
print(a is b)
a=20
print(id(a) == id(b))
del a,b # 删除引用
# print(a) 报错