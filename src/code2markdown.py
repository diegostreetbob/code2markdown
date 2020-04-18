#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#-------------------------------------------------------------------------------
# Name:        c2md.py
# Author:      diegostreetbob
# Created:     14/04/2020
# Copyright:   (c) diegostreetbob 2020
# Licence:     <Free>
#-------------------------------------------------------------------------------
################################################################################
import re #importamos módulo regex
import sys
from datetime import datetime
import glob, os
################################################################################
h1="#"
h2="##"
h3="###"
h4="####"
h5="#####"
toc="[TOC]"
ccodestar="```c"
ccodend="```"
pycodestar="```python"
pycodend="```"
espacio=" "
saltolin="\n"
retorno="\r"
lineamd="***"
clasenombre=""
indentado="2"
################################################################################
'''
Creamos el documento a markdown ha de ir esto(respetar los espacios)
[TOC]

'''
def cCrearDoc(modulonombre,comando=1, extension=".c"):
    #abre el fichero, si no existe lo borra y si existe lo sobre escribe
    # importante encoding="cp1252" para escribir bien los acentos
    f=open(modulonombre+".md",'w',encoding="cp1252")
    if(comando==1):
        salida=toc+saltolin+h2+espacio+"Fuente: "+ modulonombre+extension+saltolin
    else:
        salida=toc+saltolin+h2+espacio+"Fuente: "+modulonombre+saltolin+h3+espacio+"Entidades"
    f.write(salida)
    f.close
################################################################################
'''
Creamos el documento a markdown ha de ir esto(respetar los espacios)
[TOC]

## Casa.c

###  Clases, tipos
'''
def crearDoc(modulonombre):
    #abre el fichero, si no existe lo borra y si existe lo sobre escribe
    # importante encoding="cp1252" para escribir bien los acentos
    f=open(modulonombre+".md",'w',encoding="cp1252")
    salida=toc+saltolin+h2+espacio+"Fuente: "+modulonombre+saltolin
    f.write(salida)
    f.close
################################################################################
#Recorremos el documento buscando //@ent,//@atr,//@oper nombre, por ejemplo
#cuando encontremos, este método solo es para tratamiento C modo especial,comando
#2
def headerBuscarEntidades(ficheroentrada,modulonombre):
    flag=0 # no se ha encontrado entidad aún
    flag1=0 #flag para controlar que no se escriba mas de una vez  atributo
    flag2=0 #flag para controlar que no se escriba mas de una vez  operacion
    flag3=0 #flag para controlar que no se escriba mas de una vez  macros
    descripcion=""
    #abrimos el fichero .h en modo lectura y guardamos todas las lineas en
    #una lista, ojo que mete siempre un \n al final
    try:
        #importante usar encoding encoding='utf-8' para leer bien los acentos
        f=open(ficheroentrada,'r',encoding='utf-8')
        #guardamos el fichero en una lisa
        lineas=f.readlines()
        f.close
    except:
        print("Error al abrir fichero header")
    #recorremos todas las lineas buscando @clase
    for linea in lineas:
        #si en la iteración anterior se ha encontrado escribimos la siguiente
        #linea que sera el encabezado del typedef struct
        if(flag):
            linea_=linea[:-2]# de typedef struct imagen{\n a typedef struct imagen
            anadirLinea(linea_+saltolin+ccodend+saltolin,modulonombre)
            flag=0
        #buscamos la //@.... en linea
        locclase=re.search("//@ent",linea)
        locatr=re.search("//@atr",linea)
        locoper=re.search("//@oper",linea)
        #si se encuentra //@clase
        if(locclase or locatr or locoper):
            if(locclase):
                tag = re.split("//@ent", linea)
                nombre = re.split("\s", tag[1])
                desc= re.split(nombre[1], tag[1])
                clasenombre=nombre[1]
                descripcion=desc[1]
            if(locatr):
                tag = re.split("//@atr", linea)
                descripcion=tag[1]
            if(locoper):
                tag = re.split("//@oper", linea)
                descripcion=tag[1]
             # si hemos encontrado una clase
            if(locclase):
                # escribimos el nombre de la clase
                salida=saltolin+h4+espacio+clasenombre
                anadirLinea(salida,modulonombre)
                # escribimos la descripción de la clase como código
                salida=saltolin+ccodestar+saltolin+"//"+descripcion
                anadirLinea(salida,modulonombre)
                flag=1
                flag1=0
            # si hemos encontrado un atributo
            if(locatr):
                # escribimos encabezado de atributos
                if(flag1==0):
                    salida=saltolin+h5+espacio+"Atributos"
                    anadirLinea(salida,modulonombre)
                    flag1=1
                # escribimos la descripción del atributo como código
                salida=saltolin+ccodestar+saltolin+"//"+descripcion
                anadirLinea(salida,modulonombre)
                flag=1
            # si hemos encontrado una operacion
            if(locoper):
                # escribimos encabezado de atributos
                if(flag2==0):
                    salida=saltolin+h5+espacio+"Operaciones"
                    anadirLinea(salida,modulonombre)
                    #enlace a definiciones de operaciones
                    salida=saltolin+"[Ir a desglose de operaciones]"+"(#Desglose de operaciones)"
                    anadirLinea(salida,modulonombre)
                    flag2=1
                # escribimos la descripción del atributo como código
                salida=saltolin+ccodestar+saltolin+"//"+descripcion
                anadirLinea(salida,modulonombre)
                flag=1
        #fin si se encuentra
    buscarMacros(ficheroentrada,modulonombre)
    buscarVarGlobales(ficheroentrada,modulonombre)
