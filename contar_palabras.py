#!/usr/bin/python3
import lector
import argparse

def nueva_funcion(archivo):
    texto = lector.leer_archivo(archivo)
    return
    
def contar_palabras_unicas(dp):
    total=len(set(dp))
    return total
    
def contar(texto,stopwords):
  lista_palabras=texto.split(" ") #sacamos la lista de palabras de un texto split(separado) por espacios
  total_palabras=len(lista_palabras)  #length de la lista_palabras
  dpc=dict() #dicc.palabnras clave
  dps=dict() #dicc.palabras stop
  
  for palabra in lista_palabras:
    p=palabra.lower().strip(".,") # con esto cada palabra le quitamos el . y las comas
    if p in stopwords:
      if p in dps:
        dps[p] +=1 #sumamos 1
      else:
        dps[p] =1 #creamos
    else:
        if p in dpc:
            dpc[p]+=1 #sumamos
        else: 
            dpc[p]=1 #creamos
  sumapc=suma_diccionario(dpc)
  sumaps=suma_diccionario(dps)
  print("total de palabras:",total_palabras,"total de palabras clave:",sumapc,"total palabras unicas",sumaps)
  pcu=contar_palabras_unicas(dpc)
  pcs=contar_palabras_unicas(dps)
  total_pu= pcu+pcs
  print(total_pu)
    
def suma_diccionario(dp):
    suma=0
    for k,v in dp.items():
        suma+=v
    return suma

  
def contar_palabras_totales( texto ):
    palabras = texto.split(" ")
    dp = dict()
    cont = 0
    for palabra in palabras:
        p = palabra.strip(",.")
        if p != '':
            dp[cont] = p
            cont = cont+1
    return dp
    
def limpia_diccionario(dp, set_stopwords):
     ndp = {}
     for k,v in dp.items():
         if k.lower() not in set_stopwords:
             ndp[v] = k
     return ndp

def main(archivo,archivo_stopwords):
    nueva_funcion(archivo)
    texto = lector.leer_archivo( archivo )
    dip   = lector.contar_palabras( texto )
    stop_words= lector.leer_stopwords("/home/draco/alessandro/spanish_stopwords.txt")
    ndp = lector.limpia_diccionario(dip,stop_words)
    tot_texto=len(dip)
    tot_sinstopw=len(ndp)
    tot_stopw=tot_texto-tot_sinstopw
    new_dip = contar_palabras_totales( texto )
    palabras_totales = len(new_dip)
    palabras_stoptot = (palabras_totales-tot_sinstopw) 
    print("------------------------------------------------")
    print("Palabras totales: ", palabras_totales, " Palabras clave totales: ", tot_sinstopw," Palabras stop totales: ", palabras_stoptot)
    print("------------------------------------------------")
    print("Palabras unicas: ",tot_texto," Palabras clave unica: ",tot_sinstopw," Palabras stop unica: ",tot_stopw)
    print("Porcentaje de palabras clave unicas")
    print(((tot_sinstopw*100)/tot_texto),"%")
    print("Porcentaje de stopwords unicas")
    print(((tot_stopw*100)/tot_texto),"%")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( '-a', '--archivo', dest='archivo', help="nombre de archivo", required=True)
    parser.add_argument( '-s', '--stopwords', dest='archivo_stopwords', help="stopwords", required=False,default="spanish_stopwords.txt")
    args = parser.parse_args()
    archivo = args.archivo
    archivo_stopwords=args.archivo_stopwords
    main(archivo,archivo_stopwords)
    