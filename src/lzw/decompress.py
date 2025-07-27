import struct


def load_lzw(file_object):
    """
    Carrega os códigos comprimidos e o alfabeto de um arquivo .lzw.

    Args:
        filename (str): Nome base do arquivo (sem extensão).

    Returns:
        tuple: (codes, alphabet) onde codes é uma lista de inteiros e alphabet é uma lista de caracteres.
    """
    alphabet_len = struct.unpack(">H", file_object.read(2))[0]
    alphabet = list(file_object.read(alphabet_len).decode("utf-8"))
    codes = []

    while chunk := file_object.read(4):
        codes.append(struct.unpack(">I", chunk)[0])
    file_object.close()
    
    return codes, alphabet


def decompress(compressed, alphabet):
    """
    Descomprime uma lista de códigos LZW para o texto original.

    Args:
        compressed (list of int): Lista de códigos LZW comprimidos.
        alphabet (list of str): Alfabeto utilizado na compressão.

    Returns:
        str: Texto descomprimido.
    """
    dictionary = {i: ch for i, ch in enumerate(alphabet)}
    dict_size = len(alphabet)
    w = dictionary[compressed.pop(0)]
    result = [w]
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Bad compressed k: %s" % k)
        result.append(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return ''.join(result)
