import glfw
from OpenGL.GL import *

from Camera import Camera
from Renderer.RendererMaster import RendererMaster

from InputHandlers.PacmanInputHandler import PacmanInputHandler

from Actors.ActorsController import ActorsController
from Actors.Ghost import Ghost
from Actors.Direction import Direction

import Config

from Util.NetworkController import NetworkController


class Application:


    def __init__(self):
        self.__initializeWindow()
        self.__initializeOpenGL()

        self.renderer = RendererMaster()

        self.actorsController = ActorsController()
        self.networkController = NetworkController(self.actorsController)


    def runLoop(self):

        self.renderer.setFruits(self.actorsController.fruits)

        self.actorsController.addGhost([4, 7], Direction.DOWN, 3.0, "1", Ghost.GhostColor.RED)
        self.actorsController.addGhost([4, 23], Direction.RIGHT, 3.0, "2", Ghost.GhostColor.ORANGE)
        self.actorsController.addGhost([23, 7], Direction.LEFT, 3.0, "3", Ghost.GhostColor.PURPLE)
        self.actorsController.addGhost([23, 23], Direction.UP, 3.0, "4", Ghost.GhostColor.GREEN)

        self.renderer.addPresentComponents(self.actorsController)

        while(   
            (not self.networkController.processInitializationData() or
            not self.networkController.checkConnectionToServer()) and
            not glfw.window_should_close(self.window)
        ):

            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            camera.process_keyboard(self.window, 0.1)

            self.renderer.render(self.window, camera)

            glfw.swap_buffers(self.window)


        self.renderer.addPresentComponents(self.actorsController)
        pacmanInputHandler = PacmanInputHandler(self.actorsController.player_1_pacman)

        while not glfw.window_should_close(self.window):

            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            camera.process_keyboard(self.window, 0.1)
            
            self.networkController.processGameStateData()
            pacmanInputHandler.handleInput(self.window)

            self.actorsController.update()
            
            self.renderer.render(self.window, camera)

            glfw.swap_buffers(self.window)

        glfw.terminate()

     
    def __initializeWindow(self):
        if not glfw.init():
            return
        
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)

        monitor = glfw.get_primary_monitor()
        mode = glfw.get_video_mode(monitor)

        self.window = glfw.create_window(Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT, "My OpenGL window", None, None)

        if not self.window:
            glfw.terminate()
            return

        glfw.set_cursor_pos_callback(self.window, mouse_look_clb)
        glfw.set_key_callback(self.window, key_input_clb)
        #glfw.set_framebuffer_size_callback(self.window, framebuffer_size_callback)

        glfw.make_context_current(self.window)
        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)
        

    def __initializeOpenGL(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_DEPTH_TEST)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)




# Callbacks
lastX, lastY = Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 2
first_mouse = True
camera = Camera()

def mouse_look_clb(window, xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos

    lastX = xpos
    lastY = ypos

    camera.process_mouse_movement(xoffset, yoffset)



def key_input_clb(window, key, scancode, action, mode):

    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)


def framebuffer_size_callback(window, width, height):
    glViewport(0, 0, Config.VIEWPORT_WIDTH, Config.VIEWPORT_HEIGHT)