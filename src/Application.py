import glfw
from OpenGL.GL import *

from Camera import Camera
from Renderer.RendererMaster import RendererMaster

from InputHandlers.PacmanInputHandler import PacmanInputHandler

from GameActors import GameActors
#from GameController import GameController

import Config

from NetworkController1 import NetworkController1



class Application:


    def __init__(self):
        self.__initializeWindow()
        self.__initializeOpenGL()

        self.renderer = RendererMaster()

        self.actors = GameActors()
        self.networkController = NetworkController1(self.actors)


    def runLoop(self):

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


        self.renderer.addPacmans(self.actors.player_1_pacman)
        pacmanInputHandler = PacmanInputHandler(self.actors.player_1_pacman)

        while not glfw.window_should_close(self.window):

            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            camera.process_keyboard(self.window, 0.1)
            
            self.networkController.processGameStateDataData()
            pacmanInputHandler.handleInput(self.window)

            self.actors.player_1_pacman.update()
            #self.actors.player_2_pacman.update()
            
            self.renderer.render(self.window, camera)

            glfw.swap_buffers(self.window)

        glfw.terminate()




    # def runLoop(self):

    #     renderer = RendererMaster()

    #     while not glfw.window_should_close(self.window):

    #         glfw.poll_events()
    #         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #         camera.process_keyboard(self.window, 0.1)

    #         renderer.render(self.window, camera)

    #         glfw.swap_buffers(self.window)

    #     glfw.terminate()


    # def runLoop(self):

    #     renderer = RendererMaster()
    #     #renderer.addPacmans(self.gameController.player_1_pacman)#self.pacman)#)

    #     pacmanInputHandler = None

    #     while not glfw.window_should_close(self.window):

    #         glfw.poll_events()
    #         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #         if self.networkController.initializationDone == True:

    #             renderer.addPacmans(self.gameController.player_1_pacman, self.gameController.player_2_pacman)
    #             pacmanInputHandler = PacmanInputHandler(self.gameController.player_1_pacman)


    #         camera.process_keyboard(self.window, 0.1)
            
    #         if self.networkController.initializationDone == True:

    #             pacmanInputHandler.handleInput(self.window)
    #             self.gameController.player_1_pacman.update()
    #             self.gameController.player_2_pacman.update()
            

    #         renderer.render(self.window, camera)

    #         glfw.swap_buffers(self.window)

    #     glfw.terminate()


    # def __initializeActors(self):
            
    #     # Connect to server

    #     self.gameController = GameController()
    #     self.networkController = NetworkController(self.gameController)

    #     if self.networkController.connectedToServer == True:
    #         self.networkController.initializeComponents()
        #Network().setRecievedDataParser(self.networkDataParser)
        


        # while not self.networkDataParser.IsInitializationDone():
        #     pass




        # self.gameController.addPacman([0, 0], Pacman.Direction.NONE, '0', True)

        # self.pacman = Pacman([0, 0], Pacman.Direction.NONE, 0)
        # self.pacman1 = Pacman([0, 1], Pacman.Direction.NONE, 0)
        # self.pacman2 = Pacman([1, 1], Pacman.Direction.NONE, 0)
        # self.pacman3 = Pacman([2, 1], Pacman.Direction.NONE, 0)
        # self.pacman4 = Pacman([3, 1], Pacman.Direction.NONE, 0)


        
    def __initializeWindow(self):
        if not glfw.init():
            return
        
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, glfw.TRUE)

        self.window = glfw.create_window(1100, 900, "My OpenGL window", None, None)

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