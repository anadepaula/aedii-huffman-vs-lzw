from .compress import create_alphabet, compress_text
from .decompress import decompress_text


def compress(file_content):
    alphabet = create_alphabet(file_content)
    compressed_content = compress_text(file_content, alphabet)
    
    return compressed_content, alphabet

def decompress(loaded_codes, loaded_alphabet):
    decompressed = decompress_text(loaded_codes, loaded_alphabet)
    
    return decompressed