import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class OXGameWindow(arcade.Window) :
    def __init__(self, width, height) :
        super().__init__(width, height)

        self.image = arcade.load_texture('BG.jpg')

        self.playerO = arcade.Sprite('O.png')
        self.playerX = arcade.Sprite('X.png')

        self.playerO.set_position(100, 100)
        self.playerX.set_position(200, 200)

    def on_draw(self) :
        arcade.start_render()
        arcade.draw_texture_rectangle(300, 300, SCREEN_WIDTH, SCREEN_HEIGHT,self.image)
        self.playerO.draw()
        self.playerX.draw()

if __name__ == '__main__' :
    window = OXGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
