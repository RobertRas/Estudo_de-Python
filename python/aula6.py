#crie um programa que leia dois números e mostre a soma entre eles
print ('--------------- Primeiro desafio ----------------')
num1 = int (input('digite o primeiro valor: '))
num2 = int (input('digite o segundo valor: '))
soma = num1 + num2
print ('A soma de {} e {} vale {}'.format(num1, num2, soma))

print ('--------------- Segundo desafio ----------------')
#faça um program que leia algo pelo teclado e mostre na tela o seu tipo primitivo 
#e todas as informações possíveis sobre ele
var = input('digite algo: ')
print(type(var))
print('é numérico?', var.isnumeric())
