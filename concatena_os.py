#!/usr/bin/python3
import lector
import os
import argparse

def juntar_archivos_os(inicio,termina):
    ruta = "/tmp/"
    folder_actual = os.listdir(ruta)
    #ruta+archivos
    lista_inicia = [archivo for archivo in folder_actual if archivo.startswith(inicio)]
    '''print(lista_inicia)
    print('--')'''
    lista_episodios = [archivo for archivo in lista_inicia if archivo.endswith(termina)]
    #print(lista_episodios)
    lista_texto = []
    #print(archivos)
    for archivo in lista_episodios:
        texto = lector.leer_archivo(ruta+archivo)
        lista_texto.append(texto)
    #print(lista_texto)
    return lista_texto
    
def main(inicio,termina,output):
    textos = juntar_archivos_os( inicio,termina )
    texto_limpio = " ".join(textos)
    #print('------------------------')
    #print (texto_limpio)
    
    with open(output, 'w') as f:
            f.write(texto_limpio)

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    #parser.add_argument('-f', '--folder', dest = 'folder', help = "nombre de folder", action="append", required = True)
    parser.add_argument('-o', '--output', dest='output', help="archivos en uno", required=True)
    parser.add_argument('-i', '--inicio', dest='inicio', help="donde inicia", required=True)
    parser.add_argument('-t', '--termina', dest='termina', help="donde termina", required=True)
    args = parser.parse_args()
    #folder = args.archivo
    output = args.output
    inicio = args.inicio
    termina = args.termina
    main(inicio, termina, output)