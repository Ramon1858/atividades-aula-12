#tabuada de multiplicação
#Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
def tabuada():
    n = int(input('digite um numero até 10:'))
    for i in range(0,11):
        c = n * i
        print(n,'x',i,'=',c)
tabuada()