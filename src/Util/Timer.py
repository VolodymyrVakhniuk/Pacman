import glfw

class Timer:

    def restart(self):
        self.previousTime = glfw.get_time()

    # in milliseconds
    def getElapsedTime(self):
        return 1000 * ((glfw.get_time() - self.previousTime))