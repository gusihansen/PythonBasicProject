# #dict
# # Python内置了字典：dict的支持，dict全称dictionary,
# # 在其他语言中也成为map，使用key-value存储，具有极快的存储速度
# names = ['Micheal','Bob','Tracy','Bessie']
# scores = [94,55,66,65]
# d = {'Micheal':94,'Bob':55,'Tracy':66,'Bessie':65,'Bessie':99}
# print(d['Bessie'])
#
# d={}
# print('a' in d)
# d['a'] = 100
# print(d)
# d['b'] = 102
# print(d)
# temp = d.get('d')
# print(temp)
# d['add'] = 'how to add'
# print(d)
# d.pop('a')
# print(d)
# # dict 的 key 必须是不可变对象
#
#
# #set
# s= {1,}
# s.add(1)
# s.add(2)
# print(s)
# l =[1,2,3,4,5,6]
# s = set(l)
# print(s)
# t = (1,2,3,4,5)
# s = set(t)
# print(s)
# s.add(6)
# print(s)

# tuple

t = (1,2,[1,2,3,4])
#t = (1,2,3)
# d ={t : 1}
# print(d)
s = set(t)
print(s)