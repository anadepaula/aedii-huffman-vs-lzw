from datetime import datetime
from pathlib import Path
import os
import pandas as pd
import time
import json
import tracemalloc

from main import (
    huffman_compress_cli,
    huffman_decompress_cli,
    lzw_compress_cli,
    lzw_decompress_cli,
)
from utils import logger


def get_size_of_file(filename):
    return os.path.getsize(Path(filename))

def count_bases(file_path):
    counting_bases = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
        "N": 0,
    }
    has_extra_chars = False
    bases = set(counting_bases.keys())
    with open(file_path, "r") as f:
        content = f.readlines()
        for line in content:
            line = line.strip()
            if not line.startswith(">"):
                for base in counting_bases.keys():
                    counting_bases[base] += line.count(base)
                if (not has_extra_chars) and set(line) - bases:
                    has_extra_chars = True

    counting_bases["has_extra_chars"] = has_extra_chars
    return counting_bases

def get_execution_metrics(name, file, index, number_of_runs=5):
    execution_filename = f"execution_info_{name}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json"

    all_runs_info = []
    file_size = get_size_of_file(file)
    logger.info(f"[{index}][{file}] starting runs")

    for run in range(1, number_of_runs+1):
        logger.info(f"[{index}][{file}] [{run}] started")

        logger.info(f"[{index}][{file}] [{run}] [1/4] huffman_compressing")
        start_time = time.time() 
        tracemalloc.start()
        filename_huffman_compressed_file, filename_huffman_map_tree = huffman_compress_cli([file])
        huffman_compressing_meemory_current, huffman_compressing_memory_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        huffman_compressing_time = end_time - start_time

        huffman_compressed_file_size = get_size_of_file(filename_huffman_compressed_file)
        huffman_map_tree_size = get_size_of_file(filename_huffman_map_tree)

        logger.info(f"[{index}][{file}] [{run}] [2/4] huffman_decompressing")
        start_time = time.time()
        tracemalloc.start()
        _filename_huffman_decompressed_file = huffman_decompress_cli(
            [filename_huffman_compressed_file, filename_huffman_map_tree, file.replace('/', '/huffman_decompressed_')]
        )
        huffman_decompressing_meemory_current, huffman_decompressing_memory_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        huffman_decompressing_time = end_time - start_time

        logger.info(f"[{index}][{file}] [{run}] [3/4] lzw_compressing")
        start_time = time.time() 
        tracemalloc.start()
        filename_lzw_compressed_file = lzw_compress_cli([file])
        lzw_compressing_meemory_current, lzw_compressing_memory_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        lzw_compressing_time = end_time - start_time
        
        lzw_compressed_file_size = get_size_of_file(filename_lzw_compressed_file)
        
        logger.info(f"[{index}][{file}] [{run}] [4/4] lzw_decompressing")
        start_time = time.time() 
        tracemalloc.start()
        _filename_lzw_decompressed_file = lzw_decompress_cli(
            [filename_lzw_compressed_file, file.replace('/', '/lzw_decompressed_')]
        )
        lzw_decompressing_meemory_current, lzw_decompressing_memory_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        lzw_decompressing_time = end_time - start_time

        run_info = {
            "file": file,
            "run": run,
            "file_size": file_size,
            "huffman_compressing_time": huffman_compressing_time,
            "huffman_compressing_meemory_current": huffman_compressing_meemory_current,
            "huffman_compressing_memory_peak": huffman_compressing_memory_peak,
            "huffman_decompressing_time": huffman_decompressing_time,
            "huffman_decompressing_meemory_current": huffman_decompressing_meemory_current,
            "huffman_decompressing_memory_peak": huffman_decompressing_memory_peak,
            "huffman_compressed_file_size": huffman_compressed_file_size,
            "huffman_map_tree_size": huffman_map_tree_size,
            "lzw_compressing_time": lzw_compressing_time,
            "lzw_compressing_meemory_current": lzw_compressing_meemory_current,
            "lzw_compressing_memory_peak": lzw_compressing_memory_peak,
            "lzw_decompressing_time": lzw_decompressing_time,
            "lzw_decompressing_meemory_current": lzw_decompressing_meemory_current,
            "lzw_decompressing_memory_peak": lzw_decompressing_memory_peak,
            "lzw_compressed_file_size": lzw_compressed_file_size,
        }
        
        logger.info(f"[{index}][{file}] [{run}] counting bases")
        bases_counting = count_bases(file)
        run_info.update(bases_counting)

        with open(execution_filename, "w") as f:
            json.dump(run_info, f)
        logger.info(f"[{index}][{file}] [{run}] finished! data saved in {execution_filename}")
        all_runs_info.append(run_info)

    logger.info(f"[{index}][{file}] all runs finished!")
    
    return all_runs_info

all_runs_filename = f"execution_info_all_dnas_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"

dir_with_files = "data"
json_mapping_file = Path(dir_with_files, "file_mapping.json")

with open(json_mapping_file) as f:
    mapping_files = json.load(f)
files = mapping_files.keys()

n_files = len(files)

logger.info(
    "will run the stats for the following files "
    f"in the dir {dir_with_files}: {','.join(files)} "
    f"and save the result to the file {all_runs_filename}."
)

execution_info_all_dnas = []

for index, name in enumerate(files, start=1):
    file_path = str(Path(dir_with_files, f"{name}.fna"))
    execution_metrics = get_execution_metrics(
        name,
        file_path, 
        f"{index}/{n_files}",
        number_of_runs=1,
    )
    execution_info_all_dnas.extend(execution_metrics)

datetime.now.strftime("%Y%m%d_%H%M%S")
pd.DataFrame(
    data=execution_info_all_dnas
).to_csv(
    all_runs_filename,
    index=False,
)
logger.info(f"all runs finished! data saved in {all_runs_filename}")