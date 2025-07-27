import heapq


def create_frequencies_table(text):
    """
    Cria uma tabela de frequência dos caracteres presentes no texto.

    Args:
        texto (str): Texto para análise de frequência.
    Returns:
        dict: Tabela de frequência dos caracteres.
    """
    frequencies_table = {}
   
    for word in text:
        if not frequencies_table.get(word):
            frequencies_table[word] = 1
        else:
            frequencies_table[word] += 1
   
    return frequencies_table
   

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
    
def create_huffmann_coding(node: Node, huffman_dic, code):
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
    
    create_huffmann_coding(node.left, huffman_dic, code + '0')
    create_huffmann_coding(node.right, huffman_dic, code + '1')


def create_huffmann_tree(freq_table):
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
    create_huffmann_coding(raiz, huffman_dic, "")
    return huffman_dic

def encode(texto, huffman_dic):
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

def compress_data(encoded_content):
    data = bytearray()
    padding = 8 - len(encoded_content) % 8
    encoded_content += '0' * padding
    data.append(padding)
    for i in range (0, len(encoded_content), 8):
        byte = encoded_content[i:i+8]
        data.append(int(byte, 2))
    
    
    return data

