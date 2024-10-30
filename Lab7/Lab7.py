# Import a library of functions called 'pygame'
import math
import pygame
from math import pi
import numpy as np


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Line3D():

    def __init__(self, start, end):
        self.start = start
        self.end = end

def loadOBJ(filename):

    vertices = []
    indices = []
    lines = []

    f = open(filename, "r")
    for line in f:
        t = str.split(line)
        if not t:
            continue
        if t[0] == "v":
            vertices.append(Point3D(float(t[1]),float(t[2]),float(t[3])))

        if t[0] == "f":
            for i in range(1,len(t) - 1):
                index1 = int(str.split(t[i],"/")[0])
                index2 = int(str.split(t[i+1],"/")[0])
                indices.append((index1,index2))

    f.close()

    #Add faces as lines
    for index_pair in indices:
        index1 = index_pair[0]
        index2 = index_pair[1]
        lines.append(Line3D(vertices[index1 - 1],vertices[index2 - 1]))

    #Find duplicates
    duplicates = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]

            # Case 1 -> Starts match
            if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
                if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
                    duplicates.append(j)
            # Case 2 -> Start matches end
            if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
                if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
                    duplicates.append(j)

    duplicates = list(set(duplicates))
    duplicates.sort()
    duplicates = duplicates[::-1]

    #Remove duplicates
    for j in range(len(duplicates)):
        del lines[duplicates[j]]

    return lines

def loadHouse():
    house = []
    #Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    #Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    #Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    #Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    #Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))

    return house

def loadCar():
    car = []
    #Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    #Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))
    
    #Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car

def loadTire():
    tire = []
    #Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    #Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    #Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))
    
    return tire




# create quite a bit here i think


def convert_to_homogenous(regular_points):
    homogenous_coordinates = []

    # for all points passed in, homogenize them and return the new list of lines with homogenized points
    for point in regular_points:
        homogenous_coordinates.append(Line3D([point.start.x, point.start.y, point.start.z, 1],
                                             [point.end.x, point.end.y, point.end.z, 1]))
    return homogenous_coordinates

def object_to_world(homogenous_list, matrix_type):
    obj_to_world_coordinates = []
    for matrix in matrix_type:
        for point in homogenous_list:
            obj_to_world_coordinates.append(Line3D(matrix.dot(point.start),matrix.dot(point.end)))

    return obj_to_world_coordinates

def world_to_camera(object_to_world_list, cam_x,cam_y,cam_z,camera_rotation):
    camera_matrix = np.array([[math.cos(math.radians(camera_rotation)), 0, -math.sin(math.radians(camera_rotation)), -cam_x * math.cos(math.radians(camera_rotation)) - cam_z * math.sin(math.radians(camera_rotation))],
                              [0, 1, 0, cam_y],
                              [math.sin(math.radians(camera_rotation)), 0, math.cos(math.radians(camera_rotation)), -cam_x * math.sin(math.radians(camera_rotation)) + cam_z * math.cos(math.radians(camera_rotation))],
                              [0, 0, 0, 1]])

    world_to_camera_list = []
    for j in object_to_world_list:
        world_to_camera_list.append(Line3D(camera_matrix.dot(j.start),camera_matrix.dot(j.end)))


def clipping_tests():
    pass

def clipping():
    pass

def viewport_transformation():
    pass

def pipeline():
    pass

def draw_house(house_list, cam_x, cam_y, cam_z, camera_rotation):
    homogenous_list = convert_to_homogenous(house_list)
    world_to_camera_list = world_to_camera(object_to_world(homogenous_list, house_matrices),cam_x,cam_y,cam_z,camera_rotation)
    clipping(world_to_camera_list)
    for i in world_to_camera_list:
        pygame.draw.line(screen, RED, (i.start[0], i.start[1]), (i.end[0], i.end[1]))


def draw_car(car_list, x, y, z, camera_rotation):
    pass
def draw_tires():
    pass

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [512, 512]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")
 
#Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0,0.0)
end = Point(0.0,0.0)
house_line_list = loadHouse()
car_line_list = loadCar()
CAMERA_X = 0
CAMERA_Y = 0
CAMERA_Z = -30
CAMERA_ROTATE = 0
CAMERA_VIEW = "perspective"
CAR_MOVE = -40
TIRE_ROTATION = 0
clipping_matrix = np.array([])
screen_display_matrix = np.array([])
house_matrices = np.array([])
car_matrices = np.array([])
tire_matrices = np.array([])

#Loop until the user clicks the close button.
while not done:

    # This limits the while loop to a max of 100 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(100)

    # Clear the screen and set the screen background
    screen.fill(BLACK)

    #Controller Code#
    #####################################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            done=True
            
    
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_w]:
        print("w is pressed")
        CAMERA_X -= math.sin(math.radians(CAMERA_ROTATE))
        CAMERA_Z += math.cos(math.radians(CAMERA_ROTATE))


    if pressed[pygame.K_a]:
        print("a is pressed")
        CAMERA_X -= math.sin(math.radians(CAMERA_ROTATE - 90))
        CAMERA_Z += math.cos(math.radians(CAMERA_ROTATE - 90))


    if pressed[pygame.K_s]:
        print("s is pressed")
        CAMERA_X += math.sin(math.radians(CAMERA_ROTATE))
        CAMERA_Z -= math.cos(math.radians(CAMERA_ROTATE))

    if pressed[pygame.K_d]:
        print("d is pressed")
        CAMERA_X -= math.sin(math.radians(CAMERA_ROTATE + 90))
        CAMERA_Z += math.cos(math.radians(CAMERA_ROTATE + 90))

    if pressed[pygame.K_e]:
        print("e is pressed")
        CAMERA_ROTATE += 1

    if pressed[pygame.K_q]:
        print("q is pressed")
        CAMERA_ROTATE -= 1


    if pressed[pygame.K_r]:
        print("r is pressed")
        CAMERA_Y -= 1

    if pressed[pygame.K_f]:
        print("f is pressed")
        CAMERA_Y += 1

    if pressed[pygame.K_h]:
        print("h is pressed")
        CAMERA_X = 0
        CAMERA_Y = 0
        CAMERA_Z = -30
        CAMERA_ROTATE = 0
        CAR_MOVE = -40
        TIRE_ROTATION = 0

    #Viewer Code#
    #####################################################################
    draw_house(house_line_list, CAMERA_X, CAMERA_Y, CAMERA_Z, CAMERA_ROTATE)
    draw_car(car_line_list, CAMERA_X,CAMERA_Y, CAMERA_Z, CAMERA_ROTATE)


    for s in house_line_list:
        #BOGUS DRAWING PARAMETERS SO YOU CAN SEE THE HOUSE WHEN YOU START UP
        pygame.draw.line(screen, BLUE, (20*s.start.x+200, -20*s.start.y+200), (20*s.end.x+200, -20*s.end.y+200))

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
