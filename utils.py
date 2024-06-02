import logging, sys

from time import sleep
from pyautogui import locateCenterOnScreen,locateOnScreen

def obtainCords(fileName, center = True, region = None):
    try:
        filePath = f"pics/{fileName}.png"
        confidence = 0.9
        return locateCenterOnScreen(filePath, confidence = confidence, region= region) if center else locateOnScreen(filePath, confidence=confidence, region=region)
        # logging.debug(region)
    except:
        logging.error(f"Cannot find the image {fileName}")
        sys.exit(1)

def obtainWaitCords(fileName, region):
    total = 0
    maxTotal = 960
    while(total < maxTotal):
        try:
            filePath = f"pics/{fileName}.png"
            confidence = 0.9
            return locateCenterOnScreen(filePath, confidence = confidence, region= region)
            # logging.debug(region)
        except:
            logging.error(f"Cannot find the image {fileName}")
            sleep(1)
            total = total+1
    logging.error("Cannot continue because it didn't find the required image")
    sys.exit()

def isInMenu(region):
        filePath = f"pics/menu.png"
        try:
            confidence = 0.9
            locateCenterOnScreen(filePath, confidence = confidence, region= region)
            return True
        except:
            return False

def isVisible(file, region):
        filePath = f"pics/{file}.png"
        try:
            confidence = 0.9
            locateCenterOnScreen(filePath, confidence = confidence, region= region)
            return True
        except:
            return False
