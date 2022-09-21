d= dict.fromkeys('abc',123)
d.update({'c':4})
d.update(a=4, b=2)
print(d)
print(d.get('dc',100))
#设置不存在key的值
print(d.setdefault('a',100))
print(d)

print(d.items())
print(d.keys())
print(d.values())
print(d.copy())
d.clear()
print(len(d))
print('c' in d)
d= dict.fromkeys('abc',123)
# 根据key返回list
print(list(d))
print(d.keys())
# 迭代器
print(iter(d))
f= dict(a=1,b=2,c=3)
# 字典推导式
b= {
  k: v for k,v in f.items() if k == 'a' or v == 3
}
c = {
  x:y for i,x in enumerate([1,3,4]) for l,y in enumerate([2,4,6]) if i == l
}
print(b)
print(c)