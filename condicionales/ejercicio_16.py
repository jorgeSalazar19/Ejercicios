#16. Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son iguales.

#se captura el dato de entrada y se valida
num = int(input('Ingrese el numero: '))

if num < 100 or num > 999:
    print('El numero no es de 3 digitos')
else:
    if num%10 == int(num/10)%10 or num%10 == int(num/100)%10:
        print('Dos de los digitos del numero son iguales')
    else:
        if int(num/10)%10 == int(num/100)%10:
            print('Dos de los digitos del numero son iguales')
        else:
            print('No tiene digitos comunes')