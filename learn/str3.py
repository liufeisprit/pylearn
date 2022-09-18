import keyword
# isdecimal 一个字符串是否仅有十进制的数字字符
# isnumeric 如果字符串是数值字符串，返回True，否则返回False。
# isdigit 如果字符串是数字字符串，返回True，否则返回False
print('-3'.isdecimal())
print('-2'.isnumeric())
print('-1'.isdigit())
# 是否是变量标识符
print('i_love_you'.isidentifier())
# 是否关键字
print(keyword.iskeyword('if'))
# 左侧 右侧去除字符串 NONE去除空白
print('  123'.lstrip())
print('  123   '.rstrip())
print('  123   '.strip())
# 去除左侧目标字符串 直到找到不符合目标字符串的字符为止
print('w1ww.test.com'.lstrip('wcom.'))
print('w1ww.test.com1'.rstrip('wcom.'))
# removeprefix removesupfix 3.9新增方法
# print("w1ww.test.com".removeprefix('wcom.'))
# print("w1ww.test.com".removesupfix('wcom.'))
# 切割成三元祖 从左往右 从右往左  返回元祖
print('w1ww.test.com1'.partition('test1'))
print('w1ww.test.com1'.rpartition('.'))
print('w1ww.test.com1'.partition('.'))
# split类似js 返回list
print('w1ww.test.com1'.split('.',1))
print('w1ww.test.com1'.rsplit('.',1))
# 按换行符切割 keepends是否携带换行符
print('w1ww\ntest\rcom1\r\n1'.splitlines())

