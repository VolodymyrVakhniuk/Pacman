from pyrr import Vector3, vector, vector3, matrix44
from math import sin, cos, radians
import glfw
import Config

class Camera:
    def __init__(self):
        self.camera_pos = Vector3([0.0, 4.0, 3.0])
        self.camera_front = Vector3([0.0, 0.0, -1.0])
        self.camera_up = Vector3([0.0, 1.0, 0.0])
        self.camera_right = Vector3([1.0, 0.0, 0.0])

        self.mouse_sensitivity = 0.25
        self.jaw = -90
        self.pitch = 0

        self.projectionMatrix = matrix44.create_perspective_projection_matrix(65, Config.WINDOW_WIDTH / Config.WINDOW_HEIGHT, 0.1, 100.0)

    def get_view_matrix(self):
        return matrix44.create_look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)

    def get_projection_matrix(self):
        return self.projectionMatrix


    def process_mouse_movement(self, xoffset, yoffset, constrain_pitch=True):
        xoffset *= self.mouse_sensitivity
        yoffset *= self.mouse_sensitivity

        self.jaw += xoffset
        self.pitch += yoffset

        if constrain_pitch:
            if self.pitch > 90:
                self.pitch = 90
            if self.pitch < -90:
                self.pitch = -90

        self.update_camera_vectors()

    def update_camera_vectors(self):
        front = Vector3([0.0, 0.0, 0.0])
        front.x = cos(radians(self.jaw)) * cos(radians(self.pitch))
        front.y = sin(radians(self.pitch))
        front.z = sin(radians(self.jaw)) * cos(radians(self.pitch))

        self.camera_front = vector.normalise(front)
        self.camera_right = vector.normalise(vector3.cross(self.camera_front, Vector3([0.0, 1.0, 0.0])))
        self.camera_up = vector.normalise(vector3.cross(self.camera_right, self.camera_front))

    # Camera method for the WASD movement
    def process_keyboard(self, window, velocity):
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            self.camera_pos += self.camera_front * velocity

        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            self.camera_pos -= self.camera_front * velocity

        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
            self.camera_pos -= self.camera_right * velocity

        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
            self.camera_pos += self.camera_right * velocity

        if glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            self.camera_pos -= self.camera_up * velocity

        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            self.camera_pos += self.camera_up * velocity


