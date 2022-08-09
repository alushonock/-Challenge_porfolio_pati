import os
import sys

from selenium.webdriver.common.by import By

SYSTEM = sys.platform
PATH_TO_PROJECT = os.path.dirname(os.path.abspath(__file__))

if SYSTEM == 'mac64':
    CHROME_DRIVER = "chromedriver-2"
else:
    CHROME_DRIVER = "chromedriver-3"

DRIVER_PATH = os.path.join(/Users/alina/Documents/GitHub/-Challenge_porfolio_pati/drivers/chromedriver-2)
IMPLICITLY_WAIT = 3
EXPLICITLY_WAIT = 30

DEFAULT_LOCATOR_TYPE = By.XPATH


UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

if SYSTEM == ' == 'macOS':
    CHROME_DRIVER = 'chromedriver-2'
    FIREFOX_DRIVER = 'geckodriver-2'
    EDGE_DRIVER = 'MicrosoftWebDriver.exe'
else:
    CHROME_DRIVER = 'chromedriver'
    FIREFOX_DRIVER = 'geckodriver'
    EDGE_DRIVER = 'MicrosoftWebDriver.exe'
