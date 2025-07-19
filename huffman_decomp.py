import pickle
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename


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

def save_decoded_text(decoded_text):
    root = Tk()
    root.withdraw()
    folder = filedialog.askdirectory() 
    with open(folder + "/texto_descomprimido.txt", 'w', encoding='utf-8') as f:
        f.write(decoded_text)

def main():

    Tk().withdraw() 
    input_path = askopenfilename() 
    Tk().withdraw() 
    map_path = askopenfilename() 
    compressed_text = load_compressed_file(input_path)
    huffman_map = load_map(map_path)
    decoded_text = descompress_data(compressed_text, huffman_map) 
    save_decoded_text(decoded_text)
    
if __name__ == "__main__":
    main()

