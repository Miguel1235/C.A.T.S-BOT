import logging, sys
import cv2
import pytesseract

from time import sleep
from pyautogui import locateCenterOnScreen,locateOnScreen

def obtainCords(fileName, center = True, region = None):
    try:
        filePath = f"pics/{fileName}.png"
        confidence = 0.9
        return locateCenterOnScreen(filePath, confidence = confidence, region= region) if center else locateOnScreen(filePath, confidence=confidence, region=region)
        # logging.debug(region)
    except:
        logging.error(f"Cannot find the image {fileName}, is it running and is it visible??")
        sys.exit(1)

def obtainWaitCords(fileName, region):
    total = 0
    maxTotal = 40
    while(total < maxTotal):
        try:
            filePath = f"pics/{fileName}.png"
            confidence = 0.9
            return locateCenterOnScreen(filePath, confidence = confidence, region= region)
            # logging.debug(region)
        except:
            logging.error(f"Cannot find the image {fileName}, is it running and is it visible??")
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

def img2Text(input_path):
   img = cv2.imread(input_path)
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   text = pytesseract.image_to_string(img)
   print(text)

   return text.strip()