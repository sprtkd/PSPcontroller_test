import psp2d

def drawGamePadTest(pad,image):
    if pad.up:
        font.drawText(image, 30, 80, "UP")
    if pad.down:
        font.drawText(image, 30, 110, "DOWN")
    if pad.left:
        font.drawText(image, 0, 95, "LEFT")
    if pad.right:
        font.drawText(image, 60, 95, "RIGHT")

        
    if pad.triangle:
        font.drawText(image, 130+30, 80, "TRIANGLE")
    if pad.cross:
        font.drawText(image, 130+30, 110, "CROSS")
    if pad.square:
        font.drawText(image, 130+0, 95, "SQUARE")
    if pad.circle:
        font.drawText(image, 130+60, 95, "CIRCLE")
        
    if pad.l:
        font.drawText(image, 0, 60, "LEFT TRIG")
    if pad.r:
        font.drawText(image, 160, 60, "RIGHT TRIG")
    if pad.start:
        font.drawText(image, 120, 130, "START")
    if pad.select:
        font.drawText(image, 60, 130, "SELECT")
    if pad.analogX:
        font.drawText(image, 0, 150, "ANALOG_X= "+str(pad.analogX))
    if pad.analogY:
        font.drawText(image, 0, 170, "ANALOG_Y= "+str(pad.analogY))
    return image


font = psp2d.Font("font.png")
image = psp2d.Image(480, 272)
screen = psp2d.Screen()
CLEAR_COLOR = psp2d.Color(0,0,0)
image.clear(CLEAR_COLOR)
x = True
while x == True:
    image.clear(CLEAR_COLOR)
    font.drawText(image, 70, 0, "--PSP CONTROLLER TEST--")
    font.drawText(image, 50, 30, "------------------------------------")
    font.drawText(image, 70, 210, "WRITTEN BY: SUPROTIK DEY")
    pad = psp2d.Controller()
    image = drawGamePadTest(pad,image)
    screen.blit(image)
    screen.swap()
