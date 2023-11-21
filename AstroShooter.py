import arcade
import arcade.gui
import random
import os
from os import path

import twoplayer
from twoplayer import *

file_path = os.path.dirname(os.path.abspath(__file__))
DIR = path.dirname(path.abspath(__file__))
os.chdir(file_path)
WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5
SCORE = 0
NITRO = 0
HIGH_SCORE = 0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Asteroid shooter"

MOVEMENT_SPEED = 1.5

SPRITE_SCALING_LASER = 0.8
SHOOT_SPEED = 15
BULLET_SPEED = 5

# Index of textures, first element faces left, second faces right

TEXTURE_LEFT = 0

TEXTURE_RIGHT = 1


class Mode(arcade.View):
    def __init__(self):
        super().__init__()

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        self.background = arcade.load_texture(
            "D:\Python Wesley\Python\pythonProject\\venv\lib\python3.11\site-packages\\arcade\\resources\images\space_shooter\space.png")

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons

        start_button = arcade.gui.UIFlatButton(text="1v1: Battle against each other in an arena", width=300)
        self.v_box.add(start_button.with_space_around(bottom=50))

        two_player = arcade.gui.UIFlatButton(text="""LMS: Last man standing.""", width=300)
        self.v_box.add(two_player.with_space_around(bottom=50))

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start
        two_player.on_click = self.on_click_begin

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        game_view = twoplayer.Game3View()
        self.window.show_view(game_view)

    def on_click_begin(self, event):
        levels = GameOverView2()
        self.window.show_view(levels)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.background.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text("Mode", WIDTH / 2, 500,
                         arcade.color.WHITE, font_size=50, anchor_x="center", font_name="Kenney Future")
        self.manager.draw()


class Explosion(arcade.Sprite):
    """ This class creates an explosion animation """

    def __init__(self, texture_list):

        super().__init__()

        # Start at the first frame

        self.current_texture = 0

        self.textures = texture_list

    def update(self):

        # Update to the next frame of the animation. If we are at the end

        # of our frames, then delete this sprite.

        self.current_texture += 1

        if self.current_texture < len(self.textures):

            self.set_texture(self.current_texture)

        else:

            self.remove_from_sprite_lists()


