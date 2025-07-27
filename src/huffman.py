from utils import (
    parse_args_main,
    parse_args_compress, 
    parse_args_decompress_huffman,
    read_text_file, 
    save_content_to_file, 
    save_huffman_map_to_file,
    get_file_names_huffman,
    read_huffman_map,
    read_binary_file,
    logger,
    WRITING_MODE_COMPRESS,
    WRITING_MODE_DECOMPRESS,
)

from huffman.compress import break_file_content_in_words, create_frequencies_table, create_huffmann_tree, encode, compress
from huffman.decompress import load_compressed_file, decompress_data


def huffman_compress(args=None):
    args = parse_args_compress(args)
    filename = args.file_to_compress_path

    logger.info(f"let's try to compress {filename}")
    file_content = read_text_file(filename)

    words = break_file_content_in_words(file_content)
    frequencies_table = create_frequencies_table(words)
    map_tree = create_huffmann_tree(frequencies_table)
    encoded_content = encode(words, map_tree)
    compressed_content = compress(encoded_content)
    
    filename_compressed_file, filename_map_tree = get_file_names_huffman(filename)

    logger.info(f"saving outputs in {filename_compressed_file} and {filename_map_tree}")
    save_content_to_file(compressed_content, filename_compressed_file, WRITING_MODE_COMPRESS)
    save_huffman_map_to_file(map_tree, filename_map_tree)
    logger.info(f"compression finished!")

def huffman_decompress(args=None):
    args = parse_args_decompress_huffman(args)
    file_path = args.file_path
    map_file_path = args.map_file_path
    output_file_path = args.output_file_path

    data = read_binary_file(file_path)
    compressed_text = load_compressed_file(data)
    huffman_map = read_huffman_map(map_file_path)
    decompressed_data = decompress_data(compressed_text, huffman_map) 
    save_content_to_file(decompressed_data, output_file_path, WRITING_MODE_DECOMPRESS)

if __name__ == "__main__":
    args, remaining_args = parse_args_main()

    if args.step == "compress":
        huffman_compress(remaining_args)
    else:
        huffman_decompress(remaining_args)
