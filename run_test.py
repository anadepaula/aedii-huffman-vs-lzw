import os
import time
import huffman_compress as hc
import lzw_compression as lzw

def main():
    original_size = [] #guarda o tamanho original dos arquivos que serão comprimido
    compress_size = [] #guarda o caminho/nome do arquivo
    compress_ratio = [] #guarda a taxa de compressão dos arquivos, ou seja, quantos % o arquivo foi reduzido em relação ao tamanho original
    result_time = [] #guarda o tempo que o algoritmos de HUffman e de LZW levaram para comprimir os arquivos

    #esse for refere-se aos testes de compressão utilizando os algoritmos de huffman
    for i in range(1, 4):
        filename = f"test{i}" # f"test{i}" formata o nome do arquivo para test1, test2, test3
        start_time = time.time() 
        hc.huffman_compress(filename) #chama o algoritmo de huffman para realizar a compressão dos arquivos testes
        end_time = time.time()
        result_time.append(end_time - start_time) #adiciona à lista result_time o tempo total gasto para comprimir
        original_size.append(os.path.getsize(filename + ".txt")) #adiciona à lista original_size o tamanho do arquivo original
        compress_size.append(os.path.getsize(f"{filename}.huff")) #adiciona à lista compress_size o tamanho do arquivo  comprimido. Lembrando que no algoritmo de huffman nomeamos a extensão do arquivo comprimido como '.huff'
        compress_ratio.append((original_size[i-1] - compress_size[i-1]) / original_size[i-1] * 100) #adiciona à lista compress_ratio o valor da taxa de compressão.

    #esse for refere-se aos testes de compressão utilizando os algoritmos de LZW
    for i in range(4, 7):
        filename = f"test{i-3}"
        start_time = time.time()
        lzw.lzw_compress(filename) #chama o algoritmo de lzw para realizar a compressão dos arquivos testes
        end_time = time.time()
        result_time.append(end_time - start_time)
        original_size.append(os.path.getsize(filename + ".txt"))
        compress_size.append(os.path.getsize(f"{filename}.lzw"))
        compress_ratio.append((original_size[i-1] - compress_size[i-1]) / original_size[i-1] * 100)

    #Imprime os resultados de cada um dos testes
    for i in range(0, 6):
        if(i == 0):
            print("----------Algoritmo de Huffman----------")
        elif(i==3):
            print("----------Algoritmo de LZW----------")
        print(f"Teste {i+1}:")
        print(f"Tamanho original: {original_size[i]} bytes")
        print(f"Tamanho comprimido: {compress_size[i]} bytes")
        print(f"Taxa de compressão: {compress_ratio[i]:.2f}%")
        print(f"Tempo de execução: {result_time[i]:.2f} segundos\n")

if __name__ == "__main__":
    main()

