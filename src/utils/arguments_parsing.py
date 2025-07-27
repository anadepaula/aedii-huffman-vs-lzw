import os
import argparse

from .types import (
    HUFFMANN_COMPRESSED_FILE_EXTENSION,
    HUFFMANN_MAP_EXTENSION,
    LZW_COMPRESSED_FILE_EXTENSION,
)
from .logging import logger


def validate_inputted_file(filename, extension=None):
    if extension:
        if not filename.endswith(extension):
            return False
    
    try:
        assert os.path.exists(filename)
    except AssertionError as e:
        logger.error(f"flie {filename} doesn't exist")
        raise FileNotFoundError(filename)
    except Exception as e:
        logger.error(f"something happened while trying to open file {filename}: {e}")
        raise e

    return filename
    
def validate_file_to_compress(filename):
    return validate_inputted_file(
        filename,
    )

def validate_lzw_compressed_file(filename):
    return validate_inputted_file(
        filename, 
        LZW_COMPRESSED_FILE_EXTENSION,
    )

def validate_huffman_compressed_file(filename):
    return validate_inputted_file(
        filename, 
        HUFFMANN_COMPRESSED_FILE_EXTENSION,
    )

def validate_compression_map_file(filename):
    return validate_inputted_file(
        filename, 
        HUFFMANN_MAP_EXTENSION,
    )

def parse_args_compress(args=None):
    parser = argparse.ArgumentParser(
        description=('utility to compress files.')
    )
    parser.add_argument(
        'file_to_compress_path',
        type=validate_file_to_compress,
        help = 'path to file to compress'
    )

    parsed_args = parser.parse_args(args)
    return parsed_args

def parse_args_decompress_lzw(args=None):
    logger.info(args)
    parser = argparse.ArgumentParser(
        description=('utility to compress files compressed using lzw algorithm')
    )
    parser.add_argument(
        'file_path',
        type=validate_lzw_compressed_file,
        help = 'filename of .huff file containing the compressed file.'
    )
    parser.add_argument(
        'output_file_path', 
        help = 'filename of to use to save decompressed file.'
    )

    parsed_args = parser.parse_args(args)
    logger.info(parsed_args)
    return parsed_args

def parse_args_decompress_huffman(args=None):
    parser = argparse.ArgumentParser(
        description=('utility to compress files compressed using huffman algorithm')
    )
    parser.add_argument(
        'file_path',
        type=validate_huffman_compressed_file,
        help = 'filename of .huff file containing the compressed file.'
    )
    parser.add_argument(
        'map_file_path', 
        type=validate_compression_map_file,
        help = 'filename of .huffmap file containing the huffton map.'
    )
    parser.add_argument(
        'output_file_path', 
        help = 'filename of to use to save decompressed file.'
    )

    parsed_args = parser.parse_args(args)
    return parsed_args

def parse_args_main():
    parser = argparse.ArgumentParser(
        description=('utility to compress files compressed using huffman algorithm')
    )
    parser.add_argument(
        'step',
        choices=("compress", "decompress"),
        help = 'step to perform'
    )
    parser.add_argument(
        'algorithm',
        choices=("huffman", "lzw"),
        help = 'algorithm to use to compress or decompress'
    )

    args, remaining_args = parser.parse_known_args()
    return args, remaining_args
