input.onButtonPressed(Button.A, function () {
    if (game_start == 1) {
        if (paddleA.get(LedSpriteProperty.X) > 0) {
            paddleA.change(LedSpriteProperty.X, -1)
            paddleB.change(LedSpriteProperty.X, -1)
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    game_start = 1
})
input.onButtonPressed(Button.B, function () {
    if (game_start == 1) {
        if (paddleA.get(LedSpriteProperty.X) < 3) {
            paddleA.change(LedSpriteProperty.X, 1)
            paddleB.change(LedSpriteProperty.X, 1)
        }
    }
})
let game_over = 0
let paddle_hit = 0
let score = 0
let hits = 0
let directionX = 0
let directionY = 0
let ball: game.LedSprite = null
let paddleB: game.LedSprite = null
let paddleA: game.LedSprite = null
let start_music = 0
let game_start = 0
music.startMelody(music.builtInMelody(Melodies.Prelude), MelodyOptions.Forever)
while (game_start == 0) {
    start_music += 1
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        # # # # #
        # . . . #
        `)
    basic.pause(500)
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        `)
    basic.pause(500)
    basic.showLeds(`
        # # # # .
        # . . # .
        # # # . .
        # . . # .
        # # # # .
        `)
    basic.pause(500)
}
if (game_start == 1) {
    music.stopMelody(MelodyStopOptions.All)
    paddleA = game.createSprite(2, 4)
    paddleB = game.createSprite(3, 4)
    ball = game.createSprite(randint(0, 4), 0)
    directionY = 1
    directionX = randint(-1, 1)
    basic.pause(500)
}
basic.forever(function () {
    ball.change(LedSpriteProperty.X, directionX)
    ball.change(LedSpriteProperty.Y, directionY)
    if (ball.isTouching(paddleA) || ball.isTouching(paddleB)) {
        hits += 1
        music.playTone(262, music.beat(BeatFraction.Whole))
        score += 1
        basic.showString("" + (score))
        ball.change(LedSpriteProperty.X, directionX * -1)
        ball.change(LedSpriteProperty.Y, -1)
        directionY = -1
        directionX = randint(-1, 1)
        paddle_hit += -1
    } else {
        if (ball.get(LedSpriteProperty.Y) <= 0) {
            hits += 1
            music.playTone(220, music.beat(BeatFraction.Whole))
            directionY = 1
            directionX = randint(-1, 1)
        } else if (ball.get(LedSpriteProperty.Y) >= 4) {
            hits += 1
            game_over += 1
            music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
            ball.set(LedSpriteProperty.Blink, 1)
            basic.pause(2000)
            basic.showLeds(`
                . # # # .
                . # . . .
                . # # # .
                . # . . .
                . # . . .
                `)
            basic.showString("Score: ")
            basic.showString("" + (score))
            basic.showString("Total bounces :")
            basic.showString("" + (hits))
            basic.pause(500)
            control.reset()
        }
        if (ball.get(LedSpriteProperty.X) <= 0) {
            hits += 1
            music.playTone(330, music.beat(BeatFraction.Whole))
            directionX = 1
        } else if (ball.get(LedSpriteProperty.X) >= 4) {
            hits += 1
            music.playTone(330, music.beat(BeatFraction.Whole))
            directionX = -1
        }
        basic.pause(500)
    }
})
