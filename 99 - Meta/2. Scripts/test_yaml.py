import os
import re
import sys

import yaml

# Variables globales:
carpeta_atomic = "../../02 - Atomic"
archivo = "20240429 - 111944 - Theorem - Euclid's proof of infinite prime numbers.md"
archivo2 = "Natural numbers (set N).md"

def has_yaml_frontmatter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        # Read the first line to check for opening '---'
        first_line = f.readline().strip()
        
        if first_line != "---":
            # If the first line is not '---', it doesn't have a frontmatter
            return False
        
        # Now, look for the closing '---' in subsequent lines
        for line in f:
            if line.strip() == "---":
                return True
    
# If no closing '---' is found, return False
    return False

if has_yaml_frontmatter(os.path.join(carpeta_atomic,archivo)):
    print("Tiene YAML frontmatter")
    with open(os.path.join(carpeta_atomic,archivo)) as f:
        front_matter = next(yaml.load_all(f, Loader=yaml.FullLoader))
        print(front_matter)

if has_yaml_frontmatter(os.path.join(carpeta_atomic,archivo2)):
    print("Tiene YAML frontmatter")
    with open(os.path.join(carpeta_atomic,archivo2)) as f:
        front_matter = next(yaml.load_all(f, Loader=yaml.FullLoader))
        print(front_matter)

