
from random import randint

cpu = randint(1, 3)

print('=' + '-=' * 10)
print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')
print('=' + '-=' * 10)
p1 = int(input('Digite sua opção: '))

if p1 is cpu:
    print('EMPATE!')
else:
    if p1 == 1:
        if cpu == 2:
            print('VOCÊ PERDEU!')
        elif cpu == 3:
            print('VOCÊ VENCEU!')
    elif p1 == 2:
        if cpu == 1:
            print('VOCÊ VENCEU!')
        elif cpu == 3:
            print('VOCÊ PERDEU!')
    elif p1 == 3:
        if cpu == 1:
            print('VOCÊ PERDEU!')
        elif cpu == 2:
            print('VOCÊ VENCEU!')
