# 19. Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.

#se captura el dato de entrada y se valida
num = int(input('Ingrese el primer numero: '))
num_2 = int(input('Ingrese el segundo numero: '))

if num < 100 or num > 999:
    print('El primer numero no es de 3 digitos')
else:
    if num_2 < 100 or num_2 > 999:
        print('El segundo numero no es de 3 digitos')
    else:
        if num > num_2:
            num_2 = int(input('Ingrese el tercer numero: '))

            if num_2 < 100 or num_2 > 999:
                print('El tercer numero no es de 3 digitos')
            else:
                if num > num_2:
                    print('El primer numero ingresado es el mayor')
                else:
                    print('El tercer numero ingresado es el mayor')
        else:
            num = int(input('Ingrese el tercer numero: '))

            if num < 100 or num > 999:
                print('El tercer numero no es de 3 digitos')
            else:
                if num_2 > num:
                    print('El segundo numero ingresado es el mayor')
                else:
                    print('el tercer numero es el mayor')