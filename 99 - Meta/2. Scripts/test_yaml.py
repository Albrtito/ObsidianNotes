import os
import re
import yaml 
import sys

# Variables globales:
carpeta_atomic = "../../02 - Atomic"
archivo = "20240429 - 111944 - Theorem - Euclid's proof of infinite prime numbers.md"



with open(os.path.join(carpeta_atomic,archivo)) as f:
    front_matter = next(yaml.load_all(f, Loader=yaml.FullLoader))
    print(front_matter)
