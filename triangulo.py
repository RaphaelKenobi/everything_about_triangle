import math

while True:
    try:
        x = float(input("Digite o comprimento do lado X: "))
        y = float(input("Digite o comprimento do lado Y: "))
        z = float(input("Digite o comprimento do lado Z: "))
        aux = input("Oq você deseja calcular? (perimetro, area, angulo, tipo, tipo_triangulo): ")

        def perimetro(x, y, z):
            perimetro = x + y + z
            print(perimetro)

        def area(x, y, z):
            s = (x + y + z) / 2
            area = (s * (s - x) * (s - y) * (s - z)) ** 0.5
            print(area)

        def angulo(x, y, z):

                cos_angulo_x = (y ** 2 + z ** 2 - x ** 2) / (2 * y * z)
                cos_angulo_y = (x ** 2 + z ** 2 - y ** 2) / (2 * x * z)
                cos_angulo_z = (x ** 2 + y ** 2 - z ** 2) / (2 * x * y)


                angulo_x = math.degrees(math.acos(cos_angulo_x))
                angulo_y = math.degrees(math.acos(cos_angulo_y))
                angulo_z = math.degrees(math.acos(cos_angulo_z))


                print("Ângulo X:", angulo_x)
                print("Ângulo Y:", angulo_y)
                print("Ângulo Z:", angulo_z)

        def tipo(lado1, lado2, lado3):
            if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
                print("Pode formar um triângulo")
                if lado1 == lado2 and lado2 == lado3:
                    print("Triângulo equilátero")
                elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
                    print("Triângulo isósceles")
                else:
                    print("Triângulo escaleno")
            else:
                print("Não pode formar um triângulo")

        def tipo_triangulo(ang1, ang2, ang3):
            if ang1 == 90 or ang2 == 90 or ang3 == 90:
                print("Triângulo retângulo")
            elif ang1 > 90 or ang2 > 90 or ang3 > 90:
                print("Triângulo obtusângulo")
            else:
                print("Triângulo acutângulo")

        tipo(x, y, z)

        if aux == "perimetro":
            perimetro(x, y, z)
        elif aux == "area":
            area(x, y, z)
        elif aux == "angulo":
            angulo(x, y, z)
        elif aux == "tipo_triangulo":
            tipo_triangulo(x, y, z)

    except EOFError:
        break
