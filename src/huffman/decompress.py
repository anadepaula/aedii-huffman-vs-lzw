def load_compressed_file(data):

    padding = data[0]
    bit_string = ""

    for byte in data[1:]:
        bit_string += f'{byte:08b}'
    
    return bit_string[:-padding]

def decompress_data(compressed_text, huffman_map):
    huffman_reverse_map = {v: k for k, v in huffman_map.items()}
    decoded_text = ""
    current_bit = "" 
    for bit in compressed_text:
        current_bit += bit
        if current_bit in huffman_reverse_map:
            decoded_text += huffman_reverse_map[current_bit]
            current_bit = ""
    return decoded_text

