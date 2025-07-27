import os
import argparse

from .types import (
    HUFFMANN_COMPRESSED_FILE_EXTENSION,
    HUFFMANN_MAP_EXTENSION,
    READING_MODE_DECOMPRESS,
)


def validate_inputted_file(filename, extension):
    assert filename.endswith(extension)

    assert os.path.exists(filename)

    return open(filename, READING_MODE_DECOMPRESS)

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

def parse_args_decompress_huffman():
    parser = argparse.ArgumentParser(
        description=('utility to decompress files compressed using huffman algorithm')
    )
    parser.add_argument(
        'compressed_file_path',
        type=validate_compressed_file,
        help = 'filename of .huff file containing the compressed file.'
    )
    parser.add_argument(
        'map_file_path', 
        type=validate_compression_map_file,
        help = 'filename of .huffmap file containing the huffton map.'
    )

    args = parser.parse_args()
    return args
