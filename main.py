import logging
from pyautogui import click, press, moveTo
import pyautogui
from time import sleep

from utils import obtainCords, obtainWaitCords, isInMenu, isVisible

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
logging.debug("Program started...")

class GameRegion:
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

    def toTuple(self):
        return (self.startX, self.startY, self.endX, self.endY)
    
    def obtainMiddle(self):
        return (self.startX+(self.endX - self.startX)/2, self.startY+ (self.endY-self.startY)/2)

def obtainGameRegion():
    (x,y,_,h) = obtainCords("nox", False)
    starty = y+h # it gives us the start points of the corner of the game
    return GameRegion(x, starty, x-5+960, starty-5+540) # the -5 is to move just a little bit up the cursor

def quickFight(gameRegion):
    # click on the quickFight button
    (x,y) = obtainCords("quickFight", True, gameRegion.toTuple())
    click(x,y)

    # wait some time until the game loads 
    obtainWaitCords("startFight", gameRegion.toTuple())

    # we start the game
    (xM, yM) = gameRegion.obtainMiddle()
    click(xM, yM)

    # wait until the battle is finished and press the escape key
    obtainWaitCords("endFight", gameRegion.toTuple())
    press("escape", interval=2)


def leagueFight(gameRegion):
    # wait some time until the game loads 
    obtainWaitCords("startFight", gameRegion.toTuple())

    # we start the game
    (xM, yM) = gameRegion.obtainMiddle()
    click(xM, yM)

    # wait until the battle is finished and press the escape key
    (x,y) = obtainWaitCords("ok", gameRegion.toTuple())
    press("escape", interval=3)

    # we press the continue button or the ok one

    isFinished = isVisible("ok", gameRegion.toTuple())
    isContination = isVisible("continue", gameRegion.toTuple())
    isLose = isVisible("lose", gameRegion.toTuple())

    while(True):
        logging.debug(f"isLose: {isLose}")
        if(isContination):
            (x,y) = obtainWaitCords("continue", gameRegion.toTuple())
            click(x, y)
            break
        if(isFinished or isLose):
            logging.debug("Exit this run beause it finished or we lose it")
            sleep(3)
            press("escape")
            press("escape", interval=3)
            return
        isFinished = isVisible("ok", gameRegion.toTuple())
        isContination = isVisible("continue", gameRegion.toTuple())
        isLose = isVisible("lose", gameRegion.toTuple())

def leagueFightAll(gameRegion):
    # click on the arrow button
    (x,y) = obtainCords("arrow", gameRegion.toTuple())
    click(x,y)

    # click on the leagueFight button
    (x, y) = obtainWaitCords("leagueFight", gameRegion.toTuple())
    sleep(4) # we sleep some time to give the game some time to finish loading
    click(x,y)

    while(True):
        leagueFight(gameRegion)
        sleep(3) # we sleep some time to give the game some time to finish loading
        if(isVisible("leagueFight", gameRegion.toTuple())):
            click(x,y)

def quickFightAll(gameRegion):
    while(True):
        if(not isInMenu(gameRegion.toTuple())):
            print("The game is no in menu yet, going to wait some time")
            sleep(2)
            continue

        sleep(0.5) # we need to wait some time before the quick fight button is clickable
        quickFight(gameRegion)

def championship(gameRegion):
    # click the championship button
    (x, y) = obtainCords("championship", True, gameRegion.toTuple())
    click(x,y)

    sleep(2)

    # we click the claim button if it exists
    isClaimButton = isVisible("claim", gameRegion.toTuple())
    if(isClaimButton):
        press("escape", interval=3)

    # TODO: we click the ok button if someone promote

    # we click on the fight button
    (x, y) = obtainWaitCords("fight", gameRegion.toTuple())
    sleep(1)
    # we need to do this because this button has some animation sometimes, so it is'nt detected by pyautogui
    x = gameRegion.endX-30
    y= gameRegion.endY-30
    click(x,y)

    # wait some time until the game loads 
    obtainWaitCords("startFight", gameRegion.toTuple())

    # we start the game
    (xM, yM) = gameRegion.obtainMiddle()
    click(xM, yM)

    # we wait until all the fights are done and press the ok button
    obtainWaitCords("ok", gameRegion.toTuple())
    sleep(3)

    # we press the scape key to go back to the main menu again
    press("escape", interval=3)
    press("escape", interval=3)

def  championshipAll(gameRegion):
    while(True):
        if(not isInMenu(gameRegion.toTuple())):
            print("The game is no in menu yet, going to wait some time")
            sleep(2)
            continue

        sleep(5) # we need to wait some time before the quick fight button is clickable
        championship(gameRegion)

def main():
    while True:
        try:
            print("1. QuickFights")
            print("2. LeagueFights")
            print("3. Championships")

            num = int(input("Please enter the task you want to do with the bot: \n"))

            if(num >= 4):
                raise ValueError()

            gameRegion = obtainGameRegion()
            if(num == 1):
                quickFightAll(gameRegion)
            if(num == 2):
                leagueFightAll(gameRegion)
            if(num == 3):
                championshipAll(gameRegion)
        except ValueError:
            print("Invalid input, please prove a valid one")

if __name__ == "__main__":
    main()