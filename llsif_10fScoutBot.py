import pyautogui as pui
import pygetwindow as gw
import logging, os, sys, time

# logging info will be shown with time of happening
logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

# location of NoxWindowCenter
noxCenter = []

def auto_friendGacha():
    getGameWindow()
    getWindowCenter()
    # pull_friendGacha()
    while True:
        scoutAgain()
    sys.exit()

def imgPath(filename):
    """A shortcut for joining the 'images/' file path, since it's used often. Returns the filename with 'images/' prepanded."""
    return os.path.join('Images', filename)

def getGameWindow():
    """Opens Nox Yuyuyui Game Window."""
    noxWindow = gw.getWindowsWithTitle('YuYuYui')[0]  # returns <Win32Window left="2178", top="259", width="988", height="590", title="YuYuYui">
    logging.info(noxWindow)
    noxWindow.activate()
    logging.info('Window selected.')

def getWindowCenter():
    noxWindow = gw.getWindowsWithTitle('YuYuYui')[0]

    noxCenterX = noxWindow.bottomright[0] - noxWindow.topleft[0]
    noxCenterY = noxWindow.bottomright[1] - noxWindow.topleft[1]
    noxCenter.append(noxCenterX)
    noxCenter.append(noxCenterY)

    logging.info('Nox Center located at: %s', noxCenter)

def pull_friendGacha():
    """Pull Friend Gacha."""
    logging.info('Looking for 10-Pull Button.')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('dino_10scout.png'), confidence=0.9)
        if pos is not None:
            logging.info('10-Pull Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on 10-Pull Friend Gacha.')

    logging.info('Looking for OK1 Button.')
    while True:
        pos = pui.locateCenterOnScreen(imgPath('dino_ok1.png'), confidence=0.9)
        if pos is not None:
            logging.info('OK1 Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on OK1 Button.')

    logging.info('Looking for OK2 Button.')
    while True:
        pos = pui.locateCenterOnScreen(imgPath('dino_ok2.png'), confidence=0.9)
        if pos is not None:
            logging.info('OK2 Button located at: %s', pos)
            break
        if pos is None:
            pui.click(noxCenter, clicks=2, duration=0.25)
    pui.click(pos, duration=0.25)
    logging.info('Clicked on OK2 Button.')

def scoutAgain():
    """Scout Friend Gacha again. Needs to be looped."""
    logging.info('Looking for Scout Again Button.')
    while True:
        pos = pui.locateCenterOnScreen(imgPath('dino_scoutAgain.png'), confidence=0.9)
        if pos is not None:
            logging.info('Scout Again Button located at: %s', pos)
            break
        # if pos is None:
        #     pui.click(noxCenter, clicks=2, duration=0.25)
    pui.click(pos, duration=0.25)
    logging.info('Clicked Scout Again Button.')

    logging.info('Looking OK1 Button.')
    while True:
        pos = pui.locateCenterOnScreen(imgPath('dino_ok1_1.png'), confidence=0.9)
        if pos is not None:
            logging.info('OK1 Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked OK1 Button.')

    logging.info('Looking OK2 Button.')
    while True:
        pos = pui.locateCenterOnScreen(imgPath('dino_ok2.png'), confidence=0.9)
        if pos is not None:
            logging.info('OK1 Button located at: %s', pos)
            break
        if pos is None:
            pui.click(noxCenter, clicks=2, duration=0.25)
    pui.click(pos, duration=0.25)
    logging.info('Clicked OK2 Button.')

if __name__ == '__main__':
    auto_friendGacha()

