frase = 'Um teste para o trabalho do Trabalho '



i = 0
apareceu_mais_vezes= 0
letra_que_apareceu_mais_vezes= ''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i += 1
        continue
    vezes_letra_apareceu = frase.count(letra_atual)
     
    if apareceu_mais_vezes < vezes_letra_apareceu:
        apareceu_mais_vezes = vezes_letra_apareceu
        letra_que_apareceu_mais_vezes= letra_atual
    print(letra_atual, vezes_letra_apareceu)
    i+= 1

print('á letra que apareceu  mais vezes foi 'f'"{letra_que_apareceu_mais_vezes}"', f'{apareceu_mais_vezes}"Vezes*"')