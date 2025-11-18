nameList = ['Michael','Bob','Bessie'];
for name in nameList:
    print(name)

total = 0;
# for x in [1,2,3,4,5,6,7,8,9]:
#     total +=x
# print(total)
# for循环，range函数
for x in list(range(101)):
    total += x
print(total)

#while循环
total = 0

n= 100

while n>0:
    total  += n
    n-=1
print(total)


#练习

L = ['Bart','Lisa','Bessie']

for name in L:
    print(f'hello,{name}')



n = 0
while n <= 100:
    #print(n)
    n+=1
#break
n = 0
while n <= 100:
    if n == 10:
        break
    #print(n)
    n+=1
#continue
n = 0
while n <= 100:
    n+=1
    if (n%10)==0:
        continue
    print(n)

