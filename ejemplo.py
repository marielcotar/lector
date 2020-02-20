#!/usr/bin/python3
# ejemplo.py : programa que usa varios argumentos con la misma opcion
import argparse

def main(nombres):
    for nombre in nombres:
        print(nombre)

if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nombre', dest='nombres', help="nombres de personas", action="append", required=True)
    args = parser.parse_args()
    nombres = args.nombres
    main(nombres)