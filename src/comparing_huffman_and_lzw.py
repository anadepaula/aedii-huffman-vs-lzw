import os
import time

from utils import (
    # parse_args_main,
    # parse_args_compress, 
    # parse_args_decompress_huffman,
    # parse_args_decompress_lzw,
    # get_file_object_to_read_compressed_file,
    # get_file_object_to_write_compressed_file,
    # get_file_object_to_write_decompressed_file,
    read_text_file, 
    get_file_names_huffman,
    get_file_names_lzw,
    read_binary_file,
    logger,

)

from main import (
    huffman_compress_cli,
    huffman_decompress_cli,
    lzw_compress_cli,
    lzw_decompress_cli,
)

def get_size_of_file(file):
    return os.path.getsize(file)

def bob(file):
    file_content = read_text_file(file)
    file_size = get_size_of_file(file)

    start_time = time.time() 
    filename_huffman_compressed_file, filename_huffman_map_tree = huffman_compress_cli([file])
    end_time = time.time()
    huffman_compressing_time = end_time - start_time
    huffman_compressed_file_size = get_size_of_file(filename_huffman_compressed_file)
    huffman_map_tree_size = get_size_of_file(filename_huffman_map_tree)
    compression_rate_huffman = ((file_size - (huffman_compressed_file_size + huffman_map_tree_size)) / file_size)
    logger.info(f"huffman: {huffman_compressing_time} ({file_size}, {huffman_compressed_file_size+huffman_map_tree_size}) {compression_rate_huffman}")

    start_time = time.time() 
    filename_lzw_compressed_file = lzw_compress_cli(file_content)
    end_time = time.time()
    lzw_compressing_time = end_time - start_time
    lzw_compressed_file_size = get_size_of_file(filename_lzw_compressed_file)
    compression_rate_lzw = (file_size - (lzw_compressed_file_size)) / file_size
    logger.info(f"lzw: {lzw_compressing_time} ({file_size}, {lzw_compressed_file_size}) {compression_rate_lzw}")

dna_file = "test2.txt"
bob(dna_file)