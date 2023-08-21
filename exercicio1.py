# Crie a função que será avaliada no exercício aqui
texto = input('Digite um texto: ')
def conta_palavras_unicas():
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem
print(conta_palavras_unicas())










