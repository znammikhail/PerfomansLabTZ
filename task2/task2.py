import math
import sys

if sys.argv and len(sys.argv) > 2:  # если из командной строки
    data_circle = sys.argv[1]
    data_points = sys.argv[2]
else:                               # если из консоли
    data_circle = input()
    data_points = input()

# данные окружности
file_circle = open(data_circle, 'r')
line = file_circle.readline()
coord = line.strip().split()
x_0 = float(coord[0])
y_0 = float(coord[1])
line = file_circle.readline()
r_circle = float(line)
file_circle.close()

file_points = open(data_points, 'r')

while True:
    line = file_points.readline()
    if not line:
        break
    coord = line.strip().split()
    x_point = float(coord[0])
    y_point = float(coord[1])
    hypotenuse = math.sqrt((x_point - x_0) ** 2 + (y_point - y_0) ** 2)

    if hypotenuse == r_circle:
        print("0")  # точка на окр
    elif hypotenuse < r_circle:
        print("1")  # точка внутри
    else:
        print("2")  # точка снаружи

file_points.close()