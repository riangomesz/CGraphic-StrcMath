import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

origem = GLint()
ang = trans = 0
scl = 1

def draw_f():
   # desenha a letra F por primitivas
   glColor3f(1.0, 1.0, 1.0)
   glBegin(GL_LINES)
   glVertex3f(0.0, 0.0, 0.0)
   glVertex3f(0.0, 2.0, 0.0)

   glVertex3f(0.0, 2.0, 0.0)
   glVertex3f(1.0, 2.0, 0.0)

   glVertex3f(1.0, 2.0, 0.0)
   glVertex3f(1.0, 1.7, 0.0)

   glVertex3f(1.0, 1.7, 0.0)
   glVertex3f(0.4, 1.7, 0.0)

   glVertex3f(0.4, 1.7, 0.0)
   glVertex3f(0.4, 1.4, 0.0)

   glVertex3f(0.4, 1.4, 0.0)
   glVertex3f(1.0, 1.4, 0.0)

   glVertex3f(1.0, 1.4, 0.0)
   glVertex3f(1.0, 1.1, 0.0)

   glVertex3f(1.0, 1.1, 0.0)
   glVertex3f(0.4, 1.1, 0.0)

   glVertex3f(0.4, 1.1, 0.0)
   glVertex3f(0.4, 0.0, 0.0)

   glVertex3f(0.4, 0.0, 0.0)
   glVertex3f(0.0, 0.0, 0.0)
   glEnd()

def draw_origin():
   global origem
   
   origem = glGenLists(1)
   glNewList(origem, GL_COMPILE)
   glColor3f(1.0, 0.0, 0.0)
   glBegin(GL_LINES)
   glColor3f(1,0,0) # x
   glVertex3i(0,0,0)
   glVertex3i(1,0,0)

   glColor3f(0.0, 1.0, 0.0)
   glColor3f(0,1,0) # y
   glVertex3i(0,0,0)
   glVertex3i(0,1,0)

   glColor3f(0.0, 0.0, 1.0)
   glColor3f(0,0,1) # z
   glVertex3i(0,0,0)
   glVertex3i(0,0,1)
   glEnd()
   glEndList()

def main():
   global ang, trans, scl

   pygame.init()
   display = (640, 480)
   pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

   gluPerspective(60, (display[0]/display[1]), 0.1, 50.0)

   glTranslatef(0.0, 0.0, -5.0)

   draw_origin()

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            quit()
         if pygame.key.get_focused():
            key = pygame.key.get_pressed()
            if(key[pygame.K_r]):
               ang = (ang - 30) % 360
            if(key[pygame.K_RIGHT]):
               trans += 0.2 
            if(key[pygame.K_LEFT]):
               trans -= 0.2
            if(key[pygame.K_UP]):
               scl += 0.2
            if(key[pygame.K_DOWN]):
               scl -= 0.2 

      # Clears the screen for the next frame to be drawn over
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

      # desenho da origem
      glCallList(origem)

      # desenho letra f
      glPushMatrix()
      glTranslatef(trans, 0, 0)
      glScale(1, scl, 1)
      glRotatef(ang, 0, 1, 0)
      draw_f()
      glPopMatrix()

      
      # Function used to advance to the next frame essentially
      pygame.display.flip()
      pygame.time.wait(10)

main()