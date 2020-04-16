# code2markdown

Parser para proyectos desarrollados en `c` y `python` nos permite que el trabajo de documentación del código pase directamente a lenguaje de marcas, en este caso *Markdown*, en adelante **md**

Antes de nada es necesario tener algunos conceptos básicos de *Markdown*.



# Uso para Python

## Etiquetas

* **#>** línea    -> Extrae línea, línea puede contener cualquier instrucción de **md**
* línea de código **#<**   ->Extrae línea de código y la representa dentro de **md** como una línea de código con sintaxis `python`

### Ejemplos

***

Este código en `python` :

```python
#>### main() del programa
def main():
    #>#### Creación del socket
	#>Para la creación usamos estas tres líneas:
    serverSocket = socket(AF_INET, SOCK_STREAM)#<
    serverSocket.bind((gethostname(), 8801))#<
	serverSocket.listen(10)#<
    while True:
	    #>> Posteriormente quedamos a la espera de conexión por parte de un cliente.
        print('1.Activo y preparado para recibir conexiones\n')
        connectionSocket, addr = serverSocket.accept()#<
        try:
          mensaje = connectionSocket.recv(1024)
          mensajeclte = " _Hola soy tu servidor_"
          print("2.Mensaje recibido desde el cliente: ", mensaje)
          print("3.Respondiendo a cliente con: ", mensajeclte)
          connectionSocket.send(mensajeclte.encode())
          #cerramos la conexión
          connectionSocket.shutdown(SHUT_RDWR)
          connectionSocket.close()
          print("4.Cliente desconectado....\n")
		#>Si ocurre un error:
        except IOError:
            connectionSocket.shutdown(SHUT_RDWR)#<
            connectionSocket.close()#<
	#>Al acabar siempre cerramos la conexión
    serverSocket.close()#<
    sys.exit(0)
	#>***
```

Produce la siguiente salida en **md**:

## Fuente: testpython

### main() del programa

#### Creación del socket

Para la creación usamos estas tres líneas:
```python
serverSocket = socket(AF_INET, SOCK_STREAM)
```
```python
serverSocket.bind((gethostname(), 8801))
```
```python
serverSocket.listen(10)
```
> Posteriormente quedamos a la espera de conexión por parte de un cliente.
```python
connectionSocket, addr = serverSocket.accept()
```
Si ocurre un error:
```python
connectionSocket.shutdown(SHUT_RDWR)
```
```python
connectionSocket.close()
```
Al acabar siempre cerramos la conexión
```python
serverSocket.close()
```
***

Como observación se puede apreciar como **#>>** en la línea 9 genera un blockquote, recordemos que un blockquote es esto:

> Esto es un blockquote.

Es un ejemplo de introducción de sintaxis **md**, la sintaxis estándar para un blockquote es >+espacio+texto en este caso usamos nuestro comando de extracción de línea #>+sintaxis estándar para un blockquote.

Otros ejemplo:

* Línea 1 donde extraeremos un encabezado **h3** que en sintaxis **md** es ###+espacio+texto.
* Línea 3 donde extraeremos un encabezado **h4** que en sintaxis **md** es ####+espacio+texto.
* Línea 29 donde extraeremos una línea que en sintaxis **md** es ***+enter.

En resumen cualquier etiqueta **#>**+sintaxis **md** será representada como código **md** en el documento final.

#### Ejemplo de uso

Colocamos `code2markdown.py` en el mismo directorio donde este el archivo con el código comentado, en este ejemplo hemos usado un archivo llamado `testpython.py` hemos ejecutado así:

```bash
PS D:\SynologyDrive\SynologyDrive\GitHub\code2markdown> py -3 code2markdown.py testpython.py
```

Nos genera el archivo **md** llamado `testpython.md`

***

# Uso para lenguaje C

Para lenguaje C tenemos dos tipo de etiquetas:

1. **Etiquetas para el header .h**

   * **//@mac** descripción de la macro

     Ejemplo de uso:

     ```c
     //@mac descripción de la macro
     #define x 1
     ```

   * **//@glob** descripción de la variable global

     Ejemplo de uso:

     ```c
     //@glob descripción de la variable global
     enum tipo {binary,erodedH,edged};
     ```

   * **//@ent** descripción de la entidad, se podría usar con typedef o structs

     Ejemplo de uso:

     ```c
     //@ent descripción de la entidad, se podría usar con typedef o structs
     typedef struct imagen{
         
     }
     ```

     * Dentro de entidad tenemos **//@atr** y **//@oper** que se usaría así:

       ```c
       typedef struct imagen{
         //@atr filas de la imagen
         int fil;
         //@atr columnas de la imagen
         int col;
         //@atr columnas de la mascara, si aplica
         unsigned char col_masc;
         //@atr puntero a imagen
         unsigned char *imagen;
         //@oper método para imprimir
         void (*print)();
         //@oper método para liberar memoria
         void (*borrar)();
       }Imagen;
       ```

2. Etiquetas para el .c
   * En este caso el funcionamiento es el mismo que el descrito para `python` aunque las etiquetas difieren algo, concretamente quedan así:
     * **//>** línea    -> Extrae línea, línea puede contener cualquier instrucción de **md**
     * línea de código **//<**   ->Extrae línea de código y la representa dentro de **md** como una línea de código con sintaxis `c`

### Ejemplos

El siguiente código de los archivos `.h` y `.c`:

`test.h`