class FallingCoin(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 2

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class FallingCoin2(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 2.5

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class FallingCoin3(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 3

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class FallingCoin4(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 3.5

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class FallingCoin5(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 4

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class FallingCoin6(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 5

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT


class Special(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 3.54

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.remove_from_sprite_lists()


class Pwrup(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 2.5

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.remove_from_sprite_lists()


class Heart(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 3.5

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.remove_from_sprite_lists()


class Pwrup2(arcade.Sprite):
    """ Simple sprite that falls down """

    def update(self):
        """ Move the coin """

        # Fall down
        self.center_y -= 3.5

        # Did we go off the screen? If so, pop back to the top.
        if self.top < 0:
            self.remove_from_sprite_lists()


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING
        self.respawning = 0
        self.thrust = 0
        self.speed = 0
        self.max_speed = 3
        self.drag = 0
        self.respawning = 0
        self.angle = 180

        # Mark that we are respawning.
        self.respawn()

        self.textures = []
        self.coin_list = None

        texture = arcade.load_texture("D:\Python Wesley\Python\pythonProject\\venv\lib\python3.11\site-packages\\arcade\\resources\images\space_shooter\\spaceShips_005.png")

        self.textures.append(texture)

        texture = arcade.load_texture("D:\Python Wesley\Python\pythonProject\\venv\lib\python3.11\site-packages\\arcade\\resources\images\space_shooter\\spaceShips_005.png",

                                      flipped_horizontally=False)

        self.textures.append(texture)

        # By default, face right.

        self.texture = texture

    def respawn(self):
        self.respawning = 1

        self.center_x = 400
        self.center_y = 50

    def update(self):
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the ship goes off-screen, move it to the other side of the window

        """ Call the parent class. """
        super().update()


class ChangeShip(arcade.View):
    def __init__(self):
        super().__init__()

        self.walls = None
        self.walls = arcade.SpriteList()

        coordinate_list = [[395, 160]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                ":resources:images/space_shooter/playerShip1_blue.png", 0.5
            )
            wall.position = coordinate
            self.walls.append(wall)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()

        self.walls.draw()

        arcade.draw_text("Change your ship: ", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=25, anchor_x="center", font_name="Kenney Future")

        arcade.draw_text("Blue Ranger", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class MyWindow(arcade.View):
    def __init__(self):
        super().__init__()

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        self.background = arcade.load_texture("D:\Python Wesley\Python\pythonProject\\venv\lib\python3.11\site-packages\\arcade\\resources\images\space_shooter\space.png")

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Play", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        two_player = arcade.gui.UIFlatButton(text="2 players", width=200)
        self.v_box.add(two_player.with_space_around(bottom=20))

        levels_button = arcade.gui.UIFlatButton(text="Levels", width=200)
        self.v_box.add(levels_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="How to play", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start
        levels_button.on_click = self.on_click_levels
        two_player.on_click = self.on_click_mode

        # --- Method 3 for handling click events,
        # use a decorator to handle on_click events
        @settings_button.event("on_click")
        def on_click_settings(event):
            instructions = InstructionView()
            self.window.show_view(instructions)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        game_view = GameView()
        self.window.show_view(game_view)

    def on_click_levels(self, event):
        levels = Levels()
        self.window.show_view(levels)

    def on_click_mode(self, event):
        mode = Mode()
        self.window.show_view(mode)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.background.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text("Astro Shooter", WIDTH / 2, 500,
                         arcade.color.WHITE, font_size=50, anchor_x="center", font_name="Kenney Future")
        self.manager.draw()

class InstructionView(arcade.View):
    def on_show_view(self):
        self.background = arcade.load_texture(
            "D:\Python Wesley\Python\pythonProject\\venv\lib\python3.11\site-packages\\arcade\\resources\images\space_shooter\space.png")

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.background.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_text("Mission: Navigate your way through", WIDTH / 2, HEIGHT / 2,
                         arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text(" the dangerous asteroid fields", WIDTH / 2, HEIGHT / 2 - 25,
                         arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("Look out for powerups, as they", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("will help you throughout your journey", WIDTH / 2, HEIGHT / 2 - 100,
                         arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("The arrow keys will help you travel up,", WIDTH / 2, HEIGHT / 2 - 150,
                         arcade.color.WHITE, font_size=15, anchor_x="center", font_name="Kenney Future")
        arcade.draw_text("down, left, and right. Space is to shoot", WIDTH / 2, HEIGHT / 2 - 175,
                         arcade.color.SNOW, font_size=10, anchor_x="center", font_name="Kenney Future")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


class Levels(arcade.View):
    def __init__(self):
        super().__init__()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.background = arcade.load_texture(
            "D:\Python Wesley\Python\pythonProject\\venv\lib\python3.11\site-packages\\arcade\\resources\images\space_shooter\space.png")

        self.v_box = arcade.gui.UIBoxLayout()

        level_1 = arcade.gui.UIFlatButton(text="Level 1", width=200)
        self.v_box.add(level_1.with_space_around(bottom=20))

        level_2 = arcade.gui.UIFlatButton(text="Level 2", width=200)
        self.v_box.add(level_2.with_space_around(bottom=20))

        level_3 = arcade.gui.UIFlatButton(text="Level 3", width=200)
        self.v_box.add(level_3.with_space_around(bottom=20))

        level_4 = arcade.gui.UIFlatButton(text="Level 4", width=200)
        self.v_box.add(level_4.with_space_around(bottom=20))

        level_5 = arcade.gui.UIFlatButton(text="Level 5", width=200)
        self.v_box.add(level_5.with_space_around(bottom=20))

        level_6 = arcade.gui.UIFlatButton(text="Level 6", width=200)
        self.v_box.add(level_6.with_space_around(bottom=20))

        level_1.on_click = self.on_click_level_1
        level_2.on_click = self.on_click_level_2
        level_3.on_click = self.on_click_level_3
        level_4.on_click = self.on_click_level_4
        level_5.on_click = self.on_click_level_5
        level_6.on_click = self.on_click_level_6

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_level_1(self, event):
        level1 = GameView()
        self.window.show_view(level1)

    def on_click_level_2(self, event):
        level2 = GameView()
        level2.level += 2
        self.window.show_view(level2)

    def on_click_level_3(self, event):
        level2 = GameView()
        level2.level += 3
        self.window.show_view(level2)

    def on_click_level_4(self, event):
        level2 = GameView()
        level2.level += 4
        self.window.show_view(level2)

    def on_click_level_5(self, event):
        level2 = GameView()
        level2.level += 5
        self.window.show_view(level2)

    def on_click_level_6(self, event):
        level2 = GameView()
        level2.level += 6
        self.window.show_view(level2)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.background.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.manager.draw()


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.game_over = False
        # Variables that will hold sprite lists
        self.player_sprite_list = None
        self.ship_list = None
        self.coin_list = None
        self.explosions_list = None
        self.power_up_list = None
        self.ships = None
        self.heart_list = None
        self.special_list = None
        self.boundaries = None
        self.background = None
        self.nitro_list = None

        # Set up the player info
        self.player_sprite = None
        self.ship = None
        self.heart = None
        self.power_up = None
        self.nitro = None
        self.coin = None
        self.bullet_list = None
        self.text_score = None
        self.lives_txt = None
        self.score = None
        self.health = None
        self.level = None
        self.lvl_txt = None
        self.anders = None
        self.high_score = None
        self.current = None
        self.scores = None

        self.explosion_texture_list = []
        self.scores = [0]

        columns = 16

        count = 60

        sprite_width = 256

        sprite_height = 256
        self.respawning = 0

        file_name = ":resources:images/spritesheets/explosion.png"
        self.shoot_sound = arcade.load_sound(":resources:sounds/laser3.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit3.wav")
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")

        self.game_over = False
        self.time_taken = 0

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        self.power_up_list = arcade.SpriteList()
        self.heart_list = arcade.SpriteList()
        self.ship_list = arcade.SpriteList()
        self.special_list = arcade.SpriteList()
        self.anders = arcade.SpriteList()
        self.nitro_list = arcade.SpriteList()
        self.boundaries = arcade.SpriteList()

        self.score = 0
        self.level = 1
        self.lives = 3
        self.health = 2
        self.nitro = 0
        self.high_score = 0
        self.current = self.high_score

        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        self.text_score = arcade.Text(
            f"{self.score}",
            start_x=625,
            start_y=475,
            font_size=20,
        )

        self.high_score_text = arcade.Text(
            f"High score: {HIGH_SCORE}",
            start_x=625,
            start_y=525,
            font_size=20,
        )

        self.lvl_txt = arcade.Text(
            f"Score: {self.level}",
            start_x=10,
            start_y=50,
            font_size=13,
        )
        self.lives_txt = arcade.Text(
            f"Lives: {self.lives}",
            start_x=10,
            start_y=30,
            font_size=13,
        )
        self.nitro_txt = arcade.Text(
            f"Nitro: {self.nitro}",
            start_x=625,
            start_y=425,
            font_size=20,
            color=arcade.csscolor.WHITE
        )

        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

        self.level_1()

    def level_1(self):
        for i in range(30):
            # Create the coin instance
            coin = FallingCoin(":resources:images/space_shooter/meteorGrey_big2.png", SPRITE_SCALING / 2)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for y in (-64, SCREEN_HEIGHT - SPRITE_SCALING):
            # Loop for each box going across
            for x in range(0, SCREEN_WIDTH, 64):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                     SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                self.boundaries.append(wall)

        pu = Pwrup(":resources:images/items/gemBlue.png", SPRITE_SCALING / 1)
        pu.center_x = random.randrange(SCREEN_WIDTH)
        pu.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
        self.power_up_list.append(pu)

    def level_2(self):
        for i in range(36):
            # Create the coin instance
            coin = FallingCoin2(":resources:images/space_shooter/meteorGrey_big2.png", SPRITE_SCALING / 2)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def level_3(self):
        for i in range(40):
            # Create the coin instance
            coin = FallingCoin3(":resources:images/space_shooter/meteorGrey_big2.png", SPRITE_SCALING / 0.80)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(3):
            # Create the coin instance
            spcl = Special(":resources:images/space_shooter/meteorGrey_big2.png", SPRITE_SCALING / 0.80)

            # Position the coin
            spcl.center_x = random.randrange(SCREEN_WIDTH)
            spcl.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.special_list.append(spcl)

        pu = Pwrup2(":resources:images/items/gemBlue.png", SPRITE_SCALING / 1)
        pu.center_x = random.randrange(SCREEN_WIDTH)
        pu.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
        self.power_up_list.append(pu)

    def level_4(self):
        for i in range(45):
            # Create the coin instance
            coin = FallingCoin4(":resources:images/space_shooter/meteorGrey_big4.png", SPRITE_SCALING / 0.7)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(1):
            heart = Heart(":resources:images/items/star.png", SPRITE_SCALING / 0.7)

            # Position the coin
            heart.center_x = random.randrange(SCREEN_WIDTH)
            heart.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            self.heart_list.append(heart)

    def level_5(self):
        for i in range(55):
            # Create the coin instance
            coin = FallingCoin5(":resources:images/space_shooter/meteorGrey_big4.png", SPRITE_SCALING / 0.65)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def level_6(self):
        for i in range(55):
            # Create the coin instance
            coin = FallingCoin6(":resources:images/space_shooter/meteorGrey_big4.png", SPRITE_SCALING / 0.65)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.coin_list.append(coin)
        for i in range(1):
            heart = Heart(":resources:images/items/star.png", SPRITE_SCALING / 0.7)

            # Position the coin
            heart.center_x = random.randrange(SCREEN_WIDTH)
            heart.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            self.heart_list.append(heart)
        for i in range(4):
            # Create the coin instance
            spcl = Special(":resources:spaceshooter/PNG/Meteors/meteorGrey_big1.png  ", SPRITE_SCALING / 0.80)

            # Position the coin
            spcl.center_x = random.randrange(SCREEN_WIDTH)
            spcl.center_y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)

            # Add the coin to the lists
            self.special_list.append(spcl)

    def on_show_view(self):
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

    def on_draw(self):
        self.clear()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        # Draw all the sprites.
        self.player_sprite_list.draw()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.explosions_list.draw()
        self.power_up_list.draw()
        self.heart_list.draw()
        self.special_list.draw()
        self.anders.draw()

        self.text_score.draw()
        self.lvl_txt.draw()
        self.high_score_text.draw()
        arcade.draw_text(f"Lives: {self.lives}", 10, 100,
                         arcade.color.WHITE, font_size=10, font_name="Kenney Future")

    def on_update(self, delta_time):

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.bullet_list.update()
        self.player_sprite_list.update()
        self.explosions_list.update()
        self.power_up_list.update()
        self.heart_list.update()
        self.special_list.update()
        self.anders.update()
        self.boundaries.update()
        self.time_taken += delta_time

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)
            spcl_hit = arcade.check_for_collision_with_list(bullet, self.special_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            if len(spcl_hit) > 0:
                bullet.remove_from_sprite_lists()
            for spcl in spcl_hit:
                spcl.remove_from_sprite_lists()
                self.score += 4
                self.nitro += 2
            for coin in hit_list:
                arcade.play_sound(self.explosion_sound)
                coin.remove_from_sprite_lists()
                explosion = Explosion(self.explosion_texture_list)

                explosion.center_x = hit_list[0].center_x

                explosion.center_y = hit_list[0].center_y

                explosion.update()

                # Add to a list of sprites that are explosions

                self.explosions_list.append(explosion)
                self.score += 1
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        if len(self.coin_list) == 0 and self.level == 1:
            self.level += 1
            self.level_2()
        elif len(self.coin_list) == 0 and self.level == 2:
            self.level += 1
            self.level_3()
        elif len(self.coin_list) == 0 and self.level == 3:
            self.level += 1
            self.level_4()
        elif len(self.coin_list) == 0 and self.level == 4:
            self.level += 1
            self.level_5()
        elif len(self.coin_list) == 0 and self.level == 5:
            self.level += 1
            self.level_6()

        hit_list_pu = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list_pu:
            arcade.play_sound(self.hit_sound)
            self.lives -= 1
            self.player_sprite.respawn()
            if self.lives == 0:
                global HIGH_SCORE
                if self.score > HIGH_SCORE:
                    HIGH_SCORE = self.score
                game_over_view = GameOverView()
                self.window.set_mouse_visible(True)
                self.window.show_view(game_over_view)
                game_over_view.time_taken = self.time_taken
                game_over_view.score = self.score
                game_over_view.high_score = HIGH_SCORE
                self.score = 0

        hit_list_pu2 = arcade.check_for_collision_with_list(self.player_sprite, self.power_up_list)
        for pu in hit_list_pu2:
            pu.remove_from_sprite_lists()
            self.score += 10

        hit_list_heart = arcade.check_for_collision_with_list(self.player_sprite, self.heart_list)
        for heart in hit_list_heart:
            heart.remove_from_sprite_lists()
            self.lives += 1
        hit_list_spcl = arcade.check_for_collision_with_list(self.player_sprite, self.special_list)
        for spcl in hit_list_spcl:
            self.player_sprite.respawn()

            self.lives -= 1
            self.score -= 3

        self.text_score.text = f"Score: {self.score}"
        self.lvl_txt.text = f"Level: {self.level}"
        self.lives_txt = f"Lives: {self.lives}"

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

        if key == arcade.key.SPACE:
            arcade.play_sound(self.shoot_sound)
            bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet.angle = 90

            # Give the bullet a speed
            bullet.change_y = BULLET_SPEED

            # Position the bullet

            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            # Add the bullet to the appropriate lists
            self.bullet_list.append(bullet)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.score = 0
        self.score2 = 0
        self.high_score = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text(f"Game Over ", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart or press 'Enter' to", 215, 300, arcade.color.WHITE, 24)
        arcade.draw_text("return back to the main menu", 215, 250, arcade.color.WHITE, 24)
        arcade.draw_text(f"Score: {self.score}",
                         378,
                         200,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text(f" High score: {self.high_score}",
                         378,
                         165,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            self.window.show_view(game_view)
        if key == arcade.key.ENTER:
            menu = MyWindow()
            self.window.show_view(menu)
        if key == arcade.key.C:
            game_view = ChangeShip()
            self.window.show_view(game_view)


class GameOverView2(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        self.score = 0
        self.score2 = 0
        self.high_score = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text(f"Game Over ", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart or press 'Enter' to", 215, 300, arcade.color.WHITE, 24)
        arcade.draw_text("return back to the main menu", 215, 250, arcade.color.WHITE, 24)
        arcade.draw_text(f"Player 1 score: {self.score}",
                         378,
                         200,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text(f"Player 2 score: {self.score2}",
                         378,
                         165,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            game_view = GameView()
            self.window.show_view(game_view)
        if key == arcade.key.ENTER:
            menu = MyWindow()
            self.window.show_view(menu)
        if key == arcade.key.C:
            game_view = ChangeShip()
            self.window.show_view(game_view)


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
    window.total_score = 0
    menu_view = MyWindow()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()