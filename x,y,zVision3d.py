import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

def cross_product(v1, v2):
    return np.cross(v1, v2)

def draw_vector(vector, color):
    glBegin(GL_LINES)
    glColor3fv(color)
    glVertex3f(0, 0, 0)  # Origin
    glVertex3fv(vector)  # Destination
    glEnd()

def setup_scene():
    glClearColor(0.1, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)

def setup_projection(window):
    width, height = glfw.get_framebuffer_size(window)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / float(height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def rotate_vector(vector, angle, axis):
    c, s = np.cos(angle), np.sin(angle)
    if axis == 'z':
        R = np.array([[c, -s, 0],
                      [s, c, 0],
                      [0, 0, 1]], dtype=np.float32)
    elif axis == 'y':
        R = np.array([[c, 0, s],
                      [0, 1, 0],
                      [-s, 0, c]], dtype=np.float32)
    elif axis == 'x':
        R = np.array([[1, 0, 0],
                      [0, c, -s],
                      [0, s, c]], dtype=np.float32)
    else:
        return vector  # No rotation if axis is not recognized
    return np.dot(R, vector)

def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "3D Cross Product Visualization", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    setup_scene()

    vec1 = np.array([1, 0, 0], dtype=np.float32)
    vec2 = np.array([0, 1, 0], dtype=np.float32)
    
    angle = 0  # Initial angle for rotation

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        setup_projection(window)
        glLoadIdentity()
        gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

        # Rotate vec1 around the Z-axis
        angle += 0.01  # Increment the angle
        rotated_vec1 = rotate_vector(vec1, angle, 'z')
        cross_vec = cross_product(rotated_vec1, vec2)

        draw_vector(rotated_vec1, (1, 0, 0))  # Red
        draw_vector(vec2, (0, 1, 0))  # Green
        draw_vector(cross_vec, (0, 0, 1))  # Blue

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()