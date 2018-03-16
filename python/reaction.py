from gpiozero import LED, Button
from time import sleep
from random import uniform
from signal import pause
from sys import exit

left_name = raw_input('Left player name is: ')
right_name = raw_input('Right player name is: ')

led = LED(6)
left_led = LED(20)
left_score = 0
right_led = LED(16)
right_score = 0
left_button = Button(17) ##Closes to breadboard T
right_button = Button(27)

##left_button.wait_for_press()
##print('Left button was pressed')
##right_button.wait_for_press()
##print('Right button was pressed')

def pressed(button):
    if led.is_lit == False:
        if button.pin.number == 17:
            left_led.on()
            print(left_name+' won the game!')
            global left_score
            left_score += 10
            sleep(2)
            left_led.off()
        else:
            right_led.on()
            print(right_name+' won the game!')
            global right_score
            right_score += 10
            sleep(2)
            right_led.off()

left_button.when_pressed = pressed
right_button.when_pressed = pressed

def countDown(interval):
    for x in range(interval,0,-1):
        print('Next game starting in '+str(x)+'seconds')
        sleep(1)

stop = False
restart = False

while stop == False:
    led.on()
    sleep(uniform(5,10))
    led.off()
    sleep(1)
    print('Current score ' + left_name + ': ' + str(left_score) + '... ' + right_name + ': ' + str(right_score))
    play_again = raw_input('Would you like to play again? (y,n)')
    if play_again == 'y':
        stop = False
        countDown(5)
    else:
        print('FINAL SCORE ---> '+left_name+': '+str(left_score)+'... '+right_name+': '+str(right_score))
        print('Exiting game now...')
        stop = True
