from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

receiptNumber = ["301", "084", "000", "064", "113"]

options = Options()
# options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome("./resources/chromedriver", chrome_options=options)
options.add_argument('headless')
driver.get("http://myopinion.deltaco.com/")
timeout = 5

def actionBy(method, selector, action):
    def find(driver):
        # find the method on driver which deals with this kind of selector
        # i.e. driver.find_element_by_class_name
        find_method = getattr(driver, "find_element_by_{0}".format(method))
        element = find_method(selector)
        return element if element else False

    try:
        element = WebDriverWait(driver, timeout).until(find)
        action(element)
    except TimeoutException:
        pass

def clickBy(method, selector):
    actionBy(method, selector, lambda e: e.click())

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

def whichID(id1, id2):
    def find(driver):
        if driver.find_element_by_id(id1):
            return id1
        if driver.find_element_by_id(id2):
            return id2
        # if neither id is found
        return False

    try:
        # keep calling find until either it returns a result, or the timeout period ends
        print 'waiting'
        id = WebDriverWait(driver, timeout).until(find)
        print 'done waiting'
        return id
    except TimeoutException:
        print 'timeout exception'
        return False

id = whichID("option_745653_340084", "option_522363_247141")

if (id == "option_745653_340084"):
    # final page
    clickBy('id', "option_745653_340084")
else:
    # demographics page
    clickBy('id', "option_522363_247141")
    clickBy('id', "option_522373_247142")
    nextButton.click()
    #final page
    clickBy('id', "option_745653_340084")

nextButton.click()

# TODO: grab the validation code and close the browser
