#Soma de números pares
#Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
n = int(input('digite um numero inteiro positivo e par:'))
lista = list(range(2,n,2))
s1 = 0
for i in lista:
    L = []
    L.append(i)
    s1 = s1+ i   
    s=sum(L)  
    print(s,s1)
