
print("Hello, world!")
from ST7735 import TFT
#from sysfont import sysfont
import machine
from machine import SPI, Pin, PWM
import time
import math

backlight = machine.Pin(27, machine.Pin.OUT)
led_pwm = PWM(backlight, freq=500, duty=5)
# backlight.value(1)

spi = SPI(-1, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(23))
#spi = SPI(2, baudrate=20000000)
#spi = SPI(2, baudrate=20000000, polarity=0, phase=0)

DC = 23
RESET = 26
CS = 5
tft=TFT(spi, DC, RESET, CS)
tft.initg()
tft.rgb(True)

def testlines(color):
    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((0,0),(x, tft.size()[1] - 1), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((0,0),(tft.size()[0] - 1, y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((tft.size()[0] - 1, 0), (x, tft.size()[1] - 1), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((tft.size()[0] - 1, 0), (0, y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((0, tft.size()[1] - 1), (x, 0), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((0, tft.size()[1] - 1), (tft.size()[0] - 1,y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (x, 0), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (0, y), color)

def testfastlines(color1, color2):
    tft.fill(TFT.BLACK)
    for y in range(0, tft.size()[1], 5):
        tft.hline((0,y), tft.size()[0], color1)
    for x in range(0, tft.size()[0], 5):
        tft.vline((x,0), tft.size()[1], color2)

def testdrawrects(color):
    tft.fill(TFT.BLACK);
    for x in range(0,tft.size()[0],6):
        tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color)

def testfillrects(color1, color2):
    tft.fill(TFT.BLACK);
    for x in range(tft.size()[0],0,-6):
        tft.fillrect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color1)
        tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color2)


def testfillcircles(radius, color):
    for x in range(radius, tft.size()[0], radius * 2):
        for y in range(radius, tft.size()[1], radius * 2):
            tft.fillcircle((x, y), radius, color)

def testdrawcircles(radius, color):
    for x in range(0, tft.size()[0] + radius, radius * 2):
        for y in range(0, tft.size()[1] + radius, radius * 2):
            tft.circle((x, y), radius, color)

def testtriangles():
    tft.fill(TFT.BLACK);
    color = 0xF800
    w = tft.size()[0] // 2
    x = tft.size()[1] - 1
    y = 0
    z = tft.size()[0]
    for t in range(0, 15):
        tft.line((w, y), (y, x), color)
        tft.line((y, x), (z, x), color)
        tft.line((z, x), (w, y), color)
        x -= 4
        y += 4
        z -= 4
        color += 100

def testroundrects():
    tft.fill(TFT.BLACK)
    color = 100
    for t in range(5):
        x = 0
        y = 0
        w = tft.size()[0] - 2
        h = tft.size()[1] - 2
        for i in range(17):
            tft.rect((x, y), (w, h), color)
            x += 2
            y += 3
            w -= 4
            h -= 6
            color += 1100
        color += 100

def test_main():
    tft.fill(TFT.WHITE)
    time.sleep_ms(1000)

    time.sleep_ms(4000)

    testlines(TFT.YELLOW)
    time.sleep_ms(500)

    testfastlines(TFT.RED, TFT.BLUE)
    time.sleep_ms(500)

    testdrawrects(TFT.GREEN)
    time.sleep_ms(500)

    testfillrects(TFT.YELLOW, TFT.PURPLE)
    time.sleep_ms(500)

    tft.fill(TFT.BLACK)
    testfillcircles(10, TFT.BLUE)
    testdrawcircles(10, TFT.WHITE)
    time.sleep_ms(500)

    testroundrects()
    time.sleep_ms(500)

    testtriangles()
    time.sleep_ms(500)

test_main()
