# Crie a função que será avaliada no exercício aqui
def is_anagram(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    else:
        for letra in palavra1:
            if letra not in palavra2:
                return False
        return True

















