import pickle


def save_huffman_map_to_file(map_tree, file_object_map_tree):
    pickle.dump(map_tree, file_object_map_tree)

def read_huffman_map(file_object):
    return pickle.load(file_object)

def save_huffman_compressed(content, file_object_map_tree):
    file_object_map_tree.write(content)
    file_object_map_tree.close()

def save_decompressed_data(content, file_object):
    file_object.write(content)
    file_object.close()
