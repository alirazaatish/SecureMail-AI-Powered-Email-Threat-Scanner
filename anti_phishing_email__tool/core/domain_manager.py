# File: core/domain_manager.py
import json
import os

def load_trusted_domains(path='data/trusted_domains.json'):
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return []

def save_trusted_domains(domains, path='data/trusted_domains.json'):
    with open(path, 'w') as f:
        json.dump(domains, f)
