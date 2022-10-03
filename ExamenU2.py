from ast import arg
from io import open
import json




def Relacion_Estudiantes(*args):
    try:
        archivo_texto=open("Estudiantes.prn","r")
        Estudiantes_texto=archivo_texto.readlines()
        archivo_texto.close()

        archivo_texto=open("Kardex.txt","r")
        Kardex_texto=archivo_texto.readlines()
        archivo_texto.close()
    except :
        print("Ha ocurrido un error con la ruta de los archivos")
    else:
        datAlum={}
        if(len(args)>0): #Con argumentos
            try:
                for i in range(0,len(args[0])):
                    for estudi in Estudiantes_texto:
                        if(str(args[0][i]) == estudi[0:8]): #Encontramos el estudiante
                            liMat=[]
                            for  kar in Kardex_texto:
                                tempo={}
                                dk=kar.split('|')
                                if(dk[0]==str(args[0][i])): #Encontramos sus materias
                                    liMat.append(dk[1])
                            valest=estudi[8:].split('\n')
                            tempo["Nombre"]=valest[0]
                            tempo["Materias"]=liMat
                            datAlum[args[0][i]]=tempo
            except IndexError:
                print("Ha ocurrido con la cantidad de elementos ")
            else:
                pass
        else: #Sin argumentos
            for estudi in Estudiantes_texto:
                        liMat=[]
                        for  kar in Kardex_texto:
                            tempo={}
                            dk=kar.split('|')
                            if(dk[0]==estudi[0:8]): #Encontramos sus materias
                                liMat.append(dk[1])
                                valest=estudi[8:].split('\n')
                                tempo["Nombre"]=valest[0]
                                tempo["Materias"]=liMat
                                datAlum[dk[0]]=tempo

    return json.dumps(datAlum)



print(Relacion_Estudiantes([18420461,18420424,16420537]))