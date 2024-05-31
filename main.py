import logging
from pyautogui import click, press
import pyautogui
from time import sleep

from utils import obtainCords, obtainWaitCords, isInMenu, img2Text

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
        return ((self.endX - self.startX)/2, (self.endY-self.startY)/2)

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


def main():
    gameRegion = obtainGameRegion()
    r = img2Text("pics/value.png")
    print(r)
    # while(True):
    #     if(not isInMenu(gameRegion.toTuple())):
    #         print("The game is no in meny yet, going to wait some time")
    #         sleep(2)
    #         continue

    #     sleep(0.5) # we need to wait some time before the quick fight button is clickable
    #     quickFight(gameRegion)


# championship:
# we click the championship button
# we click the claim button if it exists
# we click the ok button if someone promes
# we click on the fight button
# we wait until the game loads
# we click on the first fight
# we wait until all the fights are done and press the ok button
# we press the scape key to go back to the main menu again

main()