from figuras import *

def main():
    canvas = Canvas(20, 20)
    figuras = []

    print("Welcome to the gimp xyz")
    print(canvas.show())
    print("Operations: Show, Add, Delete, Rotate, Resize")

    while True:
        operacion = input("Ingrese una operación (Show, Add, Delete, Rotate o Resize): ")
        operacion = operacion.capitalize()

        if operacion == "Add":
            tipo = input("Ingrese el tipo de figura (Rectangle, Triangle, Line o Circle): ")
            tipo = tipo.capitalize()

            if tipo == "Rectangle":
                puntos = input("Ingrese los puntos de inicio y fin del rectángulo (x1,y1,x2,y2): ")
                x1, y1, x2, y2 = map(int, puntos.split(','))
                figura = Rectangulo((x1, y1), (x2, y2))
                figuras.append(figura)
                print("Figura agregada exitosamente.")

            elif tipo == "Triangle":
                puntos = input("Ingrese los puntos del triángulo (x1,y1,x2,y2,x3,y3): ")
                x1, y1, x2, y2, x3, y3 = map(int, puntos.split(','))
                figura = Triangulo((x1, y1), (x2, y2), (x3, y3))
                figuras.append(figura)
                print("Figura agregada exitosamente.")

            elif tipo == "Line":
                puntos = input("Ingrese los puntos de inicio y fin de la línea (x1,y1,x2,y2): ")
                x1, y1, x2, y2 = map(int, puntos.split(','))
                figura = Linea((x1, y1), (x2, y2))
                figuras.append(figura)
                print("Figura agregada exitosamente.")

            elif tipo == "Circle":
                centro = input("Ingrese las coordenadas del centro del círculo (x,y): ")
                x, y = map(int, centro.split(','))
                radio = int(input("Ingrese el radio del círculo: "))
                figura = Circulo((x, y), radio)
                figuras.append(figura)
                print("Figura agregada exitosamente.")

            else:
                print("Tipo de figura no válido")


        elif operacion == "Delete":
            print("Figuras existentes:")
            for i, figura in enumerate(figuras, start=1):
                print("Nro de figura:", i)
                print("Tipo de figura:", type(figura).__name__)
                if isinstance(figura, Rectangulo):
                    print("Datos: Pmin =", figura.pmin, "Pmax =", figura.pmax)
                elif isinstance(figura, Linea):
                    print("Datos: Punto1 =", figura.pmin, "Punto2 =", figura.pmax)
                elif isinstance(figura, Triangulo):
                    print("Datos: P1 =", figura.p1, "P2 =", figura.p2, "P3 =", figura.p3)
                elif isinstance(figura, Circulo):
                    print("Datos: Centro =", figura.centro, "Radio =", figura.radio)
                print()
            
            if figuras:
                indice = int(input("Ingrese el número de la figura que desea eliminar: "))
                if indice >= 1 and indice <= len(figuras):
                    figuras.pop(indice - 1)
                    print("Figura eliminada exitosamente.")
                else:
                    print("Número de figura no válido.")
            else:
                print("No hay figuras para eliminar.")

        # elif operacion == "Delete":
        #     indice = int(input("Ingrese el número de figura que desea eliminar: "))
        #     if indice >= 1 and indice <= len(figuras):
        #         figuras.pop(indice - 1)
        #     else:
        #         print("Número de figura inválido")

        elif operacion == "Show":
            print("Estado de las figuras:")
            for i, figura in enumerate(figuras, start=1):
                print("Nro de figura:", i)
                print("Tipo de figura:", type(figura).__name__)
                if isinstance(figura, Rectangulo):
                    print("Datos: Pmin =", figura.pmin, "Pmax =", figura.pmax)
                elif isinstance(figura, Linea):
                    print("Datos: Punto1 =", figura.pmin, "Punto2 =", figura.pmax)
                elif isinstance(figura, Triangulo):
                    print("Datos: P1 =", figura.p1, "P2 =", figura.p2, "P3 =", figura.p3)
                elif isinstance(figura, Circulo):
                    print("Datos: Centro =", figura.centro, "Radio =", figura.radio)
                print()
            
            canvas.clear()
            for figura in figuras:
                canvas.draw_figure(figura)
            canvas.show()
        else:
            print("Operación no válida")


if __name__ == '__main__':
    main()
