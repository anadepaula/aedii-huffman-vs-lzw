import pickle
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import argparse

def load_compressed_file(input_path):
    with open(input_path, 'rb') as f:
        data = f.read()
    padding = data[0]
    bit_string = ""
    for byte in data[1:]:
        bit_string += f'{byte:08b}'
    return bit_string[:-padding]

def load_map(map_path):
    with open(map_path, 'rb') as f:
        return pickle.load(f)
    
def descompress_data(compressed_text, huffman_map):
    huffman_reverse_map = {v: k for k, v in huffman_map.items()}
    decoded_text = ""
    current_bit = "" 
    for bit in compressed_text:
        current_bit += bit
        if current_bit in huffman_reverse_map:
            decoded_text += huffman_reverse_map[current_bit]
            current_bit = ""
    return decoded_text

def save_decoded_text(decoded_text, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decoded_text)
    except Exception as e:
        print(f"an exception occured while trying to save the decompressed file to {output_file}: {e}")
        raise e

def decompress(compressed_file_path, map_file_path, decompressed_file_path):
    compressed_text = load_compressed_file(compressed_file_path)
    huffman_map = load_map(map_file_path)
    decoded_text = descompress_data(compressed_text, huffman_map) 
    save_decoded_text(decoded_text, decompressed_file_path)

def main():



    Tk().withdraw() 
    input_path = askopenfilename() 
    Tk().withdraw() 
    map_path = askopenfilename() 
    compressed_text = load_compressed_file(input_path)
    huffman_map = load_map(map_path)
    decoded_text = descompress_data(compressed_text, huffman_map) 
    input_path_without_extension = input_path.rsplit(".", 1)[0]
    output_path = f"{input_path_without_extension}_decompressed.txt"
    save_decoded_text(decoded_text, output_path)
    
if __name__ == "__main__":
    main()

