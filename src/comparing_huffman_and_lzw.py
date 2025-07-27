from pathlib import Path
import os
import pandas as pd
import time

from main import (
    huffman_compress_cli,
    huffman_decompress_cli,
    lzw_compress_cli,
    lzw_decompress_cli,
)


def get_size_of_file(filename):
    return os.path.getsize(Path(filename))

def get_execution_metrics(file, number_of_runs=5):
    all_runs_info = []
    file_size = get_size_of_file(file)

    for run in range(number_of_runs):
        start_time = time.time() 
        filename_huffman_compressed_file, filename_huffman_map_tree = huffman_compress_cli([file])
        end_time = time.time()
        huffman_compressing_time = end_time - start_time

        huffman_compressed_file_size = get_size_of_file(filename_huffman_compressed_file)
        huffman_map_tree_size = get_size_of_file(filename_huffman_map_tree)

        start_time = time.time()
        _filename_huffman_decompressed_file = huffman_decompress_cli(
            [filename_huffman_compressed_file, filename_huffman_map_tree, file.replace('/', '/huffman_decompressed_')]
        )
        end_time = time.time()
        huffman_decompressing_time = end_time - start_time

        start_time = time.time() 
        filename_lzw_compressed_file = lzw_compress_cli([file])
        end_time = time.time()
        lzw_compressing_time = end_time - start_time
        
        lzw_compressed_file_size = get_size_of_file(filename_lzw_compressed_file)
        
        start_time = time.time() 
        _filename_lzw_decompressed_file = lzw_decompress_cli(
            [filename_lzw_compressed_file, file.replace('/', '/lzw_decompressed_')]
        )
        end_time = time.time()
        lzw_decompressing_time = end_time - start_time

        run_info = {
            "file": file,
            "run": run,
            "file_size": file_size,
            "huffman_compressing_time": huffman_compressing_time,
            "huffman_decompressing_time": huffman_decompressing_time,
            "huffman_compressed_file_size": huffman_compressed_file_size,
            "huffman_map_tree_size": huffman_map_tree_size,
            "lzw_compressing_time": lzw_compressing_time,
            "lzw_decompressing_time": lzw_decompressing_time,
            "lzw_compressed_file_size": lzw_compressed_file_size,
        }

        all_runs_info.append(run_info)
    return all_runs_info

files = [
    "data/streptomyces.fna",
    "data/pseudomonas.fna",
    "data/paramuribaculum.fna",
    "data/megasphaera.fna",
    "data/campylobacter.fna",
]

execution_info_all_dnas = []
for file in files:
    execution_metrics = get_execution_metrics(file)
    execution_info_all_dnas.extend(execution_metrics)

pd.DataFrame(
    data=execution_info_all_dnas
).to_csv(
    "execution_info_all_dnas.csv", 
    index=False,
)