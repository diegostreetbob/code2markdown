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
