x='sssabc'
print(x.count('s'))
print(x.count('s',0,2))
print(x.find('s',2))
print(x.rfind('z'))
print(x.replace('s','z',2))
# 第三个参数为忽略某些字符串
print('sssabclmc'.translate(str.maketrans('sabc','1234','lc')))
# 左闭右开
print(x.startswith('s'))
print(x.startswith('s'))
print(x.startswith(('s','a','b')))
# 单词首字母大写
print('Abs Bbc'.istitle())
# 所有字母大写
print('ABC'.isupper())
# 是否单词 不能包含空白字符
print('sssabc\n'.isalpha())
# 是否空白字符
print('\n'.isspace())
# 是否可打印字符
print('\n'.isprintable())