################################################################################
def buscarMacros(ficheroentrada,modulonombre):
    flag=0 # no se ha encontrado macro aún
    flag1=0
    descripcion=""
    #abrimos el fichero .h en modo lectura y guardamos todas las lineas en
    #una lista, ojo que mete siempre un \n al final
    try:
        #importante usar encoding encoding='utf-8' para leer bien los acentos
        f=open(ficheroentrada,'r',encoding='utf-8')
        #guardamos el fichero en una lisa
        lineas=f.readlines()
        f.close
    except:
        print("Error al abrir fichero header")
    #recorremos todas las lineas buscando @clase
    for linea in lineas:
        #si en la iteración anterior se ha encontrado escribimos la siguiente
        #linea que sera el encabezado del typedef struct
        if(flag):
            linea_=linea[:-2]# de typedef struct imagen{\n a typedef struct imagen
            anadirLinea(linea_+saltolin+ccodend+saltolin,modulonombre)
            flag=0
        #buscamos la //@..... en linea
        locmac=re.search("//@mac",linea)
        #si se encuentra
        if(locmac):
            tag = re.split("//@mac", linea)
            descripcion=tag[1]
            # escribimos encabezado de macro solo una vez
            if(flag1==0):
                salida=saltolin+h5+espacio+"Macros"
                anadirLinea(salida,modulonombre)
                flag1=1
            # escribimos la descripción del macro como código
            salida=saltolin+ccodestar+saltolin+"//"+descripcion
            anadirLinea(salida,modulonombre)
            flag=1
        #fin si se encuentra
################################################################################
def buscarVarGlobales(ficheroentrada,modulonombre):
    flag=0 # no se ha encontrado macro aún
    flag1=0
    descripcion=""
    #abrimos el fichero .h en modo lectura y guardamos todas las lineas en
    #una lista, ojo que mete siempre un \n al final
    try:
        #importante usar encoding encoding='utf-8' para leer bien los acentos
        f=open(ficheroentrada,'r',encoding='utf-8')
        #guardamos el fichero en una lisa
        lineas=f.readlines()
        f.close
    except:
        print("Error al abrir fichero header")
    #recorremos todas las lineas buscando @clase
    for linea in lineas:
        #si en la iteración anterior se ha encontrado escribimos la siguiente
        #linea que sera el encabezado del typedef struct
        if(flag):
            linea_=linea[:-2]# de typedef struct imagen{\n a typedef struct imagen
            anadirLinea(linea_+saltolin+ccodend+saltolin,modulonombre)
            flag=0
        #buscamos
        locmac=re.search("//@glob",linea)
        #si se encuentra
        if(locmac):
            tag = re.split("//@glob", linea)
            descripcion=tag[1]
            # escribimos encabezado de macro solo una vez
            if(flag1==0):
                salida=saltolin+h5+espacio+"Variables globales"
                anadirLinea(salida,modulonombre)
                flag1=1
            # escribimos la descripción del macro como código
            salida=saltolin+ccodestar+saltolin+"//"+descripcion
            anadirLinea(salida,modulonombre)
            flag=1
        #fin si se encuentra
