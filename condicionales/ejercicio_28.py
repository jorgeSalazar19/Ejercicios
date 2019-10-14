try:
    num = int(input('Ingrese un numero de 5 digitos: '))

    if int(num / 10000) == 0 or num > 99999:
        print ('El numero no es de 5 digitos')
    else:
        digit_firts= num%10
        digit_second= int(num/10)%10
        digit_four= int(num/1000)%10
        digit_five= int(num/10000)%10

        if (digit_firts == digit_five) and (digit_second == digit_four):
            print('El numero es capicúo')
        else:
            print('El numero no es capicúo')
except Exception as error:
    print('error')