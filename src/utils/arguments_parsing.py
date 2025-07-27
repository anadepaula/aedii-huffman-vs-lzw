import os
import argparse

from .types import (
    HUFFMANN_COMPRESSED_FILE_EXTENSION,
    HUFFMANN_MAP_EXTENSION,
)
from .logging import logger


def validate_inputted_file(filename, extension=None):
    if extension:
        assert filename.endswith(extension)
    
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

def validate_compressed_file(filename):
    return validate_inputted_file(
        filename, 
        HUFFMANN_COMPRESSED_FILE_EXTENSION,
    )

def validate_compression_map_file(filename):
    return validate_inputted_file(
        filename, 
        HUFFMANN_MAP_EXTENSION,
    )

def parse_args_compress_huffman():
    parser = argparse.ArgumentParser(
        description=('utility to decompress files compressed using huffman algorithm')
    )
    parser.add_argument(
        'file_to_compress_path',
        type=validate_file_to_compress,
        help = 'filename of file to compress using huffman algorithm'
    )

    args = parser.parse_args()
    return args

def parse_args_decompress_huffman():
    parser = argparse.ArgumentParser(
        description=('utility to compress files compressed using huffman algorithm')
    )
    parser.add_argument(
        'file_path',
        type=validate_compressed_file,
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

    args = parser.parse_args()
    return args
