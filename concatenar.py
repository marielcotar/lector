#!/usr/bin/python3
import lector
import argparse

def juntar_archivos(archivos):
    contenidos = []
    print(archivos)
    for archivo in archivos:
        texto = lector.leer_archivo(archivo)
        print(texto)
        contenidos.append(texto)
    return contenidos
    
def main(archivos, output):
    textos = juntar_archivos( archivos )
    texto_limpio = " ".join(textos)
    print (texto_limpio)
    
    with open(output, 'w') as f:
            f.write(texto_limpio)

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest = 'archivo', help = "nombre de archivo", action="append", required = True)
    parser.add_argument('-o', '--output', dest='output', help="archivos en uno", required=True)
    args = parser.parse_args()
    archivo = args.archivo
    output = args.output
    main(archivo, output)