str = 'python'
print(str[0])
print(str[-1])
# 字符串不能被改变
# str[0] = 's'
# 截取的范围是前闭后开的（头下标取，尾下标不取），并且两个索引都可以省略：
print(str[1:5])
# print(str[0:str.__len__-1])


# 1、反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。
# 2、字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# 3、Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# 4、Python 中的字符串不能改变。