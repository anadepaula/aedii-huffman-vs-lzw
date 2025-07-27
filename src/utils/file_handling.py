import pickle
from .logging import logger
from .types import (
    READING_MODE_DECOMPRESS,
    WRITING_MODE_DECOMPRESS,
    READING_MODE_COMPRESS,
    WRITING_MODE_COMPRESS,
)


def read_text_file(filename, mode=READING_MODE_COMPRESS, encoding='utf-8'):
    # logger.debug(f"filename {filename}, mode {mode}, encoding {encoding}")
    return read_file(filename, mode, encoding)

def read_binary_file(filename, encoding=None):
    # logger.debug(f"filename {filename}, encoding {encoding}")
    return read_file(filename, "rb", encoding)

def read_file(filename, mode, encoding=None):
    """
    Abre um arquivo .txt e retorna o texto contido nele.

    Returns:
        str: Texto contido no arquivo.
    """
    # logger.debug(f"filename {filename}, mode {mode}, encoding {encoding}")
    try:
        with open(filename, mode, encoding=encoding) as f:
            texto = f.read()
    except Exception as e:
        logger.error(f"Something happened while trying to open the file {filename}: {e}")
        raise e
    else:
        return texto

def read_huffman_map(filename):
    with open(filename, READING_MODE_DECOMPRESS) as f:
        content = pickle.load(f)
    return content

def remove_extension(filename):
    return filename.rsplit(".", 1)[0]

def get_file_names_lzw(filename):
    filename_without_extension = remove_extension(filename)
    filename_compressed_file = f"{filename_without_extension}.lzw"

    return filename_compressed_file

def get_file_names_huffman(filename):
    filename_without_extension = remove_extension(filename)
    
    filename_compressed_file = f"{filename_without_extension}.huff"
    filename_map_tree = f"{filename_without_extension}.huffmap"

    return filename_compressed_file, filename_map_tree

def get_file_object(filename, mode):
    return open(filename, mode)

def get_file_object_to_write_compressed_file(filename):
    return get_file_object(filename, WRITING_MODE_COMPRESS)

def get_file_object_to_read_compressed_file(filename):
    return get_file_object(filename, READING_MODE_DECOMPRESS)

def get_file_object_to_write_decompressed_file(filename):
    return get_file_object(filename, WRITING_MODE_DECOMPRESS)
