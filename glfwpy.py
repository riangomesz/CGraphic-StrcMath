import glfw 
from OpenGL.GL import *

if not glfw.init():
        raise Exception("GLFW Não pôde ser executado")
window = glfw.create_window(1200, 800, "Uma janela para o seu bruxo,", None, None )

if not window:
    glfw.terminate()
    raise Exception ("Uma janela para o seu bruxo não pôde ser aberta")
glfw.set_window_pos(window, 400, 100)
glfw.make_context_current(window)
glClearColor(0.1, 0.2, 0.1, 0.7)
while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.poll_events()
    glfw.swap_buffers(window)
glfw.terminate()