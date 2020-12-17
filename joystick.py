from gpiozero import LED
from time import sleep

joystick_up = Joystick(7)
joystick_down = Joystick(17)
joystick_left = Joystick(27)
joystick_right = Joystick(22)

while True:
    joystick_up
    print('up')
    sleep(1)
while True:
    joystick_down
    print('down')
    sleep(1)
while True:
    joystick_left
    print('left')
    sleep(1)
while True:
    joystick_right
    print('right')
    sleep(1)