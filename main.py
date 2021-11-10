def on_button_pressed_a():
    if game_start == 2:
        if paddleA.get(LedSpriteProperty.X) > 0:
            paddleA.change(LedSpriteProperty.X, -1)
    if game_start == 1:
        if paddleA.get(LedSpriteProperty.X) > 0:
            paddleA.change(LedSpriteProperty.X, -1)
            paddleB.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global game_start, paddleA, ball, directionY, directionX
    basic.clear_screen()
    game_start = 2
    if game_start == 2:
        music.stop_melody(MelodyStopOptions.ALL)
        paddleA = game.create_sprite(2, 4)
        ball = game.create_sprite(randint(0, 4), 0)
        directionY = 1
        directionX = randint(-1, 1)
        basic.pause(500)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if game_start == 2:
        paddleA.change(LedSpriteProperty.X, 1)
    if game_start == 1:
        if paddleA.get(LedSpriteProperty.X) > 0:
            paddleA.change(LedSpriteProperty.X, -1)
            paddleB.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global game_start
    game_start = 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

game_over = 0
paddle_hit = 0
score = 0
hits = 0
directionX = 0
directionY = 0
ball: game.LedSprite = None
paddleB: game.LedSprite = None
paddleA: game.LedSprite = None
start_music = 0
game_start = 0
music.start_melody(music.built_in_melody(Melodies.PRELUDE),
    MelodyOptions.FOREVER)
while game_start == 0:
    start_music += 1
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                # # # # #
                # . . . #
    """)
    basic.pause(500)
    basic.show_leds("""
        . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
    """)
    basic.pause(500)
    basic.show_leds("""
        # # # # .
                # . . # .
                # # # . .
                # . . # .
                # # # # .
    """)
    basic.pause(500)
if game_start == 1:
    music.stop_melody(MelodyStopOptions.ALL)
    paddleA = game.create_sprite(2, 4)
    paddleB = game.create_sprite(3, 4)
    ball = game.create_sprite(randint(0, 4), 0)
    directionY = 1
    directionX = randint(-1, 1)
    basic.pause(500)

def on_forever():
    global hits, score, directionY, directionX, paddle_hit, game_over
    ball.change(LedSpriteProperty.X, directionX)
    ball.change(LedSpriteProperty.Y, directionY)
    if ball.is_touching(paddleA) or ball.is_touching(paddleB):
        hits += 1
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        score += 1
        basic.show_string("" + str((score)))
        ball.change(LedSpriteProperty.X, directionX * -1)
        ball.change(LedSpriteProperty.Y, -1)
        directionY = -1
        directionX = randint(-1, 1)
        paddle_hit += -1
    else:
        if ball.get(LedSpriteProperty.Y) <= 0:
            hits += 1
            music.play_tone(220, music.beat(BeatFraction.WHOLE))
            directionY = 1
            directionX = randint(-1, 1)
        elif ball.get(LedSpriteProperty.Y) >= 4:
            hits += 1
            game_over += 1
            music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
            ball.set(LedSpriteProperty.BLINK, 1)
            basic.pause(2000)
            basic.show_leds("""
                . # # # .
                                . # . . .
                                . # # # .
                                . # . . .
                                . # . . .
            """)
            basic.show_string("Score: ")
            basic.show_string("" + str((score)))
            basic.show_string("Total bounces :")
            basic.show_string("" + str((hits)))
            basic.pause(500)
            control.reset()
        if ball.get(LedSpriteProperty.X) <= 0:
            hits += 1
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            directionX = 1
        elif ball.get(LedSpriteProperty.X) >= 4:
            hits += 1
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            directionX = -1
        basic.pause(500)
basic.forever(on_forever)
