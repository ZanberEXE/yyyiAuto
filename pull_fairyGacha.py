import pyautogui as pui
import pygetwindow as gw
import copy, logging, os, sys, time

# logging info will be shown with time of happening
logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

# location of NoxWindowCenter
noxCenter = []

def auto_fairyGacha():
    getGameWindow()
    getWindowCenter()
    while True:
        pull_fairyGacha()
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

def pull_fairyGacha():
    """Continuosly pull fairy gacha."""
    logging.info('Looking for 10-Pull Button.')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('fairygacha_10roll.png'), confidence=0.9)
        if pos is not None:
            logging.info('10-Pull Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on 10-Pull Fairy Gacha.')

    logging.info('Looking for Accept Button.')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('fairygacha_yes.png'), confidence=0.9)
        if pos is not None:
            logging.info('Accept Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Accept Fairy Gacha.')

    logging.info('Looking for OK Button.')
    while True:  # loop because it could still be in loading screen
        time.sleep(3) # loop will be played every 2s giving enough time for animations so they can be clicked away
        pos = pui.locateCenterOnScreen(imgPath('fairygacha_ok.png'), confidence=0.9)
        if pos is not None:
            logging.info('OK Button located at: %s', pos)
            break
        if pos is None:
            pui.click(noxCenter, clicks=2, duration=0.25)
    pui.click(pos, duration=0.25)
    logging.info('10-Pull Clear.')

def getWindowCenter():
    noxWindow = gw.getWindowsWithTitle('YuYuYui')[0]

    noxCenterX = noxWindow.topleft[0] + (noxWindow.bottomright[0] / 2) + 41.5
    noxCenterY = noxWindow.topleft[1] + (noxWindow.bottomright[1] / 2)
    noxCenter.append(noxCenterX)
    noxCenter.append(noxCenterY)

    logging.info('Nox Center located at: %s', noxCenter)
    # print("Nox Center is: " + str(noxCenter))

if __name__ == '__main__':
    auto_fairyGacha()