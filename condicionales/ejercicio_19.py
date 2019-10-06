# 19. Leer tres números enteros y determinar cuál es el mayor. Usar solamente dos variables.

#se captura el dato de entrada y se valida
num = int(input('Ingrese el primer numero: '))
num_2 = int(input('Ingrese el segundo numero: '))

if num > num_2:
    num_2 = int(input('Ingrese el tercer numero: '))

    if num > num_2:
        print('El primer numero ingresado es el mayor')
    else:
        print('El tercer numero ingresado es el mayor')
else:
    num = int(input('Ingrese el tercer numero: '))

    if num_2 > num:
        print('El segundo numero ingresado es el mayor')
    else:
        print('el tercer numero es el mayor')