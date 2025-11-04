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
    