from huffman.compress import (
    create_frequencies_table,
    create_huffmann_tree,
    encode,
    compress_data,
)
from huffman.decompress import (
    load_compressed_file,
    decompress_data,
)


def compress(file_content):
    frequencies_table = create_frequencies_table(file_content)
    map_tree = create_huffmann_tree(frequencies_table)
    encoded_content = encode(file_content, map_tree)
    compressed_content = compress_data(encoded_content)

    return compressed_content, map_tree    

def decompress(data, huffman_map):
    compressed_text = load_compressed_file(data)
    decompressed_data = decompress_data(compressed_text, huffman_map) 

    return decompressed_data