print('{:+} {:}'.format(520,-250))
print('{:,}'.format(1234))
print('{:_}'.format(1234))
# 小数点后保留多少位
print('{:.2f}'.format(3.1415))
# 小数点前后多少位
print('{:.2g}'.format(3.1415))
print('{:.6}'.format('3.141515926'))
# 二进制
print('{:#b}'.format(2))
print('{:c}'.format(80))
# 10进制
print('{:#d}'.format(80))
# 八进制
print('{:#o}'.format(80))
# 十六进制
print('{:#x}'.format(80))
# 科学计数法
print('{:e}'.format(80))
# 默认6位浮点数
print('{:f}'.format(80))
print('{:g}'.format(80.44))
print('{:%}'.format(0.8))
print('{:.2%}'.format(0.8))
print('{:.{prec}%}'.format(0.8,prec=2))

# f字符串 数字写在冒号左边
print(f'{0.8:.2%}')
