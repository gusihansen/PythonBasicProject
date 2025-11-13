#模式匹配
score = 'B'

match score:
    case 'a':
        print('score is a')
    case 'b':
        print('score is b')
    case 'c':
        print('score is c')
    case 'd':
        print('score is d')
    case _:
        print('score is %s' %score)
age = 30
match age:
    case x if x<10:
        print(f'< 10 years old : {x}')
    case 10:
        print('10 years old')
    case 11|12|13|14|15|16|17|18:
        print('11~18 years old')
    case 19:
        print('19 years old')
    case _:
        print(f'{age} years old')


args =['gcc','hello.c','world.c']
match args:
    case ['gcc']:
        print('gcc: missing source file(s).')
    case ['gcc',file2,*files]:
        print('gcc compile :' + file2 +','+','.join(files))
    case ['clean']:
        print('clean')
    case _:
        print('invalid command')