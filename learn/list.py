a=[1,'s',False,100,5,5,7,9,False]
b=[2]
print(a+b)
# 字符串不一样的是，列表中的元素是可以改变的
# a[2:] = []
a.insert(1,"第一个")
# 删除对象不存在就会报错
a.remove('第一个')
print(a.pop(1))
# a.sort(reverse=True)
print('1的次数',a.count(1))
a[a.index(100)] = 101
# index返回第一个查到的下标 index(start,end)
print('a===',a)
print('False下标',a.index(False))
print('False2下标',a.index(False,a.index(False)+1))
print('浅拷贝',a.copy(),a[:])
print(a)
# print(a[:0])
# print(a[::2])
# print(a[0:3:3])
# 只能添加一个
a.append('one')
# extend添加可迭代对象
a.extend(['4','5'])
a[len(a):] = ['6']
# print(a[])
# 1、List 写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，List 可以被索引和切片。
# 3、List 可以使用 + 操作符进行拼接。
# 4、List 中的元素是可以改变的

c = (1,'2',False)
tup = ()
tup1 = (1,)
print(c[0],tup,tup1[0])
# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法都是一样的。
# 3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
# 4、元组也可以使用 + 操作符进行拼接。