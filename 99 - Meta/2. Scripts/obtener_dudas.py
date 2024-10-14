import os
import re
import sys
import yaml

# Variables globales:
carpeta_atomic = "."


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


    
def get_yaml(markdown_file):
    with open(markdown_file, 'r') as file:
        lines = file.readlines()
    
    frontmatter = []
    in_frontmatter = False
    dashes_count = 0

    for line in lines:
        
        if line == '---':
            dashes_count += 1
            if dashes_count == 1:
                in_frontmatter = True
                continue
            elif dashes_count == 2:
                break
        
        if in_frontmatter:
            frontmatter.append(line)
    
    if dashes_count == 2:
        return ''.join(frontmatter).strip()
    else:
        return None


def buscar_dudas(etiqueta):
    """
    Buscar todas las dudas con dudas de la etiqueta proporcionada.
    """
    carpeta = carpeta_atomic
    dudas_encontradas = []

    # Iterar sobre todos los archivos markdown de la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".md"):

            with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
                print(f"Buscando dudas en {archivo}")

                # Se salta el archivo si no tiene YAML frontmatter pq no tiene sentido buscar etiqueta
                if not has_yaml_frontmatter(os.path.join(carpeta, archivo)):
                    print(f"No tiene YAML frontmatter")
                    continue

                # Leer el fontmatter del archivo y extraer las etiquetas
                try:
                    config = yaml.safe_load(get_yaml(f))
                    contenido = f.readlines()
                    if config and ("tags" in config):
                        for tag in config["tags"]:
                            if tag == etiqueta:

                                for linea in contenido:
                                    # Buscar las líneas que contengan la etiqueta #Duda
                                    if "#Duda" in linea:
                                        duda = linea.split("#Duda")[
                                            -1
                                        ].strip()  # Extraer la duda
                                        dudas_encontradas.append((archivo, duda))
                except yaml.YAMLError:
                    print(f"Error parsing YAML in {archivo}")

    return dudas_encontradas


def crear_nota_dudas(etiqueta, dudas):
    nombre_archivo = f"Dudas {etiqueta}.md"
    with open(nombre_archivo, "w", encoding="utf-8") as nueva_nota:
        # Escribir la primera línea con el número total de dudas
        nueva_nota.write(f"# Dudas sobre {etiqueta}\n\n")
        nueva_nota.write(f"Total de dudas: {len(dudas)}\n\n")

        for i, (archivo, duda) in enumerate(dudas, 1):
            # Crear link a la nota, checkbox y escribir la duda numerada
            nueva_nota.write(f"- [ ] [[{archivo}]]: {duda}\n")
            # Añadir el callout para cada duda
            nueva_nota.write(f"![check] Solución:\n>\n\n")


if __name__ == "__main__":
    etiqueta_input = input("Introduce la etiqueta que deseas buscar: ").strip()

    """if etiqueta_input == "todas":
        # Obtener todas las etiquetas excepto #Duda
        todas_las_etiquetas = obtener_todas_las_etiquetas()
        for etiqueta in todas_las_etiquetas:
            dudas = buscar_dudas(etiqueta)
            
            # Solo crear nota si hay más de 5 dudas
            if len(dudas) > 5:
                crear_nota_dudas(etiqueta, dudas)
                print(f"Se ha creado la nota 'Dudas {etiqueta}.md' con {len(dudas)} dudas.")
            else:
                print(f"No se creó la nota para '{etiqueta}'. El número de dudas es menor que 5.")
    """
    dudas = buscar_dudas(etiqueta_input)

    if len(dudas) > 5:
        crear_nota_dudas(etiqueta_input, dudas)
        print(
            f"Se ha creado la nota 'Dudas {etiqueta_input}.md' con {len(dudas)} dudas."
        )
    else:
        print(
            f"El número de dudas es menor que 5. Solo se encontraron {len(dudas)} dudas."
        )
