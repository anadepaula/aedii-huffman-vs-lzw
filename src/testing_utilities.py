import argparse
import os

from utils import (
    logger,
    parse_args_decompress_huffman
)

if __name__ == "__main__":
    args = parse_args_decompress_huffman()
    logger.info(args)
