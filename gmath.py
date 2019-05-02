import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    color = [0, 0, 0]
    for j in range(3):
        I = 0
        I += ambient[j] * areflect[j]
        I += light[1][j] * dreflect[j] * (dot_product(normalize(normal), normalize(light[0])))
        stuff = (dot_product( subtract( scale( (scale( normalize(normal), 2)) , (dot_product(normalize(normal), normalize(light[0])))) , normalize(light[0])) , normalize(view)))
        if stuff < 0 and SPECULAR_EXP % 2 is 0:
            stuff = -1 * math.pow( stuff, SPECULAR_EXP)
        else:
            stuff = math.pow(stuff, SPECULAR_EXP)
        I += light[1][j] * sreflect[j] * stuff
        color[j] = I
    return limit_color(color)

def limit_color(color):
    for i in range(3):
        if color[i] < 0:
            color[i] = 0
        if color[i] > 255:
            color[i] = 255
        color[i] = int(color[i])
    return color

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude
    return vector
    
def scale(vector, const):
    return [vector[0] * const, vector[1] * const, vector[2] * const]

def subtract(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
