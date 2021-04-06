def on_pin_pressed_p0():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_logo_touched():
    basic.clear_screen()
    basic.show_number(randint(1, 6))
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_button_pressed_a():
    basic.clear_screen()
    basic.show_number(Stappen)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global Stappen
    Stappen += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_pin_pressed_p2():
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    music.play_melody("C D E C C D E C ", 120)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global BST, Computerbst
    basic.clear_screen()
    BST = randint(1, 3)
    Computerbst = randint(1, 3)
    if BST == 1:
        if Computerbst == 1:
            basic.show_string("Gelijk")
            basic.clear_screen()
        if Computerbst == 2:
            basic.show_string("Gewonnen")
            basic.clear_screen()
        if Computerbst == 3:
            basic.show_string("Verloren")
            basic.clear_screen()
    if BST == 2:
        if Computerbst == 1:
            basic.show_string("Verloren")
            basic.clear_screen()
        if Computerbst == 2:
            basic.show_string("Gelijk")
            basic.clear_screen()
        if Computerbst == 3:
            basic.show_string("Gewonnen")
            basic.clear_screen()
    if BST == 3:
        if Computerbst == 1:
            basic.show_string("Gewonnen")
            basic.clear_screen()
        if Computerbst == 2:
            basic.show_string("Verloren")
            basic.clear_screen()
        if Computerbst == 3:
            basic.show_string("Gelijk")
            basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_sound_loud():
    global BSTManual
    basic.clear_screen()
    BSTManual = randint(1, 3)
    while BSTManual == 1:
        basic.show_string("Blad")
        basic.clear_screen()
        BSTManual = 0
    while BSTManual == 2:
        basic.show_string("Steen")
        basic.clear_screen()
        BSTManual = 0
    while BSTManual == 3:
        basic.show_string("Schaar")
        basic.clear_screen()
        BSTManual = 0
input.on_sound(DetectedSound.LOUD, on_sound_loud)

BSTManual = 0
Computerbst = 0
BST = 0
Stappen = 0
soundExpression.soaring.play()
for index in range(4):
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.DIAMOND)
basic.show_string("Hallo Robin")
Stappen = 0
