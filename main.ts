let ΕΝΤΑΣΗ_ΦΩΤΟΣ = 0
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    led.setBrightness(255)
    basic.showNumber(input.lightLevel())
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    led.setBrightness(input.lightLevel())
    basic.showLeds(`
        . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
        `)
    music.setVolume(input.lightLevel())
    music.playMelody("C5 B A G F E D C ", input.lightLevel())
    music.playMelody("C D E F G A B C5 ", input.lightLevel())
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    ΕΝΤΑΣΗ_ΦΩΤΟΣ = input.lightLevel()
    basic.clearScreen()
    led.setBrightness(ΕΝΤΑΣΗ_ΦΩΤΟΣ)
    basic.showLeds(`
        . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
        `)
    music.setVolume(ΕΝΤΑΣΗ_ΦΩΤΟΣ)
    music.playMelody("C5 B A G F E D C ", ΕΝΤΑΣΗ_ΦΩΤΟΣ)
    music.playMelody("C D E F G A B C5 ", ΕΝΤΑΣΗ_ΦΩΤΟΣ)
    basic.clearScreen()
})
