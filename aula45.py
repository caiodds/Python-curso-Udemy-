#como funciona o for

texto = 'Caio'
iterator = iter(texto)

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break