timer = 0
def on_button_pressed_a():
    global timer
    timer = randint(5, 15)
    basic.show_icon(IconNames.CHESSBOARD)
    basic.pause(1000 * randint(5, 15))
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.A, on_button_pressed_a)
