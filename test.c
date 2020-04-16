#include "Imagen.h"
//>Variable global necesaria para el control de excepciones
extern jmp_buf buf;//<
//>Variable global necesaria para el control de excepciones 
extern enum STATE state;//<
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
