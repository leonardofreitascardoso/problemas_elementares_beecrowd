n1  = int(input())
n2 = int(nput())

n1_copia = n1
n2_copia = n2

lista = []

if n1 < n2:
    qtd_termos = n2 - (n1+1)
    primeiro_do_intervalo = n1_copia+1
    while primeiro_do_intervalo < n2_copia:
        lista.append(primeiro_do_intervalo)
        primeiro_do_intervalo+=1           

elif n1 > n2:
    qtd_termos = n1 - (n2+1)
    primeiro_do_intervalo = n2_copia+1
    while primeiro_do_intervalo < n1_copia:
        lista.append(primeiro_do_intervalo)
        primeiro_do_intervalo+=1

soma = 0
for item in lista:
    if (item % 2) != 0:
        soma+=item

print(soma)
