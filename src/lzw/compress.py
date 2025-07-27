import struct


def save_lzw(file_object, codes, alphabet):
    """
    Salva os códigos comprimidos pelo LZW e o alfabeto em um arquivo .lzw.

    Args:
        filename (str): Nome base do arquivo (sem extensão).
        codes (list of int): Lista de códigos LZW a serem salvos.
        alphabet (list of str): Alfabeto utilizado na compressão.
    """
    alphabet_bytes = "".join(alphabet).encode("utf-8")
    alphabet_len = len(alphabet_bytes)
    
    file_object.write(struct.pack(">H", alphabet_len))
    file_object.write(alphabet_bytes)
    for code in codes:
        file_object.write(struct.pack(">I", code))
    
    file_object.close()

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
 


def compress(text, alphabet):
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

