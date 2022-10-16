print(str(321)[::-1])
a = {
  'a': 1
}
# print(list(map(set,zip(*'liufei'))))
strs = ["flower","flow","flight"]
ss=list(map(set,zip(*strs)))
print(ss)
res=''
for i, x in enumerate(ss):
  x = list(x)
  if len(x)>1:
    break
  res+=x[0]
print(res)