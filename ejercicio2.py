
num1=0
num2=0
opc=0
resultado=0
print('---operaciones aritmeticas---')
num1=int(input('Ingrese el primer numero: '))
num2=int(input('Ingrese el segundo numero: '))
print('---menu de operaciones---')
print('1. sumar numeros')
print('2. restar numeros')
print('3. nultiplicar numeros')
print('4. dividir numeros')
opc=int(input('Digite la operacion a realizar: '))


def operaciones(num1,num2):
  if opc == 1:
    resultado= num1 + num2
  print(resultado)
operaciones(num1,num2)