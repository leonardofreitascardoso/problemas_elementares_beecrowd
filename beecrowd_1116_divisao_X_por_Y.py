##beecrowd | 1116
##-------------------------------------------------------------


##V1: exibe o resultado na medida em que os pares são digitados
n = int(input())

for _ in range(n):
    x, y = map(int,input().split())

    if y == 0:
        print('divisao impossivel')
    else:
        print(f'{x/y:.1f}')

##V2: exibe o resultado somente ao fim
pares = int(input())
lista = []
contador = 0

while contador < pares:
    lista.append((input().split()))
    contador += 1

for item in lista:
    if int(item[1]) == 0:
        print('divisao impossivel')
    else:
        print(int(item[0])/int(item[1]))