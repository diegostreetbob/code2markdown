# code2markdown

Parser para proyectos desarrollados en `c` y `python` o cualquier lenguaje que utilice como inicio de comentarios `//` .

Nos permite que el trabajo de documentación del código pase directamente a lenguaje de marcas, en este caso *Markdown*, en adelante **md**

Con las etiquetas de `code2markdown`podemos introducir cualquier sintaxis de **md** en los comentarios de nuestro código de modo que al ejecutar `code2markdown` tendremos un documento final en formato **md** , ampliamente usado en Github, entorno académico, blogs, etc....

Antes de nada es **necesario e imprescindible** tener algunos conceptos básicos de *Markdown*.

Recomiendo usar Typora https://typora.io/ como entorno editor de **md** para dar el acabado final a nuestros documentos, e ir viendo como quedan, incluye hojas de estilos `css`totalmente personalizables, permite exportación a pdf, html, etc.

# Uso para Python

## Etiquetas

* **#>** Línea    -> Extrae línea, línea puede contener cualquier instrucción de **md**

  * Ejemplo:  **#>Esto es un comentario*** en **md** se mostrará como: “Esto es un comentario”, sin las dobles comillas.

* Línea de código **#<**   ->Extrae línea de código y la representa dentro de **md** como un bloque de código con sintaxis `python`

  * Ejemplo: **serverSocket = socket(AF_INET, SOCK_STREAM)#<** en **md** se mostrará como un bloque de código:

    ```python
    serverSocket = socket(AF_INET, SOCK_STREAM)
    ```

* Línea de código **#<<**   ->Extrae línea de código y la representa dentro de **md** como código en línea

  * Ejemplo: **serverSocket = socket(AF_INET, SOCK_STREAM)#<<** se mostrará como:

    `serverSocket = socket(AF_INET, SOCK_STREAM)`

### Ejemplos

***

Este código en `python` :

```python
################################################################################
#>### main() del programa
def main():
    #>#### Creación del socket
	#>Para la creación usamos estas tres líneas:
    serverSocket = socket(AF_INET, SOCK_STREAM)#<<
    serverSocket.bind((gethostname(), 8801))#<<
	serverSocket.listen(10)#<<
    while True:
	    #>> Posteriormente quedamos a la espera de conexión por parte de un cliente.
        print('1.Activo y preparado para recibir conexiones\n')
        connectionSocket, addr = serverSocket.accept()#<
        try:
          mensaje = connectionSocket.recv(1024)#<<
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
            connectionSocket.shutdown(SHUT_RDWR)#<<
            connectionSocket.close()#<<
	#>Al acabar siempre cerramos la conexión
    serverSocket.close()#<<
    sys.exit(0)
	#>***
################################################################################
```

Produce la siguiente salida en **md**:

## Fuente: testpython.py
### main() del programa
#### Creación del socket
Para la creación usamos estas tres líneas:
`serverSocket = socket(AF_INET, SOCK_STREAM)`

`serverSocket.bind((gethostname(), 8801))`

`serverSocket.listen(10)`

> Posteriormente quedamos a la espera de conexión por parte de un cliente.
```python
connectionSocket, addr = serverSocket.accept()
```
`mensaje = connectionSocket.recv(1024)`

Si ocurre un error:
`connectionSocket.shutdown(SHUT_RDWR)`

`connectionSocket.close()`

Al acabar siempre cerramos la conexión
`serverSocket.close()`

***
*Sello temporal:17-Apr-2020 (19:59:36.054203)*
*Documentado con code2markdown, https://github.com/diegostreetbob/code2markdown*



Como observación se puede apreciar como **#>>** en la línea 10 genera un blockquote, recordemos que un blockquote es esto:

> Esto es un blockquote.

Es un ejemplo de introducción de sintaxis **md**, la sintaxis estándar para un blockquote es >+espacio+texto en este caso usamos nuestro comando de extracción de línea #>+sintaxis estándar para un blockquote.

Otros ejemplo:

* Línea 2 donde extraeremos un encabezado **h3** que en sintaxis **md** es ###+espacio+texto.
* Línea 4 donde extraeremos un encabezado **h4** que en sintaxis **md** es ####+espacio+texto.
* Línea 30 donde extraeremos una línea que en sintaxis **md** es ***+enter.

En resumen cualquier etiqueta **#>**+sintaxis **md** será representada como código **md** en el documento final.

#### Ejemplo de uso

Colocamos `code2markdown.py` en el mismo directorio donde este el archivo con el código, en este ejemplo he usado un archivo llamado `testpython.py` que se adjunta al proyecto, desde PowerShell se ha ejecutado así:

```bash
\code2markdown> py -3 code2markdown.py 3 testpython.py 
```

**Argumento 1:  tiene que ser 3 cuando vayamos a aplicar a archivos.py**

Nos genera el archivo **md** llamado `testpython.md`

***

# Uso para lenguaje C u otros con comentarios del tipo //

## Etiquetas

* **//>** Línea    -> Extrae línea, línea puede contener cualquier instrucción de **md**

  * Ejemplo:  **//>Esto es un comentario*** en **md** se mostrará como: “Esto es un comentario”, sin las dobles comillas.

* Línea de código **//<**   ->Extrae línea de código y la representa dentro de **md** como un bloque de código con sintaxis `c`

  * Ejemplo: **serverSocket = socket(AF_INET, SOCK_STREAM)//<** en **md** se mostrará como un bloque de código:

    ```python
    serverSocket = socket(AF_INET, SOCK_STREAM)
    ```

