input.onPinPressed(TouchPin.P0, function () {
    music.playTone(262, music.beat(BeatFraction.Whole))
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.clearScreen()
    basic.showNumber(randint(1, 6))
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showNumber(Stappen)
})
input.onGesture(Gesture.Shake, function () {
    Stappen += 1
})
input.onPinPressed(TouchPin.P2, function () {
    music.playTone(330, music.beat(BeatFraction.Whole))
})
input.onButtonPressed(Button.AB, function () {
    music.playMelody("C D E C C D E C ", 120)
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    BST = randint(1, 3)
    Computerbst = randint(1, 3)
    if (BST == 1) {
        if (Computerbst == 1) {
            basic.showString("Gelijk")
            basic.clearScreen()
        }
        if (Computerbst == 2) {
            basic.showString("Gewonnen")
            basic.clearScreen()
        }
        if (Computerbst == 3) {
            basic.showString("Verloren")
            basic.clearScreen()
        }
    }
    if (BST == 2) {
        if (Computerbst == 1) {
            basic.showString("Verloren")
            basic.clearScreen()
        }
        if (Computerbst == 2) {
            basic.showString("Gelijk")
            basic.clearScreen()
        }
        if (Computerbst == 3) {
            basic.showString("Gewonnen")
            basic.clearScreen()
        }
    }
    if (BST == 3) {
        if (Computerbst == 1) {
            basic.showString("Gewonnen")
            basic.clearScreen()
        }
        if (Computerbst == 2) {
            basic.showString("Verloren")
            basic.clearScreen()
        }
        if (Computerbst == 3) {
            basic.showString("Gelijk")
            basic.clearScreen()
        }
    }
})
input.onPinPressed(TouchPin.P1, function () {
    music.playTone(294, music.beat(BeatFraction.Whole))
})
input.onSound(DetectedSound.Loud, function () {
    basic.clearScreen()
    BSTManual = randint(1, 3)
    while (BSTManual == 1) {
        basic.showString("Blad")
        basic.clearScreen()
        BSTManual = 0
    }
    while (BSTManual == 2) {
        basic.showString("Steen")
        basic.clearScreen()
        BSTManual = 0
    }
    while (BSTManual == 3) {
        basic.showString("Schaar")
        basic.clearScreen()
        BSTManual = 0
    }
})
let BSTManual = 0
let Computerbst = 0
let BST = 0
let Stappen = 0
soundExpression.soaring.play()
for (let index = 0; index < 4; index++) {
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Diamond)
}
basic.showString("Hallo Robin")
Stappen = 0
