import heapq
import pickle
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

class Node(object):
    """
    Classe que representa um nó da árvore de Huffman.

    Attributes:
        char (str): Caractere representado pelo nó.
        val (int): Frequência do caractere.
        left (Node): Filho à esquerda.
        right (Node): Filho à direita.
    """
    def __init__(self, char, val):
        """
        Inicializa um nó da árvore de Huffman.

        Args:
            char (str): Caractere representado pelo nó.
            val (int): Frequência do caractere.
        """
        self.val = val
        self.char = char
        self.left = None
        self.right = None

   
    def __lt__(self, other):
        """
        Compara dois nós com base em sua frequência para uso em heap.

        Args:
            other (Node): Outro nó para comparação.
        Returns:
            bool: True se a frequência deste nó for menor que a do outro.
        """
        return self.val < other.val
    
def save_compress_file(text_cod, map):
    data = bytearray()
    padding = 8 - len(text_cod) % 8
    text_cod += '0' * padding
    data.append(padding)
    for i in range (0, len(text_cod), 8):
        byte = text_cod[i:i+8]
        data.append(int(byte, 2))
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory() 
    with open(folder + "/texto_comprimido.huff", 'wb') as f:
        f.write(data)
    with open(folder + "/huffman_map.huffmap", 'wb') as f:
        pickle.dump(map, f)
 
def codificar_texto(texto, huffman_dic):
    """
    Codifica o texto usando o dicionário de Huffman.

    Args:
        texto (str): Texto a ser codificado.
        huffman_dic (dict):
    """

    new_text = ""
    for i in texto:
        new_text += huffman_dic[i]
    return new_text




def cria_huffman_coding(node: Node, huffman_dic, code):
    """
    Cria um dicionário com a codificação de cada símbolo a partir de uma árvore de Huffman.

    Args:
        node (Node): Nó da árvore de Huffman.
        huffman_dic (dict): Dicionário onde é adicionado o par (símbolo, código) quando encontramos um nó folha.
        code (str): Código formado pelo trajeto percorrido.
    Returns:
        None
    """
    if node == None:
        return
    
    if node.left == None and node.right == None:
        huffman_dic[node.char] = code
    
    cria_huffman_coding(node.left, huffman_dic, code + '0')
    cria_huffman_coding(node.right, huffman_dic, code + '1')


   
def criar_arvore_huffman(freq_table):
    """
    Cria a árvore de Huffman a partir da tabela de frequência e imprime o dicionário de codificação.

    Args:
        freq_table (dict): Tabela de frequência dos caracteres.
    Returns:
        None
    """
    tree = []
    
    for key,val in freq_table.items():
        heapq.heappush(tree, Node(key,val))
    heapq.heapify(tree)


    while len(tree) >= 2:

        l = heapq.heappop(tree)
        r = heapq.heappop(tree)

        newNode = Node(None, l.val + r.val)
        newNode.left = l
        newNode.right = r

        heapq.heappush(tree, newNode)

    raiz = heapq.heappop(tree)
    huffman_dic = {}
    cria_huffman_coding(raiz, huffman_dic, "")
    return huffman_dic


def criar_tabela_freq(texto):
    """
    Cria uma tabela de frequência dos caracteres presentes no texto.

    Args:
        texto (str): Texto para análise de frequência.
    Returns:
        dict: Tabela de frequência dos caracteres.
    """
    freq = {}
   
    for i in texto:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] = freq[i] + 1
   
    return freq
   
   
def abrir_arquivo():
    """
    Abre um arquivo .txt e retorna o texto contido nele.

    Returns:
        str: Texto contido no arquivo.
    """
    Tk().withdraw() 
    filename = askopenfilename() 
    f = open(filename, 'r', encoding='utf-8')
    texto = f.read()
    return texto
 


def main():
    """
    Função principal que executa o processo de leitura do arquivo, criação da tabela de frequência e da árvore de Huffman.
    """
    text = abrir_arquivo()
    freq_table = criar_tabela_freq(text)
    huff_dic = criar_arvore_huffman(freq_table)
    codificado = codificar_texto(text, huff_dic)
    save_compress_file(codificado, huff_dic)
if __name__ == "__main__":
    main()


