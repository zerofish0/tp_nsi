###[TP 9 : Microbit]###
## Zerofish0 + RR     #
#######################

##Impportations
from microbit import *
from random import *
import os
##Définitions des fonctions
def showpos(pos) :
    x,y = pos[0],pos[1]
    display.show(map[y][x])
##Variables
liste = [Image("99999:99999:99999:99999:99999"),
Image("99999:99599:95559:99599:99999"),
Image("99599:95359:53335:95359:99599"),
Image("95359:53035:30003:53035:95359"),
Image("53035:30003:00000:30003:53035"),
Image("30003:00000:00000:00000:30003"),
Image("00000:00000:00000:00000:00000")]
pickaxe = Image("07770:77977:50905:00900:00900")
de = [Image('00000:03330:03930:03330:00000'),Image('00333:00393:33333:39300:33300'),Image('00039:03333:03930:33330:93000'),Image('93039:33033:00000:33033:93039'),Image('93039:33333:03930:33333:93039'),Image('39393:33333:39393:33333:39393')]
nbr = ['1','2','3','4','5','6','7','8','9','10','V','D','R']
symbole = [Image('00900:09990:99999:09990:00900'),Image.HEART, Image('00900:09990:99999:99999:00900'),Image('09900:09999:99999:99900:00900')]
sensivity = 200
score = 0
map = [
    [Image("90000:00000:00000:00000:00000"),Image("09000:00000:00000:00000:00000"),Image("00900:00000:00000:00000:00000"),Image("00090:00000:00000:00000:00000"),Image("00009:00000:00000:00000:00000")],
    [Image("00000:90000:00000:00000:00000"),Image("00000:09000:00000:00000:00000"),Image("00000:00900:00000:00000:00000"),Image("00000:00090:00000:00000:00000"),Image("00000:00009:00000:00000:00000")],
    [Image("00000:00000:90000:00000:00000"),Image("00000:00000:09000:00000:00000"),Image("00000:00000:00900:00000:00000"),Image("00000:00000:00090:00000:00000"),Image("00000:00000:00009:00000:00000")],
    [Image("00000:00000:00000:90000:00000"),Image("00000:00000:00000:09000:00000"),Image("00000:00000:00000:00900:00000"),Image("00000:00000:00000:00090:00000"),Image("00000:00000:00000:00009:00000")],
    [Image("00000:00000:00000:00000:90000"),Image("00000:00000:00000:00000:09000"),Image("00000:00000:00000:00000:00900"),Image("00000:00000:00000:00000:00090"),Image("00000:00000:00000:00000:00009")],
]
load = "random"
##Programme principal
#!!!Pour faire fonctionner le gyroscope, commenter le plus de variables possible
if load == "gyroscope":
    difficulty = 1
    while not(button_a.is_pressed()):
        display.show(difficulty)
        if button_b.is_pressed():
            if difficulty != 9:
                difficulty += 1
                sleep(200)
            else :
                difficulty = 1
                sleep(200)
    sensivity = difficulty*50
while True:
    if load == "animation" :
        display.show(liste,delay=300)
        sleep(2000)

    elif load == "random" :
        if button_a.is_pressed():
            display.show(choice(de))
            sleep(1000)
            display.clear()
        elif button_b.is_pressed():
            display.show([choice(nbr),choice(symbole)],delay = 800)
            sleep(1000)
            display.clear()
    elif load == "pin" :
        if pin0.is_touched():
            display.show(Image.HAPPY)
        else :
            display.show(Image.SAD)
    elif load == "gyroscope" :
        compteur = 0
        goalpos = [randint(0,4),randint(0,4)]
        position = [randint(0,4),randint(0,4)]
        showpos(goalpos)
        sleep(1000)
        for i in range(3,0,-1) :
            display.show(i)
            sleep(1000)
        timer = 0
        while 1 :
            if button_b.is_pressed():score += 9999
            timer += 0.1
            if button_a.is_pressed() or timer > 9+difficulty:

                display.scroll("GAME OVER")
                sleep(500)
                while 1 :
                    display.scroll("score : " + str(score))
            if position == goalpos :
                compteur+=1
            else : compteur = 0
            if compteur > 30 :
                display.show(Image.HAPPY)
                score += int(100000/timer/sensivity)
                sleep(2000)
                break
            modfx = accelerometer.get_x()
            modfy = accelerometer.get_y()

            if modfx>sensivity and position[0] != 4:
                position[0]+=1
                sleep(100)
            elif modfx<-sensivity and position[0] != 0 :
                position[0] -= 1
                sleep(100)

            if modfy>sensivity and position[1] != 4:
                position[1]+=1
                sleep(100)
            elif modfy<-sensivity and position[1] != 0 :
                position[1] -= 1
                sleep(100)
            showpos(position)
            sleep(100)





