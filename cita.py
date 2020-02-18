#!/usr/bin/python3
#Prueba
import lector
import contar_palabras
import argparse
    
def obten_cita(texto, inicio, cuenta):
    lista=texto.split(" ")
    longitud=len(lista)
    if((inicio+cuenta)<longitud):
      lista_palabras=lista[inicio:inicio+cuenta]
      cita=" ".join(lista_palabras)
    else:
      cita=""
      
    return cita
          
    
def main(archivo, archivo_sw,inicio, cuenta):
    texto=lector.leer_archivo(archivo)
    cita=obten_cita(texto, inicio, cuenta)
    print("cita",cita)
    sw=lector.leer_stopwords(archivo_sw)
    contar_palabras.contar(cita,sw)
    
  
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( '-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument( '-s', '--stopwords', dest='archivo_stopwords', help="stopwords", required=False,default="spanish_stopwords.txt")
    parser.add_argument( '-i', '--inicio', dest='inicio', help="inicio", required=False,default=20,type=int)
    parser.add_argument( '-c', '--cuenta', dest='cuenta', help="cuenta", required=False,default=30,type=int)
    args = parser.parse_args()
    archivo = args.archivo
    archivo_stopwords=args.archivo_stopwords
    inicio=args.inicio
    cuenta=args.cuenta
    main(archivo,archivo_stopwords, inicio, cuenta)
    