[TOC]
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
