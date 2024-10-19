import sys
import math

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
CAMERA_X = 0
CAMERA_Y = 0
CAMERA_Z = -10
CAMERA_ROTATE = 0
CAMERA_VIEW = "perspective"

CAR_MOVE = -40
TIRE_ROTATION = 0

def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

 
def drawCar():
	glLineWidth(2.5)
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-3, 2, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 2, 2)
	#Back Side
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 2, -2)
	#Connectors
	glVertex3f(-3, 2, 2)
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, -2)
	glEnd()
	
def drawTire():
	glLineWidth(2.5)
	glColor3f(0.0, 0.0, 1.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-1, .5, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, .5, .5)
	#Back Side
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, .5, -.5)
	#Connectors
	glVertex3f(-1, .5, .5)
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, -.5)
	glEnd()
		



def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()



def start ():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)


def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 

    
    #Your Code Here
    if CAMERA_VIEW == "perspective":
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, 1, 0, 1000000000000)
        glMatrixMode(GL_MODELVIEW)

    else:
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-20, 20, -20, 20, 1, 100)
        glMatrixMode(GL_MODELVIEW)

    glPushMatrix()
    drawHouse()
    glPopMatrix()
    
    glPushMatrix()
    glTranslated(-20, 0, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(-40, 0, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(20, 0, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(40, 0, 0)
    drawHouse()
    glPopMatrix()



    glPushMatrix()
    glRotated(180,0,1,0)
    glTranslated(0, 0, -40)
    drawHouse()
    glPopMatrix()
    
    glPushMatrix()
    glRotated(180,0,1,0)
    glTranslated(-20, 0, -40)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glRotated(180,0,1,0)
    glTranslated(-40, 0, -40)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glRotated(180,0,1,0)
    glTranslated(20, 0, -40)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glRotated(180,0,1,0)
    glTranslated(40, 0, -40)
    drawHouse()
    glPopMatrix()


    #car model is updated here 
    glPushMatrix()
    glTranslated(CAR_MOVE,0,25)
    drawCar()

    glTranslated(2,0,2.5)
    glRotated(TIRE_ROTATION,0,0,1)
    drawTire()

    glPushMatrix()
    glTranslated(0,0,-5)
    drawTire()
    glPopMatrix()

    glPopMatrix()


    glPushMatrix()
    glTranslated(CAR_MOVE,0,25)    
    glTranslated(-2,0,2.5)
    glRotated(TIRE_ROTATION,0,0,1)
    drawTire()
    
    glPushMatrix()
    glTranslated(0,0,-5)
    drawTire()
    glPopMatrix()
    glPopMatrix()
    

    
    



    glFlush()
    
def update(value):
    global CAR_MOVE
    global TIRE_ROTATION

    CAR_MOVE += 0.005
    TIRE_ROTATION -= 0.1

    glutPostRedisplay()
    glutTimerFunc(1, update, 0)

def keyboard(key, x, y):
    global CAMERA_X
    global CAMERA_Y
    global CAMERA_Z
    global CAMERA_ROTATE
    global CAMERA_VIEW
    global TIRE_ROTATION
    global CAR_MOVE
    
    if key == chr(27):
        import sys
        sys.exit(0)
  
    if key == b'w':
        print("W is pressed")
        glLoadIdentity()
        CAMERA_X -= math.sin(math.radians(CAMERA_ROTATE))
        CAMERA_Z += math.cos(math.radians(CAMERA_ROTATE))
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b's':
        print("S is pressed")
        glLoadIdentity()
        CAMERA_X += math.sin(math.radians(CAMERA_ROTATE))
        CAMERA_Z -= math.cos(math.radians(CAMERA_ROTATE))
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'a':
        print("A is pressed")
        glLoadIdentity()
        CAMERA_X -= math.sin(math.radians(CAMERA_ROTATE - 90))
        CAMERA_Z += math.cos(math.radians(CAMERA_ROTATE - 90))
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'd':
        print("D is pressed")    
        glLoadIdentity()
        CAMERA_X -= math.sin(math.radians(CAMERA_ROTATE + 90))
        CAMERA_Z += math.cos(math.radians(CAMERA_ROTATE + 90))
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'q':
        print("Q is pressed")
        glLoadIdentity()
        CAMERA_ROTATE -= 1
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)
        

    if key == b'e':
        print("E is pressed")
        glLoadIdentity()
        CAMERA_ROTATE += 1
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)
        

    if key == b'r':
        print("R is pressed")
        glLoadIdentity()
        CAMERA_Y -= 1
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'f':
        print("F is pressed")
        glLoadIdentity()
        CAMERA_Y += 1
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'h':
        print("H is pressed")
        glLoadIdentity()
        CAMERA_X = 0
        CAMERA_Y = 0
        CAMERA_Z = -30
        CAMERA_ROTATE = 0
        CAR_MOVE = -40
        TIRE_ROTATION = 0
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)
    
    if key == b'o':
        print("O is pressed")
        CAMERA_VIEW = "orthographic"
        

    if key == b'p':
        print("P is pressed")
        CAMERA_VIEW = "perspective"
        
  
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
start()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(1, update, 0)
glutMainLoop()
