from utils import (
    parse_args_main,
    parse_args_compress, 
    parse_args_decompress_lzw,
    read_text_file, 
    save_decompressed_content_to_file, 
    get_file_names_lzw,
    get_file_object_to_write_lzw_compressed_file,
    get_file_object_to_read_lzw_compressed_file,
    logger,
)

from lzw.compress import create_alphabet, compress, save_lzw
from lzw.decompress import load_lzw, decompress


def lzw_compress(args=None):
    args = parse_args_compress(args)
    filename = args.file_to_compress_path

    logger.info(f"let's try to compress {filename}")
    file_content = read_text_file(filename)

    alphabet = create_alphabet(file_content)
    compressed_content = compress(file_content, alphabet)
    
    filename_compressed_file = get_file_names_lzw(filename)
    logger.info(f"saving outputs in {filename_compressed_file}")
    file_object_compressed_file = get_file_object_to_write_lzw_compressed_file(
        filename_compressed_file
    )
    save_lzw(
        file_object_compressed_file,
        compressed_content,
        alphabet
    )
    logger.info(f"compression finished!")

def lzw_decompress(args=None):
    args = parse_args_decompress_lzw(args)
    file_path = args.file_path
    output_file_path = args.output_file_path

    file_object_compressed_file = get_file_object_to_read_lzw_compressed_file(file_path)

    loaded_codes, loaded_alphabet = load_lzw(file_object_compressed_file)
    decompressed = decompress(loaded_codes, loaded_alphabet)

    save_decompressed_content_to_file(decompressed, output_file_path)

if __name__ == "__main__":
    args, remaining_args = parse_args_main()
    logger.info(args)

    is_compress = args.step == "compress"

    if is_compress:
        lzw_compress(remaining_args)
    else:
        lzw_decompress(remaining_args)
