from pathlib import Path
import gzip 
import json
import requests
from utils import logger

def decompress_gz_file(input_filepath, output_filepath):
    with gzip.open(input_filepath, 'rb') as f_in:
        with open(output_filepath, 'wb') as f_out:
            f_out.write(f_in.read())

def download_file(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        f.write(response.content)

dir_to_save_files = "data"
json_mapping_file = Path(dir_to_save_files, "file_mapping.json")
with open(json_mapping_file) as f:
    mapping_files = json.load(f)

for name, url in mapping_files.items():

    file = f"{name}.fna"
    file_path = Path(dir_to_save_files, file)
    compressed_file_path = Path(dir_to_save_files, f"{file}.gz")
    
    logger.info(f"downloading {name} file")
    download_file(url, compressed_file_path)

    logger.info(f"decompressing {name} file")
    decompress_gz_file(compressed_file_path, file_path)
