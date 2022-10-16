# /之前只能使用位置参数 后面可以使用关键字参数
# def abc(a,/,b,c):
#   print(a,b,c)
# abc(1,b=3,c=2)
# *后面只能使用关键字参数
def abc(a,*,b,c):
  print(a,b,c)
abc(1,c=2,b=3)
# 收集参数 解包arg为元祖
def abc2(*arg):
  print('有{}个参数'.format(len(arg)))
  print('第二个参数是{}'.format(arg[1]))
  return 1,2,3
x,y,z = abc2(1,2,3,4)
print(x,y,z)
# 收集参数后面参数必须是关键字参数
def abc3(*arg,a,b):
  print(arg,a,b)
abc3(1,2,3,a=4,b=5)
# **返回字典
def abc4(a,*b,**c):
  print(a,b,c)
abc4(1,2,3,x=4,y=5)
abc4(1,*(2,3),**dict(x=4,y=5))
print(*(2,3),*dict(x=4,y=5))