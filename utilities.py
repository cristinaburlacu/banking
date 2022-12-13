import json
import os

def read_data_from_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except:
        return {}

def write_to_disk(dictionary, file_path):
    dictionary_string = json.dumps(dictionary, indent = 4, separators = (',', ': '))
    with open(file_path, "w") as file:
        file.write(dictionary_string)

def check_key(dictionary, key, error_message):
    if key not in dictionary:
        raise Exception(error_message)