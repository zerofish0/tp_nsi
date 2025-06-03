###[TP 9 : Microbit (lumière intelligente)]###
## Zerofish0 + RR                            #
##############################################

##Importations
from microbit import *

##Définitions de fonctions
def LED(pin,stat):
    if pin==0:
        if (stat=='ON'):
            pin0.write_digital(1)
        elif (stat=='OFF'):
            pin0.write_digital(0)
        else:
            display.scroll('MAUVAIS ETAT!')

    elif pin==1:
        if (stat=='ON'):
            pin1.write_digital(1)
        elif (stat=='OFF'):
            pin1.write_digital(0)
        else:
            display.scroll('MAUVAIS ETAT!')

    elif pin==2:
        if (stat=='ON'):
            pin2.write_digital(1)
        elif (stat=='OFF'):
            pin2.write_digital(0)
        else:
            display.scroll('MAUVAIS ETAT!')

    else:
        display.scroll('MAUVAIS PIN!')

def CapLum(pin):
    if pin==0:
        return(pin0.read_analog())

    elif pin==1:
        return(pin1.read_analog())

    elif pin==2:
        return(pin2.read_analog())

    else:
        display.scroll('MAUVAIS PIN!')
##Variables
button_a_bool = False
led1pin = 2
led2pin = 0
compteur = 0
## Programme principal
while 1 :
    if button_b.is_pressed() :
        sleep(300)
        LED(led1pin,"OFF")
        LED(led2pin,"OFF")
        display.clear()
        while not button_b.is_pressed():
            LED(led1pin,"ON")
            sleep(100)
            LED(led1pin,"OFF")
            LED(led2pin,"ON")
            sleep(100)
            LED(led2pin,"OFF")

    if button_a.is_pressed() :
        button_a_bool = not button_a_bool
        sleep(200)

    if button_a_bool and compteur < 5 :
        LED(led1pin,"ON")
        display.show(Image.YES)
        compteur += 0.1
    else :
        if compteur != 0:
            display.show(Image.TRIANGLE)
            sleep(500)
        LED(led1pin,"OFF")
        display.show(Image.NO)
        compteur = 0
        button_a_bool = False

    if 200 < CapLum(1) < 400:
        LED(led1pin,"ON")
    elif CapLum(1) < 150:
        LED(led1pin,"ON")
        LED(led2pin,"ON")
    else :
        if not(button_a_bool):
            LED(led1pin,"OFF")
        LED(led2pin,"OFF")
    sleep(100)









