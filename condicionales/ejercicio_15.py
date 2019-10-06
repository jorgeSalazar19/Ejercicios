#15. Leer un número entero de tres dígitos y determinar a cuánto es igual la suma de sus dígitos.

#se captura el dato de entrada y se valida
num = int(input('Ingrese el numero: '))

if num < 100 or num > 999:
    print('El numero no es de 3 digitos')
else:
    sum = num%10 + int(num/10)%10 + int(num/100)%10
    print('La suma de los digitos del numero es: ', sum)