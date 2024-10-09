import os
import re

def buscar_dudas(etiqueta):
    carpeta = "../../02 - Atomic"  # Ruta relativa desde "99 - Meta/2. Scripts"
    dudas_encontradas = []

    # Iterar sobre todos los archivos de la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".md"):  # Asumiendo que tus notas están en formato markdown
            with open(os.path.join(carpeta, archivo), 'r', encoding='utf-8') as f:
                contenido = f.readlines()
                
                # Buscar la etiqueta proporcionada
                if any(etiqueta in linea for linea in contenido):
                    for linea in contenido:
                        # Buscar las líneas que contengan la etiqueta #Duda
                        if '#Duda' in linea:
                            duda = linea.split('#Duda')[-1].strip()  # Extraer la duda
                            dudas_encontradas.append((archivo, duda))

    return dudas_encontradas

def crear_nota_dudas(etiqueta, dudas):
    nombre_archivo = f"Dudas {etiqueta}.md"
    with open(nombre_archivo, 'w', encoding='utf-8') as nueva_nota:
        # Escribir la primera línea con el número total de dudas
        nueva_nota.write(f"# Dudas sobre {etiqueta}\n\n")
        nueva_nota.write(f"**Total de dudas:** {len(dudas)}\n\n")
        
        for i, (archivo, duda) in enumerate(dudas, 1):
            # Crear link a la nota, checkbox y escribir la duda numerada
            nueva_nota.write(f"- [ ] [[{archivo}]] {duda}\n")
            # Añadir el callout para cada duda
            nueva_nota.write(f">[!check] Solución:\n>\n\n")

if __name__ == "__main__":
    etiqueta = input("Introduce la etiqueta que deseas buscar: ").strip()
    dudas = buscar_dudas(etiqueta)
    
    if len(dudas) > 5:
        crear_nota_dudas(etiqueta, dudas)
        print(f"Se ha creado la nota 'Dudas {etiqueta}.md' con {len(dudas)} dudas.")
    else:
        print(f"El número de dudas es menor que 5. Solo se encontraron {len(dudas)} dudas.")

