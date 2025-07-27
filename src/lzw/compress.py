import struct


def create_alphabet(text):
    """
    Cria uma lista ordenada de caracteres únicos (alfabeto) a partir do texto de entrada.

    Args:
        text (str): Texto de entrada.

    Returns:
        list of str: Alfabeto ordenado.
    """
    alphabet = sorted(set(text))
    return  alphabet
 


def compress_text(text, alphabet):
    """
    Comprime o texto de entrada usando o algoritmo LZW.

    Args:
        text (str): Texto a ser comprimido.
        alphabet (list of str): Alfabeto para o dicionário inicial.

    Returns:
        list of int: Lista de códigos LZW comprimidos.
    """
    dictionary = {ch: i for i, ch in enumerate(alphabet)}
    dict_size = len(alphabet) 
    w = ""
    result = []
    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])

    return result

