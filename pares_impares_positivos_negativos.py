##beecrowd | 1066
##---------------------------------------------------------------------------------------

n1, n2, n3, n4, n5 = int(input()), int(input()), int(input()), int(input()), int(input())
all = []
even = odd = positive = negative = 0

all.extend([n1,n2,n3,n4,n5])

for item in all:
    if (item%2) == 0: 
        even+=1 
    else:
        odd+=1
    
    if item > 0:
        positive+=1
    elif item < 0:
        negative+=1

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")