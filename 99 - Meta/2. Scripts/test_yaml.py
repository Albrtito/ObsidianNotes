import os
import re
import yaml 

# Variables globales:
carpeta_atomic = "../../02 - Atomic"
archivo = "20240429 - 111944 - Theorem - Euclid's proof of infinite prime numbers.md"
with open(os.path.join(carpeta_atomic,archivo), "r",encoding="utf-8") as f:
    contenido = f.read()
    yaml_match = re.match(r"^---\n(.*?)\n---", contenido, re.DOTALL)
    print(yaml_match)
