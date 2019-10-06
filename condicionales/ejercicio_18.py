#18. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.

#se captura el dato de entrada y se valida
num = int(input('Ingrese el numero: '))

if num < 100 or num > 999:
    print('El numero no es de 3 digitos')
else:
    first_digit = num%10
    second_digit = int(num/10)%10
    third_digit = int(num/100)%10

    if first_digit % second_digit == 0:
        print('El primer y segundo digito son multiplos')
    else:
        if first_digit % third_digit == 0:
            print('El primer y tercer digito son multiplos')
        else:
            if second_digit % third_digit == 0:
                print('El segundo y el tercer digito son multiplos')
            else:
                print('Ninguno de los digitos es multiplo')