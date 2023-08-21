# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(texto):
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem









