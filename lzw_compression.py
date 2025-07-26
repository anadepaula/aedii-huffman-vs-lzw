from io import StringIO
import struct
from tkinter import Tk
from tkinter.filedialog import askopenfilename
    
def save_lzw(filename, codes, alphabet):
    """
    Salva os códigos comprimidos pelo LZW e o alfabeto em um arquivo .lzw.

    Args:
        filename (str): Nome base do arquivo (sem extensão).
        codes (list of int): Lista de códigos LZW a serem salvos.
        alphabet (list of str): Alfabeto utilizado na compressão.
    """
    alphabet_bytes = "".join(alphabet).encode("utf-8")
    alphabet_len = len(alphabet_bytes)
    with open(filename + ".lzw", "wb") as f:
        f.write(struct.pack(">H", alphabet_len))
        f.write(alphabet_bytes)
        for code in codes:
            f.write(struct.pack(">I", code))

def load_lzw(filename):
    """
    Carrega os códigos comprimidos e o alfabeto de um arquivo .lzw.

    Args:
        filename (str): Nome base do arquivo (sem extensão).

    Returns:
        tuple: (codes, alphabet) onde codes é uma lista de inteiros e alphabet é uma lista de caracteres.
    """
    with open(filename + ".lzw", "rb") as f:
        alphabet_len = struct.unpack(">H", f.read(2))[0]
        alphabet = list(f.read(alphabet_len).decode("utf-8"))
        codes = []
        while chunk := f.read(4):
            codes.append(struct.unpack(">I", chunk)[0])
    return codes, alphabet

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
    print(dictionary)
    return result

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
 

def abrir_arquivo2(filename):
    """
    Abre um arquivo .txt e retorna o texto contido nele.

    Args:
        filename (str): Caminho do arquivo.

    Returns:
        str: Texto contido no arquivo.
    """

    f = open(filename, 'r', encoding='utf-8')
    texto = f.read()
    return texto
 
def lzw_compress(filename):
    """
    Executa o processo de compressão de um arquivo usando o algoritmo LZW.

    Args:
        filename (str): Caminho do arquivo a ser comprimido (sem extensão).

    Returns:
        None
    """
    texto = abrir_arquivo2(filename + ".txt")
    alphabet = create_alphabet(texto)
    codificado = compress(texto, alphabet)
    save_lzw(filename, codificado, alphabet)


def main():
    """
    Função principal para testar a compressão e descompressão LZW.

    Lê um arquivo, comprime, salva, carrega e descomprime o conteúdo.
    """

    #--------Exemplo de compressão de um único arquivo---------------
    # text = abrir_arquivo2("test1.txt")
    # alphabet = create_alphabet(text)
    #r = compress(text, alphabet)
    # save_lzw("compressed.lzw", r, alphabet)

    #------- Exemplo básico do algoritmo LZW. Descomentar e executar para visualizar o funcionamento------
    # text = "abcab"
    # alphabet = create_alphabet(text)
    # r = compress(text, alphabet)
    # print(text)
    # print(alphabet)
    # print(r)
    #-------------------------------------------------------------------------------------------------------

    #----------Exemplo de descompressão de um arquivo-------------------------------------------------------
    # loaded_codes, loaded_alphabet = load_lzw("test1")
    # decompressed = decompress(loaded_codes, loaded_alphabet)
    # print("Texto original:", decompressed)

if __name__ == "__main__":
    main()
