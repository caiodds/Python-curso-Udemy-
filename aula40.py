#Calculadora

while True:
    numero_1 = input('Digite um numero')
    numero_2 = input('Digite outro numero')
    operador = input('Digite um operador(+ ou -)')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos numeros digitados não sao validos!')
        continue


    operadores_permitidos = '+-'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador')
        continue


    if operador == '+':
            print(numero_1_float + numero_2_float)
    elif operador == '-':
            print(numero_1_float - numero_2_float)
    else:
         print('Nunca deve chegar aqui')

    sair = input('Deseja sair? [s]Sair: ').lower().startswith('s')
    if sair is True:
         break


    