* Línea de código **//<<**   ->Extrae línea de código y la representa dentro de **md** como código en línea

  * Ejemplo: **serverSocket = socket(AF_INET, SOCK_STREAM)#<<** se mostrará como:

    `serverSocket = socket(AF_INET, SOCK_STREAM)`

### Ejemplos

***

Para este código:

```c
#include "Imagen.h"
//>Variables globalles necesarias para el control de excepciones
extern jmp_buf buf;//<<
extern enum STATE state;//<<
/*
//>***
void imagenImprimir(Imagen *img)//<
//>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown 
//>printer took a galley of type and scrambled it to make a type specimen book. It has survived not 
//>only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
//>It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages.
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
Imagen img=nuevaImagen(10,10,jmp_buf buf)//<<
*/
Imagen nuevaImagen(int nfil,int ncol,jmp_buf buf)
{
  Imagen img;
  img.print=&imagenImprimir;
  img.borrar=&imagenLiberar;
  img.fil=nfil;
  img.col=ncol;
  //>Asignamos memoria dinámicamente 
  img.imagen=(unsigned char*) malloc(img.fil*img.col*sizeof(unsigned char));//<<
  //>Si hay error enviamos excepción
    THROWandLOG(!img.imagen,state=stNull)//<<
  int *res=memset(img.imagen,0,img.fil*img.col);
    THROWandLOG(!res,state=stNull)//salta si es un null y avisa de null
  return img;
}
//>***
```

Produce la siguiente salida en **md**:

## Fuente: test.c

##### Desglose de operaciones

Variables globalles necesarias para el control de excepciones
`extern jmp_buf buf;`

`extern enum STATE state;`

***

```c
void imagenImprimir(Imagen *img)
```

Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown 
printer took a galley of type and scrambled it to make a type specimen book. It has survived not 
only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages.

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
`Imagen img=nuevaImagen(10,10,jmp_buf buf)`

Asignamos memoria dinámicamente 
`img.imagen=(unsigned char*) malloc(img.fil*img.col*sizeof(unsigned char));`

Si hay error enviamos excepción
`THROWandLOG(!img.imagen,state=stNull)`

***

*Sello temporal:17-Apr-2020 (20:28:15.818518)*
*Documentado con code2markdown, https://github.com/diegostreetbob/code2markdown*

#### Ejemplo de uso

Colocamos `code2markdown.py` en el mismo directorio donde este el archivo con el código, en este ejemplo he usado un archivo llamado `test.c` que se adjunta al proyecto, desde PowerShell se ha ejecutado así:

```bash
\code2markdown> py -3 code2markdown.py 1 test.c  
```

**Argumento 1:  tiene que ser 1 cuando vayamos a aplicar a archivos.c y otros compatibles con comentarios del tipo //**

Nos genera el archivo **md** llamado `test.md`

# Uso para lenguaje C(Avanzado)

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

2. Etiquetas para el .c [ver aquí](#Uso para lenguaje C u otros con comentarios del tipo //)

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
//>Variables globalles necesarias para el control de excepciones
extern jmp_buf buf;//<<
extern enum STATE state;//<<
/*
//>***
void imagenImprimir(Imagen *img)//<
//>Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown 
//>printer took a galley of type and scrambled it to make a type specimen book. It has survived not 
//>only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
//>It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages.
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
Imagen img=nuevaImagen(10,10,jmp_buf buf)//<<
*/
Imagen nuevaImagen(int nfil,int ncol,jmp_buf buf)
{
  Imagen img;
  img.print=&imagenImprimir;
  img.borrar=&imagenLiberar;
  img.fil=nfil;
  img.col=ncol;
  //>Asignamos memoria dinámicamente 
  img.imagen=(unsigned char*) malloc(img.fil*img.col*sizeof(unsigned char));//<<
  //>Si hay error enviamos excepción
    THROWandLOG(!img.imagen,state=stNull)//<<
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

Variables globalles necesarias para el control de excepciones
`extern jmp_buf buf;`

`extern enum STATE state;`

***

```c
void imagenImprimir(Imagen *img)
```

Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown 
printer took a galley of type and scrambled it to make a type specimen book. It has survived not 
only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages.

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
`Imagen img=nuevaImagen(10,10,jmp_buf buf)`

Asignamos memoria dinámicamente 
`img.imagen=(unsigned char*) malloc(img.fil*img.col*sizeof(unsigned char));`

Si hay error enviamos excepción
`THROWandLOG(!img.imagen,state=stNull)`

***

*Sello temporal:17-Apr-2020 (20:32:53.780990)*
*Documentado con code2markdown, https://github.com/diegostreetbob/code2markdown*

#### Ejemplo de uso

Colocamos `code2markdown.py` en el mismo directorio donde este el archivo con el código, en este ejemplo he usado un archivo llamado `test.h` que se adjunta al proyecto, desde PowerShell se ha ejecutado así:

```bash
\code2markdown> py -3 code2markdown.py 2 test.h 
```

**Argumento 1:  tiene que ser 2 cuando vayamos a usar este modo especial que solo sirve para lenguaje c y en el directorio ha de estar un .h y un .c**

**Observar** que como argumento solo pasamos `test.h`

Nos genera el archivo **md** llamado test.md

Para su testeo se adjuntan todos los ficheros empleados para estas pruebas por si deseas reproducirlos.

No dudes en contactar para cualquier ayuda o sugerencia.