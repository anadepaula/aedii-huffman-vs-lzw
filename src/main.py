from utils import (
    parse_args_main,
    parse_args_compress, 
    parse_args_decompress_huffman,
    parse_args_decompress_lzw,
    get_file_object_to_read_compressed_file,
    get_file_object_to_write_compressed_file,
    get_file_object_to_write_decompressed_file,
    read_text_file, 
    get_file_names_huffman,
    get_file_names_lzw,
    read_binary_file,
    logger,
)

from huffman import (
    compress as huffman_compress,
    decompress as huffman_decompress,
    save_huffman_map_to_file,
    save_huffman_compressed,
    read_huffman_map,
    save_decompressed_data,
)
from lzw import (
    compress as lzw_compress,
    decompress as lzw_decompress,
    load_lzw,
    save_decompressed_data,
    save_lzw
)


def huffman_compress_cli(args=None):
    args = parse_args_compress(args)
    filename = args.file_to_compress_path

    file_content = read_text_file(filename)

    compressed_content, map_tree = huffman_compress(file_content)
    
    filename_compressed_file, filename_map_tree = get_file_names_huffman(filename)

    file_object_compressed_file = get_file_object_to_write_compressed_file(
        filename_compressed_file
    )
    file_object_map_tree = get_file_object_to_write_compressed_file(
        filename_map_tree
    )

    save_huffman_compressed(compressed_content, file_object_compressed_file)
    save_huffman_map_to_file(map_tree, file_object_map_tree)

    return filename_compressed_file, filename_map_tree

def huffman_decompress_cli(args=None):
    args = parse_args_decompress_huffman(args)
    file_path = args.file_path
    map_file_path = args.map_file_path
    output_file_path = args.output_file_path

    data = read_binary_file(file_path)
    huffman_map_file_object = get_file_object_to_read_compressed_file(map_file_path)
    huffman_map = read_huffman_map(huffman_map_file_object)
    
    decompressed_data = huffman_decompress(data, huffman_map)

    file_object_decompressed_file = get_file_object_to_write_decompressed_file(
        output_file_path
    )
    save_decompressed_data(decompressed_data, file_object_decompressed_file)

    return output_file_path

def lzw_compress_cli(args=None):
    args = parse_args_compress(args)
    filename = args.file_to_compress_path

    file_content = read_text_file(filename)

    compressed_content, alphabet = lzw_compress(file_content)
    
    filename_compressed_file = get_file_names_lzw(filename)
    file_object_compressed_file = get_file_object_to_write_compressed_file(
        filename_compressed_file
    )
    save_lzw(
        file_object_compressed_file,
        compressed_content,
        alphabet
    )

    return filename_compressed_file

def lzw_decompress_cli(args=None):
    args = parse_args_decompress_lzw(args)
    file_path = args.file_path
    output_file_path = args.output_file_path

    file_object_compressed_file = get_file_object_to_read_compressed_file(file_path)

    loaded_codes, loaded_alphabet = load_lzw(file_object_compressed_file)
    decompressed = lzw_decompress(loaded_codes, loaded_alphabet)
    file_object_decompressed_file = get_file_object_to_write_decompressed_file(
        output_file_path
    )
    save_decompressed_data(decompressed, file_object_decompressed_file)

    return output_file_path


if __name__ == "__main__":
    args, remaining_args = parse_args_main()

    step = args.step
    algorithm = args.algorithm

    if step == "compress" and algorithm == "huffman":
        action = huffman_compress_cli
    elif step == "compress" and algorithm == "lzw":
        action = lzw_compress_cli
    elif step == "decompress" and algorithm == "huffman":
        action = huffman_decompress_cli
    elif step == "decompress" and algorithm == "lzw":
        action = lzw_decompress_cli
    else:
        raise Exception(f"case unmapped, args {args} remaining args {remaining_args}")

    action(remaining_args)