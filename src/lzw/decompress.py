def decompress_text(compressed, alphabet):
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
