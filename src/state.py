import renderer
import player
import input_handler


class State:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.input_handler = input_handler.InputHandler()
        self.renderer = renderer.Renderer(self.width, self.height)

        self.player = player.Player(width/2, height/2)

    #TODO: implement updating
    def update(self):
        current_input_state = self.input_handler.get_current_input_state()

        self.player.update()
