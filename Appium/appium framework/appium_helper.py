from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def waitForElement(driver, method, locator, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((method, locator)))
        sleep(1)
        return True

    except Exception as ex:
        return False


def getElementWithoutWait(driver, method, locator):
    try:
        if (method == By.ID):
            element = driver.find_element_by_id(locator)
        else:
            element = driver.find_element_by_xpath(locator)
        return element

    except Exception as ex:
        return None


def getElement(driver, method, locator, timeout):
    try:
        if (not waitForElement(driver, method, locator, timeout)):
            return None

        return getElementWithoutWait(driver, method, locator)

    except Exception as ex:
        return None


def waitForElementToDisappear(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        for second in range(timeout):
            if (not element.is_displayed()):
                return True
            sleep(1)
            print('waiting for it to disappear..')

        return False

    except Exception as ex:
        return False


def waitForElementToContainSomeText(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        for second in range(timeout):
            if (element.text != ''):
                return True
            sleep(1)
            print('waiting for it to contain some text..')

    except Exception as ex:
        return False


def click(element):
    element.click()
    sleep(1)


def clickElement(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        click(element)
        return True

    except Exception as ex:
        return False


def clickElementAndWaitContentChanged(driver, method, locator, content, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        content = getElement(driver, method, content, timeout)
        if (content == None):
            return False

        originalText = content.text
        click(element)

        for second in range(timeout):
            if (content.text != originalText):
                return True
            sleep(1)
            print('waiting for content changed..')

        return False

    except Exception as ex:
        return False


def setTextForElement(driver, method, locator, timeout, text):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        element.set_text(text)

        for second in range(timeout):
            if (element.text == text):
                return True
            sleep(1)
            print('waiting for text to take effect..')

        return False

    except Exception as ex:
        return False


def setPasswordForElement(driver, method, locator, timeout, password):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        element.set_text(password)
        sleep(2)
        return True

    except Exception as ex:
        return False


def uncheckElement(driver, method, locator, timeout):
    try:
        element = getElement(driver, method, locator, timeout)
        if (element == None):
            return False

        if (element.is_selected()):
            click(element)

        return True

    except Exception as ex:
        return False


def swipeUp(driver, method, locator, timeout):
    try:
        container = getElement(driver, method, locator, timeout)
        if (container == None):
            return False

        x = container.location['x'] + (container.size['width'] / 2)
        y1 = container.location['y'] + container.size['height'] - 10
        y2 = container.location['y'] + 10
        driver.swipe(x, y1, x, y2)
        sleep(2)

        return True

    except Exception as ex:
        return False
