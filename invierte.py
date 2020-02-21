#!/usr/bin/python3

import argparse
import lector


def invertir(archivos):
    contenidos=[]
    texto = lector.leer_archivo(archivo)
    palabras = texto.split(" ")
    
    for palabra in palabras:
      contenidos.insert(0,palabra)
    print(contenidos)
    return contenidos


def main(archivos, output, contenidos):
    textos = invertir( archivos )
    texto_limpio = " ".join(textos)
    print (texto_limpio)
    
    with open(output,'w') as f:
        f.write(texto_limpio)

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest = 'archivo', help = "nombre de archivo", required = True)
    parser.add_argument('-o', '--output', dest='output', help="archivos en uno", required=True)
    parser.add_argument('-c', '--contenidos', dest='contenidos', help="archivos en uno", required=False)
    args = parser.parse_args()
    archivo = args.archivo
    output = args.output
    contenidos=args.contenidos
    main(archivo, output,contenidos)