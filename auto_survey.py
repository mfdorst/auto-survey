from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

receiptNumber = ["611", "884", "000", "034", "115"]

driver = webdriver.Chrome("./resources/chromedriver")
driver.get("http://myopinion.deltaco.com/")
timeout = 3

def actionBy(method, selector, action):
    def find(driver):
        # find the method on driver which deals with this kind of selector
        # i.e. driver.find_element_by_class_name
        find_method = getattr(driver, "find_element_by_{0}".format(method))
        element = find_method(selector)
        return element if element else False

    try:
        # keep calling find until either it returns a result, or the timeout period ends
        element = WebDriverWait(driver, timeout).until(find)
        action(element)
    except TimeoutException:
        pass

def clickBy(method, selector):
    def click(element):
        element.click()

    actionBy(method, selector, click)


# page 1
for i in range(0, 5):
    def typeReceiptNumber(field):
        field.send_keys(receiptNumber[i])
    actionBy('id', "promptInput_249796_{0}".format(i), typeReceiptNumber)

nextButton = driver.find_element_by_id("nextPageLink")
nextButton.click()

# page 2
clickBy('id', "option_628407_289359")

nextButton.click()

# page 3
clickBy('id', "option_522191_247003")

nextButton.click()

# page 4
clickBy('id', "option_522209_247008")

nextButton.click()
# page 5
clickBy('css_selector', "div.option.option_522230_247015.last")
clickBy('css_selector', "div.option.option_522235_247016.last")
clickBy('css_selector', "div.option.option_522220_247013.last")

nextButton.click()

# page 6
clickBy('css_selector', "div.option.option_522246_247022.last")
clickBy('css_selector', "div.option.option_522258_247026")
clickBy('css_selector', "div.option.option_522261_247027.last")
clickBy('css_selector', "div.option.option_522251_247025.last")

nextButton.click()

# page 7
clickBy('id', "prompt_247033")

nextButton.click()

# page 8
clickBy('id', "option_522270_247036")

nextButton.click()

# page 9
clickBy('id', "prompt_305144")

nextButton.click()

# page 10
clickBy('class_name', "option_772689_351323")

nextButton.click()

# page 11
clickBy('id', "prompt_351327")

nextButton.click()

# page 12
clickBy('css_selector', "div.option.option_522349_247119.last")
clickBy('css_selector', "div.option.option_522354_247120.last")

nextButton.click()

# page 13
def typeStuff(element):
    element.clear()
    element.send_keys("I like del taco very much" * 6)

actionBy('id', "commentArea", typeStuff)

nextButton.click()

# page 14
clickBy('xpath', "//a[@ng-click='clickNoThanks()']")

# page 15
clickBy('id', "option_525421_247666")

nextButton.click()

# page 16
clickBy('id', "option_745653_340084")

nextButton.click()

# if the demographics page comes up then the previous click will fail

clickBy('id', "option_522363_247141")
clickBy('id', "option_522373_247142")

nextButton.click()

# we have to repeat this click, which was attempted before
# this time it will succeed
clickBy('id', "option_745653_340084")

nextButton.click()

# TODO: grab the validation code and close the browser
