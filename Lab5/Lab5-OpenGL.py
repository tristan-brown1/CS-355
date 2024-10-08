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
CAMERA_Z = 0 
CAMERA_ROTATE = 0
CAMERA_VIEW = "perspective"


def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

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

def start ():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 

    
    #Your Code Here
    
    drawHouse()
    
    
    glFlush()
    

def keyboard(key, x, y):
    global CAMERA_X
    global CAMERA_Y
    global CAMERA_Z
    global CAMERA_ROTATE
    
    if key == chr(27):
        import sys
        sys.exit(0)
  
    if key == b'w':
        print("W is pressed")
        glLoadIdentity()
        CAMERA_Z += 1
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b's':
        print("S is pressed")
        glLoadIdentity()
        CAMERA_Z -= 1
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'a':
        print("A is pressed")
        glLoadIdentity()
        CAMERA_X += 1
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'd':
        print("D is pressed")    
        glLoadIdentity()
        CAMERA_X -= 1
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'q':
        print("Q is pressed")
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)
        glLoadIdentity()
        CAMERA_ROTATE -= 1
        glRotated(0,0,1,0)
        glRotated(0,1,0,0)
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'e':
        print("E is pressed")
        glLoadIdentity()
        CAMERA_ROTATE += 1
        glRotated(0,0,1,0)
        glRotated(0,1,0,0)
        glRotated(CAMERA_ROTATE,0,1,0)
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'r':
        print("R is pressed")
        glLoadIdentity()
        CAMERA_Y -= 1
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'f':
        print("F is pressed")
        glLoadIdentity()
        CAMERA_Y += 1
        glTranslated(CAMERA_X,CAMERA_Y,CAMERA_Z)

    if key == b'h':
        print("H is pressed")
        glLoadIdentity()
        glTranslated(0,0,-6)
    
    if key == b'o':
        print("O is pressed")
        CAMERA_VIEW = "orthographic"
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10, 10, -10, 10, 1, -100)
        glMatrixMode(GL_MODELVIEW)

    if key == b'p':
        print("P is pressed")
        CAMERA_VIEW = "perspective"
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(170, 1, 1, 100)
        glMatrixMode(GL_MODELVIEW)
  
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
glutMainLoop()
