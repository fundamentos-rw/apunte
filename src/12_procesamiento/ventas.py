import csv

def ventas_clientes_mes(archivo_ventas):
    """Calcula totales por mes, año y cliente a partir de la
    información almacenada en el archivo CSV, que debe tener
    el formato: cliente,año,mes,día,venta"""

    with open(archivo_ventas) as f:
        ventas_csv = csv.reader(f)

        item = next(ventas_csv, None)
        total = 0

        while item:
            # Inicialización para el bucle de cliente
            cliente = item[0]
            total_cliente = 0
            print(f"Cliente: {cliente}")

            while item and item[0] == cliente:
                # Inicialización para el bucle de año
                año = item[1]
                total_año = 0
                print(f"\tAño: {año}")

                while item and item[0] == cliente and item[1] == año:
                    mes, monto = item[2], float(item[4])
                    print(f"\t\tVentas del mes {mes}: {monto:.2f}")
                    total_año += monto

                    # Siguiente registro
                    item = next(ventas_csv, None)

                # Final del bucle de año
                print(f"\tTotal para el año {año}: {total_año:.2f}")
                total_cliente += total_año

            # Final del bucle de cliente
            print(f"Total para el cliente {cliente}: {total_cliente:.2f}\n")
            total += total_cliente

        # Final del bucle principal
        print(f"Total general: {:total.2f}")