################################################################################
def cBuscarOper(ficheroentradaoper,modulonombre):
    #Encabezado
    salida=saltolin+h5+espacio+"Desglose de operaciones"+saltolin
    anadirLinea(salida,modulonombre)
    #abrimos el fichero .c en modo lectura y guardamos todas las lineas en
    #una lista, ojo que mete siempre un \n al final
    try:
        #importante usar encoding encoding='utf-8' para leer bien los acentos
        f=open(ficheroentradaoper,'r',encoding='utf-8')
        #guardamos el fichero en una lisa
        lineas=f.readlines()
        f.close
    except:
        print("Error al abrir fichero .c")
    #recorremos todas las lineas buscando @clase
    for linea in lineas:
        #buscamos comentario /> en cada línea
        loccom=re.search("//>",linea)
        #buscamos linea a insertar como comentario de código
        loccod=re.search("//<",linea)
        #buscamos linea a insertar como comentario de código en linea
        loccodlin=re.search("//<<",linea)
        #si se encuentra
        if(loccom):
            tag = re.split("//>", linea)
            descripcion=tag[1]
            # escribimos el comentario
            salida=descripcion
            anadirLinea(salida,modulonombre)
        if(loccod and not loccodlin):
            tag = re.split("//<", linea)
            descripcion=tag[0]
            # escribimos el comentario
            salida=descripcion.strip()
            anadirLineaCodigo(salida,modulonombre)
        if(loccodlin):
            tag = re.split("//<<", linea)
            descripcion=tag[0]
            # escribimos el comentario quitando espacios en blanco
            salida="`"+descripcion.strip()+"`"+saltolin+saltolin
            anadirLinea(salida,modulonombre,"py")
################################################################################
def pyBuscarOper(ficheroentradaoper,modulonombre):
    #abrimos el fichero .py en modo lectura y guardamos todas las lineas en
    #una lista, ojo que mete siempre un \n al final
    try:
        #importante usar encoding encoding='utf-8' para leer bien los acentos
        f=open(ficheroentradaoper,'r',encoding='utf-8')
        #guardamos el fichero en una lisa
        lineas=f.readlines()
        f.close
    except:
        print("Error al abrir fichero .py")
    #recorremos todas las lineas buscando
    for linea in lineas:
        #buscamos comentario /> en cada línea
        loccom=re.search("#>",linea)
        #buscamos linea a insertar como comentario de código
        loccod=re.search("#<",linea)
        #buscamos linea a insertar como comentario de código en linea
        loccodlin=re.search("#<<",linea)
        #si se encuentra
        if(loccom):
            tag = re.split("#>", linea)
            descripcion=tag[1]
            # escribimos el comentario
            salida=descripcion
            anadirLinea(salida,modulonombre)
        if(loccod and not loccodlin):
            tag = re.split("#<", linea)
            descripcion=tag[0]
            # escribimos el comentario
            salida=descripcion.strip()
            anadirLineaCodigo(salida,modulonombre,"py")
        if(loccodlin):
            tag = re.split("#<<", linea)
            descripcion=tag[0]
            # escribimos el comentario quitando espacios en blanco
            salida="`"+descripcion.strip()+"`"+saltolin+saltolin
            anadirLinea(salida,modulonombre,"py")
################################################################################
def anadirLinea(texto,modulonombre,tipo="c"):
    #abre el fichero, si no existe lo crea y si existe escribe al final
    # importante encoding="cp1252" para escribir bien los acentos
    f=open(modulonombre+".md",'a',encoding="cp1252")
    f.write(texto)
    f.close
################################################################################
def anadirLineaCodigo(codigo,modulonombre,tipo="c"):
    #abre el fichero, si no existe lo crea y si existe escribe al final
    # importante encoding="cp1252" para escribir bien los acentos
    f=open(modulonombre+".md",'a',encoding="cp1252")
    if(tipo=="c"):
        f.write(ccodestar+saltolin+codigo+saltolin+ccodend+saltolin)
    if(tipo=="py"):
        f.write(pycodestar+saltolin+codigo+saltolin+pycodend+saltolin)
    f.close
