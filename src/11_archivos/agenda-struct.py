import struct, os, datetime

FORMATO_FECHA = "%d/%m/%Y"

RUTA = "agenda.dat"
STRUCT_CANTIDAD_ITEMS = struct.Struct("I") # 4 bytes, entero sin signo
STRUCT_LONGITUD_CADENA = struct.Struct("H") # 2 bytes, entero sin signo
STRUCT_FECHA = struct.Struct("BBH") # 1 byte, 1 byte, 2 bytes, enteros sin signo
CODIFICACION_CADENAS = 'utf-8'

def cargar_agenda(ruta):
    """Carga todos los datos del archivo en una lista y la devuelve."""
    agenda = []
    if not os.path.exists(ruta):
        return agenda
    with open(ruta, "rb") as f:
        (n,) = STRUCT_CANTIDAD_ITEMS.unpack(f.read(STRUCT_CANTIDAD_ITEMS.size))
        for _ in range(n):
            nombre = leer_cadena(f)
            apellido = leer_cadena(f)
            telefono = leer_cadena(f)
            d, m, y = STRUCT_FECHA.unpack(f.read(STRUCT_FECHA.size))
            nacimiento = datetime.date(y, m, d)
            agenda.append((nombre, apellido, telefono, nacimiento))
    return agenda

def guardar_agenda(agenda, ruta):
    """Guarda la agenda en el archivo."""
    with open(ruta, "wb") as f:
        f.write(STRUCT_CANTIDAD_ITEMS.pack(len(agenda)))
        for item in agenda:
            nombre, apellido, telefono, nacimiento = item
            escribir_cadena(f, nombre)
            escribir_cadena(f, apellido)
            escribir_cadena(f, telefono)
            d, m, y = nacimiento.day, nacimiento.month, nacimiento.year
            f.write(STRUCT_FECHA.pack(d, m, y))

def escribir_cadena(f, nombre):
    """Escribe una cadena de longitud variable en el archivo"""
    b = bytes(nombre, CODIFICACION_CADENAS)
    f.write(STRUCT_LONGITUD_CADENA.pack(len(b)))
    f.write(b)

def leer_cadena(f):
    """Lee una cadena de longitud variable del archivo"""
    (n,) = STRUCT_LONGITUD_CADENA.unpack(f.read(STRUCT_LONGITUD_CADENA.size))
    b = f.read(n)
    return b.decode(CODIFICACION_CADENAS)

def leer_busqueda():
    """Solicita al usuario nombre y apellido y los devuelve."""
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    return nombre, apellido

def buscar(nombre, apellido, agenda):
    """Busca el primer item que coincida con nombre y con apellido."""
    for item in agenda:
        if nombre in item[0] and apellido in item[1]:
            return item
    return None

def menu_alta(nombre, apellido, agenda):
    """Pregunta si se desea ingresar un nombre y apellido y
       de ser así, pide los datos al usuario."""
    print(f"No se encuentra {nombre} {apellido} en la agenda.")
    confirmacion = input("¿Desea ingresarlo? (s/n): ")
    if confirmacion.lower() != "s":
        return
    telefono = input("Telefono: ")
    nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
    agenda.append([nombre, apellido, telefono, cadena_a_fecha(nacimiento)])

def mostrar_item(item):
    """Muestra por pantalla un item en particular."""
    nombre, apellido, telefono, nacimiento = item
    print()
    print(f"{nombre} {apellido}")
    print(f"Telefono: {telefono}")
    print(f"Fecha de nacimiento (dd/mm/aaaa): {fecha_a_cadena(nacimiento)}")
    print()

def menu_item():
    """Muestra por pantalla las opciones disponibles para un item
       existente."""
    o = input("b: borrar, m: modificar, ENTER para continuar (b/m): ")
    return o.lower()

def modificar(viejo, nuevo, agenda):
    """Reemplaza el item viejo con el nuevo, en la lista datos."""
    indice = agenda.index(viejo)
    agenda[indice] = nuevo

def menu_modificacion(item, agenda):
    """Solicita al usuario los datos para modificar una entrada."""
    nombre = input("Nuevo nombre: ")
    apellido = input("Nuevo apellido: ")
    telefono = input("Nuevo teléfono: ")
    nacimiento = input("Nueva fecha de nacimiento (dd/mm/aaaa): ")
    modificar(item, [nombre, apellido, telefono, cadena_a_fecha(nacimiento)], agenda)

def baja(item, agenda):
    """Elimina un item de la lista."""
    agenda.remove(item)

def confirmar_salida():
    """Solicita confirmación para salir"""
    confirmacion = input("¿Desea salir? (s/n): ")
    return confirmacion.lower() == "s"

def agenda():
    """Función principal de la agenda.
    Carga los datos del archivo, permite hacer búsquedas, modificar
    borrar, y al salir guarda. """
    agenda = cargar_agenda(RUTA)
    while True:
        nombre, apellido = leer_busqueda()
        if nombre + apellido == "":
            if confirmar_salida():
                break
        item = buscar(nombre, apellido, agenda)
        if not item:
            menu_alta(nombre, apellido, agenda)
            continue
        mostrar_item(item)
        opcion = menu_item()
        if opcion == "m":
            menu_modificacion(item, agenda)
        elif opcion == "b":
            baja(item, agenda)
    guardar_agenda(agenda, RUTA)

def fecha_a_cadena(fecha):
    """Convierte una fecha de tipo `date` a una cadena"""
    return fecha.strftime(FORMATO_FECHA)

def cadena_a_fecha(s):
    """Convierte una cadena a una fecha de tipo `date`"""
    return datetime.datetime.strptime(s, FORMATO_FECHA).date()

agenda()
