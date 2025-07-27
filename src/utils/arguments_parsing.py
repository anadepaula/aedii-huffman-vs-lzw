import os
import argparse

from .types import (
    HUFFMANN_COMPRESSED_FILE_EXTENSION,
    HUFFMANN_MAP_EXTENSION,
    READING_MODE_COMPRESS,
    READING_MODE_DECOMPRESS,
)


def validate_inputted_file(filename, mode, extension=None):
    if extension:
        assert filename.endswith(extension)

    assert os.path.exists(filename, mode)

    return open(filename, READING_MODE_DECOMPRESS)

def validate_file_to_compress(filename):
    return validate_inputted_file(
        filename,
        READING_MODE_COMPRESS,
    )

def validate_compressed_file(filename):
    return validate_inputted_file(
        filename, 
        HUFFMANN_COMPRESSED_FILE_EXTENSION,
        READING_MODE_DECOMPRESS,
    )

def validate_compression_map_file(filename):
    return validate_inputted_file(
        filename, 
        HUFFMANN_MAP_EXTENSION,
        READING_MODE_DECOMPRESS,
    )

def parse_args_compress_huffman():
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

    args = parser.parse_args()
    return args


def parse_args_decompress_huffman():
    parser = argparse.ArgumentParser(
        description=('utility to decompress files compressed using huffman algorithm')
    )
    parser.add_argument(
        'file_to_compress_path',
        type=validate_file_to_compress,
        help = 'filename of file to compress using huffman algorithm'
    )
    parser.add_argument(
        '--output_file_path', 
        help = 'filename of to use to save compressed file and extension.'
    )

    args = parser.parse_args()
    return args
