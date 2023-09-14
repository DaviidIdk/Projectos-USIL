# Importar el módulo math
import math

# Definir la clase Figura
class Figura:
    def dibujar(self, canvas):
        # Método abstracto que debe ser implementado por las subclases.
        pass

# Definir la clase Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, pmin, pmax):
        # Inicializar un rectángulo con los puntos mínimo y máximo.
        super().__init__()
        self.pmin = pmin
        self.pmax = pmax

    def dibujar(self, canvas):
        # Dibujar el rectángulo en el canvas.
        for y in range(self.pmin[1], self.pmax[1] + 1):
            for x in range(self.pmin[0], self.pmax[0] + 1):
                if y == self.pmin[1] or y == self.pmax[1] or x == self.pmin[0] or x == self.pmax[0]:
                    canvas.grid[y][x] = '*'
                else:
                    canvas.grid[y][x] = ' '

# Definir la clase Linea que hereda de Figura
class Linea(Figura):
    def __init__(self, pmin, pmax):
        # Inicializar una línea con los puntos mínimo y máximo.
        super().__init__()
        self.pmin = pmin
        self.pmax = pmax

    def dibujar(self, canvas):
        # Dibujar la línea en el canvas utilizando el algoritmo de Bresenham.
        dx = self.pmax[0] - self.pmin[0]
        dy = self.pmax[1] - self.pmin[1]
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            canvas.grid[self.pmin[1]][self.pmin[0]] = '*'
        else:
            x_inc = dx / steps
            y_inc = dy / steps
            x = self.pmin[0]
            y = self.pmin[1]
            for _ in range(steps):
                canvas.grid[round(y)][round(x)] = '*'
                x += x_inc
                y += y_inc

# Definir la clase Triangulo que hereda de Figura
class Triangulo(Figura):
    def __init__(self, p1, p2, p3):
        # Inicializar un triángulo con los puntos p1, p2 y p3 como vértices.
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def dibujar(self, canvas):
        # Obtener los vértices del triángulo
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3

        # Dibujar los lados del triángulo utilizando la clase Linea
        linea1 = Linea(self.p1, self.p2)
        linea2 = Linea(self.p2, self.p3)
        linea3 = Linea(self.p3, self.p1)
        linea1.dibujar(canvas)
        linea2.dibujar(canvas)
        linea3.dibujar(canvas)

        # Dibujar solo los bordes externos del triángulo
        canvas.grid[y1][x1] = '*'
        canvas.grid[y2][x2] = '*'
        canvas.grid[y3][x3] = '*'

    @staticmethod
    def esta_dentro(x, y, x1, y1, x2, y2, x3, y3):
        # Comprobar si un punto (x, y) está dentro de un triángulo definido por sus vértices
        d1 = (x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)
        d2 = (x - x3) * (y2 - y3) - (x2 - x3) * (y - y3)
        d3 = (x - x1) * (y3 - y1) - (x3 - x1) * (y - y1)
        return (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0)

# Definir la clase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, centro, radio):
        # Inicializar un círculo con el centro y el radio.
        super().__init__()
        self.centro = centro
        self.radio = radio

    def dibujar(self, canvas):
        # Dibujar el círculo en el canvas utilizando el algoritmo de Bresenham para el trazado de círculos.
        cx, cy = self.centro
        r = self.radio

        x = 0
        y = r
        p = 1 - r

        self.plot_points(canvas, cx, cy, x, y)

        while x < y:
            x += 1
            if p < 0:
                p += 2 * x + 1
            else:
                y -= 1
                p += 2 * (x - y) + 1
            self.plot_points(canvas, cx, cy, x, y)

    @staticmethod
    def plot_points(canvas, cx, cy, x, y):
        # Dibujar los puntos del círculo en el canvas
        canvas.grid[cy + y][cx + x] = '*'
        canvas.grid[cy + y][cx - x] = '*'
        canvas.grid[cy - y][cx + x] = '*'
        canvas.grid[cy - y][cx - x] = '*'
        canvas.grid[cy + x][cx + y] = '*'
        canvas.grid[cy + x][cx - y] = '*'
        canvas.grid[cy - x][cx + y] = '*'
        canvas.grid[cy - x][cx - y] = '*'

# Definir la clase Canvas
class Canvas:
    def __init__(self, width, height):
        # Inicializar el canvas con el ancho y alto dados
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]

    def draw_figure(self, figure):
        # Dibujar una figura en el canvas
        figure.dibujar(self)

    def clear(self):
        # Limpiar el canvas
        self.grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def show(self):
        # Mostrar el contenido del canvas en la consola
        print(' '.join(str(i % 10) for i in range(1, self.width + 1)))
        for y, row in enumerate(self.grid, start=1):
            print(str(y % 10) + ' '.join(row) + ' ' + str(y % 10))
        print(' '.join(str(i % 10) for i in range(1, self.width + 1)))
