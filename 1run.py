import pyautogui as pui
import pygetwindow as gw
import logging, os, sys, time

# logging info will be shown with time of happening
logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

def one_Run():
    getGameWindow()
    while True:
        startLazyClear()
    # time.sleep(8)
    # for i in range(0, 3):
    #     checkRewards()
    #     time.sleep(1)
    # checkLvlUp()
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

def startLazyClear():
    """One Run when Story is already selected."""
    logging.info('Looking for Accept Udon Overflow Button.')
    while True: # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('menu_1.png'), confidence=0.9)
        if pos is not None:
            logging.info('Accept Udon Overflow Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Unread/Uncleared Story.')

    logging.info('Looking for Next Button')
    while True: # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('menu_2.png'), confidence=0.9)
        if pos is not None:
            logging.info('Next Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Next Button.')

    logging.info('Looking for Support Player Button')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('menu_3.png'), confidence=0.9)
        if pos is not None:
            logging.info('Support Player Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Support Player Button.')

    logging.info('Looking for Sortie Button')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('menu_4.png'), confidence=0.9)
        if pos is not None:
            logging.info('Sortie Button located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Sortie Button.')

    # logging.info('Looking for Start Button')
    # while True:  # loop because it could still be in loading screen
    #     pos = pui.locateCenterOnScreen(imgPath('menu_5_1.png'), confidence=0.9)
    #     if pos is not None:
    #         logging.info('Start Button located at: %s', pos)
    #         break
    # pui.click(pos, duration=0.25)
    # logging.info('Clicked on Start Button.')

    logging.info('Looking for Winning Screen')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('win_screen_6.png'), confidence=0.9)
        if pos is not None:
            logging.info('Winning Icon located at: %s', pos)
            break
    pui.click(pos, clicks=2, duration=0.25)
    time.sleep(1)
    pui.click(pos, clicks=5, duration=0.25)
    time.sleep(1)
    pui.click(pos, clicks=5, duration=0.25)
    logging.info('Clicked on Winning Screen.')

    logging.info('Looking for End Screen')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('end_screen_7_1.png'), confidence=0.9)
        if pos is not None:
            logging.info('End Icon located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on End Screen.')

def checkRewards():
    logging.info('Looking for Chapter Rewards')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('chapter_clear_bonus.png'), confidence=0.9)
        if pos is not None:
            logging.info('Reward Button located at: %s', pos)
            break
        if pos is None:
            return
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Rewards Button.')

def checkLvlUp():
    logging.info('Looking for Level Up Screen')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('card_level_up.png'), confidence=0.9)
        if pos is not None:
            logging.info('Level Up Icon located at: %s', pos)
            break
        if pos is None:
            return
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Level Up Screen.')

if __name__ == '__main__':
    one_Run()