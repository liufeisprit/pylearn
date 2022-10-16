x=250
# global修饰的全局的
def myfunc():
  global x
  x=123
  print(x)
myfunc()
print(x)

def funA():
  x=520
  def funB():
    # nonlocal修饰上一个作用域
    nonlocal x
    x = 888
    print(x)
  funB()
  print(x) 
funA()
print(x)