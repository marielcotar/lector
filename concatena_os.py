#!/usr/bin/python3
import lector
import os
import argparse

def juntar_archivos_os(folder, inicio,termina):
    folder_actual = os.listdir(folder)
    lista_inicia = [archivo for archivo in folder_actual if archivo.startswith(inicio)]
    lista_termina = [archivo for archivo in lista_inicia if archivo.endswith(termina)]
    lista_texto = []
    for archivo in lista_termina:
        texto = lector.leer_archivo(os.path.join(folder,archivo))
        lista_texto.append(texto)
    return lista_texto
    
def main(folder,inicio,termina,output):
    textos = juntar_archivos_os( folder, inicio,termina )
    texto_limpio = " ".join(textos)
    
    with open(output, 'w') as f:
            f.write(texto_limpio)

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', dest = 'folder', help = "nombre de folder", required=True)
    parser.add_argument('-o', '--output', dest='output', help="archivos en uno", required=True)
    parser.add_argument('-i', '--inicio', dest='inicio', help="donde inicia", default='')
    parser.add_argument('-t', '--termina', dest='termina', help="donde termina", required=True)
    args = parser.parse_args()
    folder = args.folder
    output = args.output
    inicio = args.inicio
    termina = args.termina
    main(folder, inicio, termina, output)