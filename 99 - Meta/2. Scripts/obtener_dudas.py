import os
import re
import yaml 

# Variables globales:
carpeta_atomic = "../../02 - Atomic"

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


# Ahora mismo esta función no esta activa
def obtener_todas_las_etiquetas():
    carpeta = "../../02 - Atomic"  # Ruta relativa desde "99 - Meta/2. Scripts"
    etiquetas_encontradas = set()  # Usamos un set para evitar etiquetas duplicadas

    # Expresión regular para encontrar etiquetas
    patron_etiqueta = re.compile(r"#\w+")

    # Iterar sobre todos los archivos de la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".md"):
            with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
                contenido = f.readlines()

                # Buscar todas las etiquetas en cada línea
                for linea in contenido:
                    etiquetas = patron_etiqueta.findall(linea)
                    for etiqueta in etiquetas:
                        if etiqueta != "#Duda":  # Ignorar la etiqueta #Duda
                            etiquetas_encontradas.add(etiqueta)

    return etiquetas_encontradas


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
                # Se salta el archivo si no tiene YAML frontmatter pq no tiene sentido buscar etiquetas
                if not has_yaml_frontmatter(os.path.join(carpeta, archivo)):
                    continue
                front_matter = next(yaml.load_all(f, Loader=yaml.FullLoader))
                print(front_matter)
                if front_matter:
                    yaml_content = front_matter.group(1)
                    try:
                        front_matter = yaml.safe_load(yaml_content)
                        if front_matter and "tags" in front_matter:
                            for tag in front_matter["tags"]:
                                if tag == etiqueta:
                                    for linea in contenido:
                                    # Buscar las líneas que contengan la etiqueta #Duda
                                        if "#Duda" in linea:
                                            duda = linea.split("#Duda")[-1].strip()  # Extraer la duda
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
