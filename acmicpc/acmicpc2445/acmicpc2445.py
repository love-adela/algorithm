n = int(input())

for i in range(n):
    for j in range(1,i+2):
        print('*', end='')
    for j in range(2*(n-(i+1))):
        print(' ', end='')
    for j in range(1, i+2):
        print('*', end='')
    print('')

for i in range(n-1, 0, -1):
    for j in range(i):
        print('*', end='')
    for j in range(2*(n-i)):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print('')
