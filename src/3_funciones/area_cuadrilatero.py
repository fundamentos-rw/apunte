def norma(x, y, z):
    return (x**2 + y**2 + z**2)**0.5

print('norma', norma(3, 2, -4))

def diferencia(x1, y1, z1, x2, y2, z2):
    return (x1 - x2, y1 - y2, z1 - z2)

print('diferencia', diferencia(8, 7, -3, 5, 3, 2))

def producto_vec(x1, y1, z1, x2, y2, z2):
    return (
        y1 * z2 - z1 * y2,
        z1 * x2 - x1 * z2,
        x1 * y2 - y1 * x2,
    )

print('producto_vec', producto_vec(1, 4, -2, 3, -1, 0))

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    d1x, d1y, d1z = diferencia(x2, y2, z2, x1, y1, z1)
    d2x, d2y, d2z = diferencia(x3, y3, z3, x1, y1, z1)
    px, py, pz = producto_vec(d1x, d1y, d1z, d2x, d2y, d2z)
    return norma(px, py, pz) / 2

print('area_triangulo', area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0))

def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    return area_triangulo(x1, y1, 0, x2, y2, 0, x3, y3, 0) \
        + area_triangulo(x2, y2, 0, x3, y3, 0, x4, y4, 0)

print('area_cuadrilatero', area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5))
