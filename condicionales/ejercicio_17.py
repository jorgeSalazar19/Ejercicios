#17. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.

#se captura el dato de entrada y se valida
num = int(input('Ingrese el numero: '))

if num < 100 or num > 999:
    print('El numero no es de 3 digitos')
else:
    first_digit = num%10
    second_digit = int(num/10)%10
    third_digit = int(num/100)%10

    if first_digit > second_digit and first_digit > third_digit:
        print('El mayor digito es el primero')
    else:
        if second_digit > first_digit and second_digit > third_digit:
            print('El mayor digito es el segundo digito')
        else:
            if third_digit > first_digit and third_digit > second_digit:
                print('El mayor digito es el tercer digito')
            else:
                print('Todos los digitos son iguales')