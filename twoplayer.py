import arcade

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



class Player2(arcade.Sprite):

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

        texture = arcade.load_texture("D:\Python Wesley\Python\pythonProject\\venv\lib\python3.11\site-packages\\arcade\\resources\images\space_shooter\\red_ship.png")

        self.textures.append(texture)

        texture = arcade.load_texture("D:\Python Wesley\Python\pythonProject\\venv\lib\python3.11\site-packages\\arcade\\resources\images\space_shooter\\red_ship.png",

                                      flipped_horizontally=False)

        self.textures.append(texture)

        # By default, face right.

        self.texture = texture

    def respawn(self):
        self.respawning = 1

        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT

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



class Game3View(arcade.View):
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
        self.player_sprite2 = None
        self.ship = None
        self.heart = None
        self.power_up = None
        self.nitro = None
        self.coin = None
        self.bullet_list = None
        self.bullet_list2 = None
        self.text_score = None
        self.lives_txt = None
        self.score = None
        self.health = None
        self.health2 = None
        self.level = None
        self.lvl_txt = None
        self.anders = None
        self.high_score = None
        self.current = None
        self.scores = None
        self.scores2 = None

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
        self.player_sprite_list2 = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.bullet_list2 = arcade.SpriteList()
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
        self.score2 = 0
        self.level = 1
        self.lives = 2
        self.lives2 = 2
        self.health = 2
        self.nitro = 0
        self.high_score = 0
        self.current = self.high_score

        # Set up the player
        self.player_sprite = Player()
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        self.player_sprite2 = Player2()
        self.player_sprite2.center_x = SCREEN_WIDTH / 2
        self.player_sprite2.center_y = SCREEN_HEIGHT
        self.player_sprite_list2.append(self.player_sprite2)

        self.text_score = arcade.Text(
            f"Player 1: {self.score}",
            start_x=625,
            start_y=475,
            font_size=20,
        )

        self.high_score_text = arcade.Text(
            f"Player 2: {self.score}",
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
            f"",
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
        self.player_sprite_list2.draw()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.bullet_list2.draw()
        self.explosions_list.draw()
        self.power_up_list.draw()
        self.heart_list.draw()
        self.special_list.draw()
        self.anders.draw()

        self.text_score.draw()
        self.lvl_txt.draw()
        arcade.draw_text(f"Lives: {self.lives}", 10, 100,
                         arcade.color.WHITE, font_size=10, font_name="Kenney Future")

    def on_update(self, delta_time):

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.bullet_list.update()
        self.bullet_list2.update()
        self.player_sprite_list.update()
        self.player_sprite_list2.update()
        self.explosions_list.update()
        self.power_up_list.update()
        self.heart_list.update()
        self.special_list.update()
        self.anders.update()
        self.boundaries.update()
        self.time_taken += delta_time

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.player_sprite_list2)
            spcl_hit = arcade.check_for_collision_with_list(bullet, self.special_list)
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                self.score += 1
                game_over = GameOverView2()
                game_over.score = self.score
                game_over.score2 = self.score2
                self.window.show_view(game_over)
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

        for bullet2 in self.bullet_list2:
            hit_list = arcade.check_for_collision_with_list(bullet2, self.player_sprite_list)
            spcl_hit = arcade.check_for_collision_with_list(bullet2, self.special_list)
            if len(hit_list) > 0:
                bullet2.remove_from_sprite_lists()
                self.score2 += 1
                game_over = GameOverView2()
                game_over.score = self.score
                game_over.score2 = self.score2
                self.window.show_view(game_over)
            if len(spcl_hit) > 0:
                bullet2.remove_from_sprite_lists()
                self.score2 += 1
            for spcl in spcl_hit:
                spcl.remove_from_sprite_lists()
                self.score2 += 4
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
            if bullet2.bottom > SCREEN_HEIGHT:
                bullet2.remove_from_sprite_lists()

        hit_list_pu = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list2)
        for bullet2 in hit_list_pu:
            arcade.play_sound(self.hit_sound)
            game_over = GameOverView2()
            self.window.show_view(game_over)

        hit_list_pu2 = arcade.check_for_collision_with_list(self.player_sprite2, self.coin_list)
        for coin in hit_list_pu2:
            arcade.play_sound(self.hit_sound)
            self.lives2 -= 1
            self.player_sprite2.respawn()
            if self.lives == 0:
                self.player_sprite2.remove_from_sprite_lists()

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

        if key == arcade.key.W:
            self.player_sprite2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite2.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite2.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite2.change_x = MOVEMENT_SPEED

        if key == arcade.key.X:
            arcade.play_sound(self.shoot_sound)
            bullet2 = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_LASER)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet2.angle = 180

            # Give the bullet a speed
            bullet2.change_y = -BULLET_SPEED

            # Position the bullet

            bullet2.center_x = self.player_sprite2.center_x
            bullet2.top = self.player_sprite2.bottom

            # Add the bullet to the appropriate lists
            self.bullet_list2.append(bullet2)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite2.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite2.change_x = 0


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
        if self.score > self.score2:
            arcade.draw_text(f"Game Over: Player 1 won! ", 240, 400, arcade.color.WHITE, 20)
        elif self.score < self.score2:
            arcade.draw_text(f"Game Over: Player 2 won! ", 240, 400, arcade.color.WHITE, 54)
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



