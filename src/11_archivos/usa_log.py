
import log

# Constante que contiene el nombre del archivo de log a utilizar
ARCHIVO_LOG = "mi_log.txt"

def main():
    # Al comenzar, abrir el log
    archivo_log = log.abrir(ARCHIVO_LOG)
    # ...
    # Hacer cosas que pueden dar error
    if error:
        log.guardar(archivo_log, "ERROR: "+error)
    # ...
    # Finalmente cerrar el archivo
    log.cerrar(archivo_log)

main()
