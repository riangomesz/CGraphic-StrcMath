import glfw
from OpenGL.GL import *
import ctypes

if not glfw.init():
    raise Exception("GLFW Não pôde ser executado")

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

window_width = 1200
window_height = 800
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)

window = glfw.create_window(window_width, window_height, "Uma janela para o seu bruxo,", None, None)

if not window:
    glfw.terminate()
    raise Exception ("Uma janela para o seu bruxo não pôde ser aberta")

glfw.set_window_pos(window, window_x, window_y)
glfw.make_context_current(window)
glClearColor(0.1, 0.2, 0.1, 0.7)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.poll_events()
    glfw.swap_buffers(window)

glfw.terminate()