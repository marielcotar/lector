#!/usr/bin/python3
# importacion de librerias
import  argparse

#---------------------------
#2 funciones
def leer_archivo( archivo ):
    '''aqui va mi codigo
    '''
    
    try:
        with open(archivo,"r") as fh:
          texto = fh.read()
          lineas = texto.splitlines()
          texto_limpio = " ".join(lineas)
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
    if "" in dp:
        del(dp[""])

    return dp
    
def imprimir_diccionario(dp, minimo):
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
    
def limpia_diccionario(dp, set_stopwords):
     ndp = {}
     for k,v in dp.items():
         if k.lower() not in set_stopwords:
             ndp[k] = v
     return ndp

def main( archivo, minimo ):
    '''main() recibe nombre del archivo
       lo abre y cuenta las palabras repetidas
    '''
    #sw = leer_stopwords(archivo)
    texto = leer_archivo( archivo )
    dip   = contar_palabras( texto )
    stop_words = leer_stopwords ( "/home/auriga/Mariel/spanish_stopwords.txt" )
    ndp = limpia_diccionario ( dip, stop_words )
    #print( dip )
    imprimir_diccionario(ndp, minimo)
    
#-----------------------------
#3 ejecucion de main

if __name__ == "__main__":
    '''archivo = "/tmp/episodio4.txt"'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--archivo', dest = 'archivo', help = "nombre de archivo", required = True)
    parser.add_argument('-m', '--minimo', dest = 'minimo', help = "minimoo", required = False, type = int, default = 1 )
    args = parser.parse_args()
    minimo = args.minimo
    archivo = args.archivo
    #print(archivo)
    main(archivo,minimo)