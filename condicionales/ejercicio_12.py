# 12. Leer dos números enteros de dos dígitos y determinar si tienen dígitos comunes.

#se capturan los datos de entrada y validan los datos de entrada.
first_num = int(input('Ingrese el primer numero: '))
if first_num < 10 or first_num > 99:
    print('El primer numero no es de dos digitos')

second_num = int(input('Ingrese el segundo numero: '))   
if second_num < 10 or second_num > 99:
    print('El segundo numero no es de dos digitos')

#se extraen los digitos
first_num_first_digit = first_num%10
first_num_second_digit = int(first_num/10)%10
second_num_first_digit = second_num%10
second_num_second_digit = int(second_num/10)%10


if first_num_first_digit == second_num_first_digit or first_num_first_digit == second_num_second_digit:
    print('Los dos numeros tienen digitos comunes')

else:
    if first_num_second_digit == second_num_first_digit or first_num_second_digit == second_num_second_digit:
        print('Los dos numeros tienen digitos comunes')
    else:
        print('No tienen digitos comunes')