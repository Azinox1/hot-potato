let timer = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    timer = randint(5, 15)
    basic.showIcon(IconNames.Chessboard)
    basic.pause(1000 * randint(5, 15))
    basic.showIcon(IconNames.Skull)
})
