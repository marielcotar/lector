#!/usr/bin/python3
# importacion de librerias
import argparse

#---------------------------
#2 funciones
def leer_archivo( archivo ):
    '''aqui va mi codigo
    '''
    
    try:
       with open(archivo, "r") as fh:
         texto = fh.read()
         lista = texto.splitlines()
         texto_limpio = " ".join(lista)
    except:
       texto_limpio = ""
       
    return texto_limpio
    
def contar_palabras( texto ):
    '''codigo para esta funcion
    '''
    palabras = texto.split(" ")
    dp = dict()
    for palabra in palabras:
        p = palabra.strip(",.")
        if p in dp:
            dp[p] += 1
        else:
            dp[p] = 1
        del (dp[""])

    return dp
    
def imprime_diccionario(dp, minimo):
    lista = [(k,v) for k,v in dp.items() if v >= minimo]
    lista_ordenada = sorted(lista, key= lambda x:x[1], reverse = True)
    for tupla in lista_ordenada:
      print(tupla[0],"= ",tupla[1])
    return
    
def leer_stopwords(archivo):
    lista = []
    set_stop = set()
    try:
        with open(archivo,"r") as fh:
            texto = fh.readlines()
            for palabra in texto:
                p = palabra.strip("\n")
                lista.append(p)
        set_stop = set(lista)
    except:
        set_stop = set()
    return set_stop
    
def main( archivo ):
    '''main() recibe nombre del archivo
       lo abre y cuenta las palabras repetidas
    '''
    texto = leer_archivo( archivo )
    dip   = contar_palabras( texto )
    #print( dip )
    imprime_diccionario(dip, 3)
    
#-----------------------------
#3 ejecucion de main

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--archivo', dest = 'archivo', help = "nombre archivo", required=True)
    parser.add_argument('-m','--minimo', dest = 'minimo', help = "minimo de repeticiones", required=False, type=int, default=1)
    args = parser.parse_args()
    archivo = args.archivo
    minimo = args.minimo
    #archivo = "/tmp/episodio4.txt"
    main(archivo)