#Atividade Udemy Python

entrada = input('digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int %2 == 0
    par_impar_texto = 'ímpar'
    if par_impar:
        par_impar_texto = 'par'

    print(f'o numero {entrada_int} é {par_impar_texto}')
else:
    print('Voce nao digitou um numero inteiro')