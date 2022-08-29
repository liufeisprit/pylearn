import random
a=1
x=3
x,a = a,x
print(a,x)
# \转译符
print("\"life is short let\'s learn python \n 你好")
# r表示不转译
print(r"D:\three\two\one\now")
# 长字符串
print("""
asa 
w 
fff
""")
# print("爱上"*10)
# temp = input("输入一个")
# guess = int(temp)
# if(guess == 8):
#   print("猜中了")
# else:
#   print("猜错了")
x = random.getstate()
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
random.setstate(x)
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))