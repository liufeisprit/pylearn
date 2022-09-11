# 列表表达式
oho = [i*2 for i in range(10)]
print(oho)

str = [c * 2 for c in 'liufei']
print(str)
str = [ord(c) for c in 'liufei']
print(str)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
        ]
col2 = [row[1] for row in matrix]
print(col2)

dig = [matrix[i][i] for i in range(len(matrix))]
print(dig)

dig2 = [matrix[i][len(matrix)-i-1] for i in range(len(matrix))]
print(dig2)

S = [[0] * 3 for i in range(3)]
print(S)

forwords = [i for i in ['liu','li','huang','ye'] if i[0]=='l']
print(forwords)

flatten = [col for row in matrix for col in row]
print(flatten)

str2 = [x + y + z for x in 'liu' for y in 'fei' for z in '1234']
print(str2)