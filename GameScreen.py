import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = (244, 255, 129)

class OXGameWindow(arcade.Window) :
    def __init__(self, width, height) :
        super().__init__(width, height)

        arcade.set_background_color(BG_COLOR)

    def on_draw(self) :
        arcade.start_render()

if __name__ == '__main__' :
    window = OXGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