################################################################################
def borrarUltimaLinea():
    fd=open("salida.md","r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open("salida.md","w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
################################################################################
def fusionar():
    #Borramos el contenido del fichero previo si existe
    try:
        f=open("docDeProyecto.md",'w',encoding="cp1252")
        f.write("\n")
        f.close
    except:
        print("...")
    #Recorremos todo el directorio buscando los .md excepto readme.md
    docs = [f for f in glob.glob("*.md")]
    #para cada documento
    for doc in docs:
        #guardamos todas las lineas en lineas
        try:
            f=open(doc,'r')
            #guardamos el fichero en una lisa
            lineas=f.readlines()
            f.close
        except:
            print("Error al abrir fichero")
        #por cada linea abrimos el documento final e insertamos dicha linea
        for linea in lineas:
            anadirLinea(linea,"docDeProyecto")
################################################################################
'''
Ejemplos de uso:
    Argumento 1(tipo de lenguaje a documentar)
        1- C,(o cualquier lenguaje que admita comentarios de línea del tipo //):
        2- Lenguaje C(modo especial):
            * Extensiones admitidas: .h, internamente carga el .c
        3- Lenguaje Python
'''
def main():
    piepagina="*Documentado con code2markdown, https://github.com/diegostreetbob/code2markdown*"
    sellotemporalobj=datetime.now()
    sellotemporal="*Sello temporal:"+sellotemporalobj.strftime("%d-%b-%Y (%H:%M:%S.%f)")+"*"+saltolin
    comando=sys.argv[1]
    mod_nom=sys.argv[2]
    ext=mod_nom.split(".")
    #longitud de la extensión, js tiene longitud 2
    lext=len(ext[1])
    lext=lext+1 #añadimos el . a la longitud de extensión
    modulonombre=mod_nom[:-lext]#Imagen.h -> Imagen
    #Tratamiento C u otro con comentarios del typo //
    if(comando=="1"):
        print("Comienzo.....")
        ficheroentradaoper=modulonombre+"."+ext[1]
        cCrearDoc(modulonombre,1,"."+ext[1])
        cBuscarOper(ficheroentradaoper,modulonombre)
        anadirLinea(sellotemporal,modulonombre)
        anadirLinea(piepagina,modulonombre)
        print("Fusionamos documentos")
        #fusionamos todos los documentos
        fusionar()
        print("Fin.....")
    #Tratamiento C(modo especial)
    elif(comando=="2" and mod_nom.endswith("h")):
        print("Comienzo.....")
        modulonombre=mod_nom[:-2]#Imagen.h -> Imagen
        ficheroentrada=modulonombre+".h"
        ficheroentradaoper=modulonombre+".c"
        cCrearDoc(modulonombre,2)
        headerBuscarEntidades(ficheroentrada,modulonombre)
        cBuscarOper(ficheroentradaoper,modulonombre)
        anadirLinea(sellotemporal,modulonombre)
        anadirLinea(piepagina,modulonombre)
        print("Fusionamos documentos")
        #fusionamos todos los documentos
        fusionar()
        print("Fin.....")
    #Tratamiento de código Python, enviamos por parámetro el. py pero se trata
    elif(comando=="3" and mod_nom.endswith("y")):
        print("Comienzo.....")
        ficheroentradaoper=modulonombre+"."+ext[1]
        cCrearDoc(modulonombre,1,"."+ext[1])
        pyBuscarOper(ficheroentradaoper,modulonombre)
        anadirLinea(sellotemporal,modulonombre)
        anadirLinea(piepagina,modulonombre)
        print("Fusionamos documentos")
        #fusionamos todos los documentos
        fusionar()
        print("Fin.....")
    elif(comando=="-h"):
        print("Para ayuda visitar el repositorio en: https://github.com/diegostreetbob/code2markdown")
    else: print("No ha seleccionado ninguna opción correcta")

################################################################################
if __name__ == '__main__':
    main()
################################################################################
