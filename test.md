[TOC]
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
*Sello temporal:17-Apr-2020 (20:39:30.768403)*
*Documentado con code2markdown, https://github.com/diegostreetbob/code2markdown*