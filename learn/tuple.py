t = 1,2,3
s = 4,5,6
print(t+s,s[::-1])
print(s*2,s.index(5))
# 元祖不支持修改 元祖中的元素指向可变的列表 是可以改变的
w = ([1,2,3],[4,5,6])
w[0][0] = 0
print(w,w[0])
# 列表推导式支持
print([each * 2 for each in s])
print(type(1))
x = (1,)
print(type((1,)))
# 打包解包 同样适用于列表 字符串 左侧变量数量和右侧一样
t=(123,'s',3.14)
x,y,z=t
print(x,y,z)
# *表示接收多个剩余的
x,*y=t
print(x,y,z)
