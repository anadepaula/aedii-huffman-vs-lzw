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

### compressão usando huffman

`python src/main.py compress huffman data/example.fna`
Serão criados 2 arquivos: `data/example.huff` e `data/example.huffmap` 

### descompressão usando huffman

`python src/main.py decompress huffman data/example.huff data/example.huffmap data/decomp_huff_example.fna`
O arquivo descomprimido será salvo em `data/decomp_huff_example.fna`

### compressão usando lzw

`python src/main.py compress lzw data/example.fna`
O aarquivo será salvo em `data/example.lzw`

### descompressão usando lzw

`python src/main.py decompress lzw data/example.lzw data/decomp_lzw_example.fna`
O arquivo descomprimido será salvo em `data/decomp_lzw_example.fna`
