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

## Casa.c

###  Clases, tipos
'''
def cCrearDoc(modulonombre):
    #abre el fichero, si no existe lo borra y si existe lo sobre escribe
    # importante encoding="cp1252" para escribir bien los acentos
    f=open(modulonombre+".md",'w',encoding="cp1252")
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
#Recorremos el documento buscando @ent nombre, por ejemplo cuando encontremos
#esto:
#cuando encontremos este código:
'''
//@ent Imagen descripción de la clase
typedef struct imagen{
int fil;//@atr filas de la imagen
int col;//@atr columnas de la imagen
unsigned char col_masc;//@atr columnas de la mascara, si aplica
unsigned char *imagen;//@atr puntero a imagen
void (*print)();//@met método para imprimir
void (*borrar)();//@met método para liberar memoria
}Imagen;
'''
#1º Buscamos @ent y en markdown escribimos:
'''
#### nombre\n
```c
descripción de la clase
```

'''
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
            anadirlinea(linea_+saltolin+ccodend+saltolin,modulonombre)
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
                anadirlinea(salida,modulonombre)
                # escribimos la descripción de la clase como código
                salida=saltolin+ccodestar+saltolin+"//"+descripcion
                anadirlinea(salida,modulonombre)
                flag=1
                flag1=0
            # si hemos encontrado un atributo
            if(locatr):
                # escribimos encabezado de atributos
                if(flag1==0):
                    salida=saltolin+h5+espacio+"Atributos"
                    anadirlinea(salida,modulonombre)
                    flag1=1
                # escribimos la descripción del atributo como código
                salida=saltolin+ccodestar+saltolin+"//"+descripcion
                anadirlinea(salida,modulonombre)
                flag=1
            # si hemos encontrado una operacion
            if(locoper):
                # escribimos encabezado de atributos
                if(flag2==0):
                    salida=saltolin+h5+espacio+"Operaciones"
                    anadirlinea(salida,modulonombre)
                    #enlace a definiciones de operaciones
                    salida=saltolin+"[Ir a desglose de operaciones]"+"(#Desglose de operaciones)"
                    anadirlinea(salida,modulonombre)
                    flag2=1
                # escribimos la descripción del atributo como código
                salida=saltolin+ccodestar+saltolin+"//"+descripcion
                anadirlinea(salida,modulonombre)
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
            anadirlinea(linea_+saltolin+ccodend+saltolin,modulonombre)
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
                anadirlinea(salida,modulonombre)
                flag1=1
            # escribimos la descripción del macro como código
            salida=saltolin+ccodestar+saltolin+"//"+descripcion
            anadirlinea(salida,modulonombre)
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
            anadirlinea(linea_+saltolin+ccodend+saltolin,modulonombre)
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
                anadirlinea(salida,modulonombre)
                flag1=1
            # escribimos la descripción del macro como código
            salida=saltolin+ccodestar+saltolin+"//"+descripcion
            anadirlinea(salida,modulonombre)
            flag=1
        #fin si se encuentra
################################################################################
def cBuscarOper(ficheroentradaoper,modulonombre):
    #Encabezado
    salida=saltolin+h5+espacio+"Desglose de operaciones"+saltolin
    anadirlinea(salida,modulonombre)
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
        #si se encuentra
        if(loccom):
            tag = re.split("//>", linea)
            descripcion=tag[1]
            # escribimos el comentario
            salida=descripcion
            anadirlinea(salida,modulonombre)
        if(loccod):
            tag = re.split("//<", linea)
            descripcion=tag[0]
            # escribimos el comentario
            salida=descripcion.strip()
            anadirLineaCodigo(salida,modulonombre)
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
        #si se encuentra
        if(loccom):
            tag = re.split("#>", linea)
            descripcion=tag[1]
            # escribimos el comentario
            salida=descripcion
            anadirlinea(salida,modulonombre)
        if(loccod):
            tag = re.split("#<", linea)
            descripcion=tag[0]
            # escribimos el comentario
            salida=descripcion.strip()
            anadirLineaCodigo(salida,modulonombre,"py")
################################################################################
def anadirlinea(texto,modulonombre):
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
def main():
    print("Comienzo.....")
    mod_nom=sys.argv[1]
    #Tratamiento de código C, enviamos por parámetro el .h pero se trata
    #el punto .h y .c
    if(mod_nom.endswith("h")):
        modulonombre=mod_nom[:-2]#Imagen.h -> Imagen
        ficheroentrada=modulonombre+".h"
        ficheroentradaoper=modulonombre+".c"
        cCrearDoc(modulonombre)
        headerBuscarEntidades(ficheroentrada,modulonombre)
        cBuscarOper(ficheroentradaoper,modulonombre)
    #Tratamiento de código Python, enviamos por parámetro el. py pero se trata
    if(mod_nom.endswith("y")):
        modulonombre=mod_nom[:-3]#Imagen.py -> Imagen
        ficheroentradaoper=modulonombre+".py"
        crearDoc(modulonombre)
        pyBuscarOper(ficheroentradaoper,modulonombre)
    print("Fin.....")
################################################################################
if __name__ == '__main__':
    main()
################################################################################