```c
//@mac macro para lo que sea
#define x 1
//@mac macro para lo que sea
#define x 2
//@glob variable global necesaria para el control de errores
enum tipo {binary,erodedH,edged};
//@ent Imagen descripción de la entidad
typedef struct imagen{
  //@atr filas de la imagen
  int fil;
  //@atr columnas de la imagen
  int col;
  //@atr columnas de la mascara, si aplica
  unsigned char col_masc;
  //@atr puntero a imagen
  unsigned char *imagen;
  //@oper método para imprimir
  void (*print)();
  //@oper método para liberar memoria
  void (*borrar)();
}Imagen;
```

`test.c`

```c
#include "Imagen.h"
//>Variable global necesaria para el control de excepciones
extern jmp_buf buf;//<
//>Variable global necesaria para el control de excepciones 
extern enum STATE state;//<
/*
//>***
void imagenImprimir(Imagen *img)//<
//>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when 
//>printer took a galley of type and scrambled it to make a type specimen book. It 
//>only five centuries, but also the leap into electronic typesetting, remaining  
//>It was popularised in the 1960s with the release of Letraset sheets containing 
//Ejemplo de uso de sintaxis de markdown para generar listas  
//>* Elemento1.
//>* Elemento2.
//>  * Elemento2.1
//>
//>Parámetros:
//>* **[in]** Imagen
//>* **[out]** void 
*/
void imagenImprimir(Imagen *img)
{
  int test=0;
  for(int fil=0; fil<img->fil; fil++)
  {
    for(int col=0; col<img->col; col++)
    {
      test=printf("%hhu|", *(img->imagen+(fil*img->col)+col));
        THROWandLOG(test<0,state=stStdError)//testeado
      //para vaciar el buffer,si no no muestra todos los caracteres
      test=fflush(stdout);
        THROWandLOG(test!=0,state=stStdError)//testeado
    }
    test=printf("\n");
        THROWandLOG(test<0,state=stStdError)//testeado
  }
}
/*
//>***
Imagen nuevaImagen(int nfil,int ncol,jmp_buf buf)//<
//>Parámetros:
//>* **[in]** filas, columnas, buf
//>* **[out]** Imagen
//>
//>Ejemplo de uso para declarar e inicializar una imagen de 10x10
Imagen img=nuevaImagen(10,10,jmp_buf buf)//<
*/
Imagen nuevaImagen(int nfil,int ncol,jmp_buf buf)
{
  Imagen img;
  img.print=&imagenImprimir;
  img.borrar=&imagenLiberar;
  img.fil=nfil;
  img.col=ncol;
  //>Asignamos memoria dinámicamente 
  img.imagen=(unsigned char*) malloc(img.fil*img.col*sizeof(unsigned char));//<
  //>Si hay error enviamos excepción
    THROWandLOG(!img.imagen,state=stNull)//<//salta si es un null y avisa de null
  int *res=memset(img.imagen,0,img.fil*img.col);
    THROWandLOG(!res,state=stNull)//salta si es un null y avisa de null
  return img;
}
//>***
```

Produce la siguiente salida en **md**:

## Fuente: test

### Entidades

#### Imagen
```c
// descripción de la entidad
typedef struct imagen
```

##### Atributos
```c
// filas de la imagen
  int fil
```

```c
// columnas de la imagen
  int col
```

```c
// columnas de la mascara, si aplica
  unsigned char col_masc
```

```c
// puntero a imagen
  unsigned char *imagen
```

##### Operaciones
[Ir a desglose de operaciones](#Desglose de operaciones)
```c
// método para imprimir
  void (*print)()
```

```c
// método para liberar memoria
  void (*borrar)()
```

##### Macros
```c
// macro para lo que sea
#define x 
```

```c
// macro para lo que sea
#define x 
```

##### Variables globales
```c
// variable global necesaria para el control de errores
enum tipo {binary,erodedH,edged}
```

##### Desglose de operaciones
Variable global necesaria para el control de excepciones
```c
extern jmp_buf buf;
```
Variable global necesaria para el control de excepciones 
```c
extern enum STATE state;
```
***
```c
void imagenImprimir(Imagen *img)
```
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages.
* Elemento1.
* Elemento2.
  * Elemento2.1

Parámetros:
* **[in]** Imagen
* **[out]** void 
***
```c
Imagen nuevaImagen(int nfil,int ncol,jmp_buf buf)
```
Parámetros:
* **[in]** filas, columnas, buf
* **[out]** Imagen

Ejemplo de uso para declarar e inicializar una imagen de 10x10
```c
Imagen img=nuevaImagen(10,10,jmp_buf buf)
```
Asignamos memoria dinámicamente 
```c
img.imagen=(unsigned char*) malloc(img.fil*img.col*sizeof(unsigned char));
```
Si hay error enviamos excepción
```c
THROWandLOG(!img.imagen,state=stNull)
```
***

#### Ejemplo de uso

Colocamos `code2markdown.py` en el mismo directorio donde este el archivo con el código comentado, en este ejemplo hemos usado los archivos `test.h y test.c` hemos ejecutado así:

```bash
PS D:\SynologyDrive\SynologyDrive\GitHub\code2markdown> py -3 code2markdown.py test.h
```

**Observar** que como argumento solo pasamos `test.h`

Nos genera el archivo **md** llamado `test.md

Para su testeo se adjuntan todos los fichero empleados para estas pruebas por si deseas reproducirlos.

