import keyword
# isdecimal 一个字符串是否仅有十进制的数字字符
# isnumeric 如果字符串是数值字符串，返回True，否则返回False。
# isdigit 如果字符串是数字字符串，返回True，否则返回False
print('-3'.isdecimal())
print('-2'.isnumeric())
print('-1'.isdigit())
# 是否是变量标识符
print('i_love_you'.isidentifier())
print(keyword.iskeyword('if'))