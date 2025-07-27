Este projeto consiste numa análise comparada 
de dois algoritmos de compressão:

* Algoritmo de compressão de Huffmann

* Algoritmo de compressão de LZW (Lempel-Ziv-Welch) 

O desenvolvimento do projeto deu-se na disciplina 
MCCC002-23 Algoritmos e Estruturas de Dados II, 
vinculada ao Bacharelado em Ciência da Computação 
da Universidade Federal do ABC 
sob orientação do Prof. Dr. Carlo Kleber da Silva Rodrigues 
durante o segundo quadrimestre de 2025. 

## Como usar

## compressão usando huffman

`python src/huffman.py compress test2.txt`
Serão criados 2 arquivos: `test2.huff` e `test2.huffmap` 


`python src/huffman.py decompress test4.huff test4.huffmap test4_decoded.txt`
O arquivo `test4.huff` será descomprimido usando o mapa de `test4.huffmap`, e o resultado será salvo em `test4_decoded.txt`