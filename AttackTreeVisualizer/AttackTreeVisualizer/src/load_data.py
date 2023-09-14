import json

def load_attack_tree(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
