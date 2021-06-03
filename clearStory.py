import pyautogui as pui
import random as rdm
import pygetwindow as gw
import copy, logging, os, sys, time
from threading import Timer

# logging info will be shown with time of happening
logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.info) # uncomment to block debug log messages


unread_story = None
# regions of the 5 stages available
# sadly need to be adjusted manually, use pyautogui.displayMousePosition() in Python to check positions
r1 = (1140, 340, 150, 200)
r2 = (1280, 475, 150, 200)
r3 = (1360, 340, 150, 200)
r4 = (1430, 500, 150, 200)
r5 = (1550, 340, 150, 200)
lr = (r1, r2, r3, r4, r5)

delay = 10

def main():
    """Runs the entire program. Nox will be selected and start the Bot."""
    logging.info('Program started. Press Ctrl+C to abort any time.')
    logging.info('To interrupt mouse movement, move mouse to upper left corner.')
    getGameWindow()
    # while True:
    for i in range(0, 5):
        startClearing(lr[i])
        time.sleep(10)
    # sys.exit() # may terminate python
    quit()


def imgPath(filename):
    """A shortcut for joining the 'images/' file path, since it's used often. Returns the filename with 'images/' prepanded."""
    return os.path.join('Images', filename)

def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if somepredicate(*args, **kwargs): return True
    time.sleep(period)
  return False

def getGameWindow():
    """Opens Nox Yuyuyui Game Window."""
    noxWindow = gw.getWindowsWithTitle('YuYuYui')[0]  # returns <Win32Window left="2178", top="259", width="988", height="590", title="YuYuYui">
    logging.info(noxWindow)
    noxWindow.activate()
    logging.info('Window selected.')

def startClearing(r):
    """The main game playing function. This functions handles all menus to navigate through."""
    curr_r = r
    logging.info('Looking for Unread Story...')
    while True: # loop because it could still be in loading screen
        pos = None
        global unread_story
        if pos is None:
            pos = pui.locateCenterOnScreen(imgPath('story_unread_0.png'), region=r, confidence=0.85)
            unread_story = True
        if pos is None:
            pos = pui.locateCenterOnScreen(imgPath('story_unclear_0.png'), region=r, confidence=0.9)
            unread_story = None
        if pos is None:
            pos = pui.locateCenterOnScreen(imgPath('boss_unclear_0.png'), region=r, confidence=0.85)
            unread_story = None
        # if pos is None: # this is totally broken fuck
        #     if curr_r != r:
        #         start_time = Timer(delay, skip_region(r))
        #         start_time.start()
        if pos is None:
            logging.info('Could not find Story at:' + str(r))
            return

        if pos is not None:
            logging.info('Unclear story located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Unread/Uncleared Story.')

    if unread_story:
        read_Story()
        return logging.info('Story was read.')

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
    #     pos = pui.locateCenterOnScreen(imgPath('menu_5.png'), confidence=0.9)
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
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Winning Screen.')

    logging.info('Looking for End Screen')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('end_screen_7_1.png'), confidence=0.9)
        if pos is not None:
            logging.info('End Icon located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on End Screen.')

def read_Story():
    logging.info('Looking for Skip Story Button')
    while True:  # loop because it could still be in loading screen
        pos = pui.locateCenterOnScreen(imgPath('menu_1_1.png'), confidence=0.9)
        if pos is not None:
            logging.info('End Icon located at: %s', pos)
            break
    pui.click(pos, duration=0.25)
    logging.info('Clicked on Winning Screen.')
    global unread_story
    unread_story = None

def skip_region(r):
    return

if __name__ == '__main__':
    main()