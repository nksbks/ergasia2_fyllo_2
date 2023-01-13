ΕΝΤΑΣΗ_ΦΩΤΟΣ = 0

def on_button_pressed_ab():
    basic.clear_screen()
    led.set_brightness(255)
    basic.show_number(input.light_level())
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_a():
    basic.clear_screen()
    led.set_brightness(input.light_level())
    basic.show_leds("""
        . # . # .
                # . # . #
                # . . . #
                . # . # .
                . . # . .
    """)
    music.set_volume(input.light_level())
    music.play_melody("C5 B A G F E D C ", input.light_level())
    music.play_melody("C D E F G A B C5 ", input.light_level())
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global ΕΝΤΑΣΗ_ΦΩΤΟΣ
    ΕΝΤΑΣΗ_ΦΩΤΟΣ = input.light_level()
    basic.clear_screen()
    led.set_brightness(ΕΝΤΑΣΗ_ΦΩΤΟΣ)
    basic.show_leds("""
        . # . # .
                # . # . #
                # . . . #
                . # . # .
                . . # . .
    """)
    music.set_volume(ΕΝΤΑΣΗ_ΦΩΤΟΣ)
    music.play_melody("C5 B A G F E D C ", ΕΝΤΑΣΗ_ΦΩΤΟΣ)
    music.play_melody("C D E F G A B C5 ", ΕΝΤΑΣΗ_ΦΩΤΟΣ)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
