'''
    ¿ES UN ANAGRAMA?

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.

'''

def anagrama(palabra1, palabra2):
    length = len(palabra1)
    i = 0
    for index in palabra1:
        for index2 in palabra2:
            if index == index2:
                i = i + 1
    if i == length:
        print(True)
    else:
        print(False)

anagrama("amor", "roma")