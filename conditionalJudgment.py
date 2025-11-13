#条件判断
#inputStrData = input('BessieAge: ')
# BessieAge = int(inputStrData)
# print(BessieAge)
# if BessieAge >= 18:
#     print("Bessie can vote")
# else :
#     print("Bessie can't vote")
#
# if BessieAge >= 18:
#     print('she age is ',BessieAge)
#     print('adult')
# elif BessieAge >= 6:
#     print('she age is ',BessieAge)
#     print('teenager')
# else :
#     print('she is a baby')

inputData = input('Bessie\'s height: ')
height = float(inputData)
inputData = input('Bessie\'s weight: ')
weight = float(inputData)

bmi = weight / (height ** 2)
print('Bessie\'s bmi: %.2f' %bmi)
if bmi <= 18.5:
    print('过轻')
elif 18.5 < bmi <= 25:
    print('正常')
elif 25< bmi <=28:
    print('过重')
elif 28< bmi <=32:
    print('肥胖')
else :
    print('严重肥胖')
