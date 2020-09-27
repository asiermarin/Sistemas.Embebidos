#
# EJEMPLO DE LEER Y ESCRIBIR FICHEROS
#

def main():
  PATH_DIR_INTERIOR = "./textfile.txt"

  # Abre un fichero para escribir y lo crea si no existe
  f = open(PATH_DIR_INTERIOR,"w+")
  
  # Abrir el ficher para aniadir texto al final (append)
  # f = open("textfile.txt","a+")

  # Escribir algunas lineas al fichero
  for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
  
  # Cerrar el fichero
  f.close()
  
  # Abrir el fichero y leer el contenido
  f = open(PATH_DIR_INTERIOR,"r")
  if f.mode == 'r': # comprobar que antes hemos abierto el fichero
    # usa la funcion read() para leer todo el fichero
    # contents = f.read()
    # print (contents)
    
    fl = f.readlines() # readlines lee las lineas individuales del archivo
    for x in fl:
      print (x)
    
if __name__ == "__main__":
  main()
