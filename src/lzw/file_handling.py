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

def save_decompressed_data(content, file_object):
    file_object.write(content)
    file_object.close()
