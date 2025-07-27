from utils import (
    parse_args_main,
    parse_args_compress, 
    parse_args_decompress_huffman,
    get_file_object_to_read_compressed_file,
    get_file_object_to_write_compressed_file,
    get_file_object_to_write_decompressed_file,
    read_text_file, 
    get_file_names_huffman,
    read_binary_file,
    logger,
)

from huffman import (
    compress,
    decompress,
    save_huffman_map_to_file,
    save_huffman_compressed,
    read_huffman_map,
    save_decompressed_data,
)


def huffman_compress(args=None):
    args = parse_args_compress(args)
    filename = args.file_to_compress_path

    logger.info(f"let's try to compress {filename}")
    file_content = read_text_file(filename)

    compressed_content, map_tree = compress(file_content)
    
    filename_compressed_file, filename_map_tree = get_file_names_huffman(filename)

    logger.info(f"saving outputs in {filename_compressed_file} and {filename_map_tree}")
    file_object_compressed_file = get_file_object_to_write_compressed_file(
        filename_compressed_file
    )
    file_object_map_tree = get_file_object_to_write_compressed_file(
        filename_map_tree
    )

    save_huffman_compressed(compressed_content, file_object_compressed_file)
    save_huffman_map_to_file(map_tree, file_object_map_tree)
    logger.info(f"compression finished!")

def huffman_decompress(args=None):
    args = parse_args_decompress_huffman(args)
    file_path = args.file_path
    map_file_path = args.map_file_path
    output_file_path = args.output_file_path

    data = read_binary_file(file_path)
    huffman_map_file_object = get_file_object_to_read_compressed_file(map_file_path)
    huffman_map = read_huffman_map(huffman_map_file_object)
    
    decompressed_data = decompress(data, huffman_map)

    file_object_decompressed_file = get_file_object_to_write_decompressed_file(
        output_file_path
    )
    save_decompressed_data(decompressed_data, file_object_decompressed_file)


if __name__ == "__main__":
    args, remaining_args = parse_args_main()
    logger.info(args)
    logger.info(remaining_args)

    step = args.step
    algorithm = args.algorithm

    if step == "compress" and algorithm == "huffman":
        action = huffman_compress
    # elif is_compress and algorithm == "lzw":
    #     action = lzw_compress
    elif step == "decompress" and algorithm == "huffmann":
        action = huffman_decompress
    else:
        raise Exception("case unmapped")
    # elif not is_compress and algorithm == "lzw":
    #     action = lzw_decompress

    action(remaining_args)