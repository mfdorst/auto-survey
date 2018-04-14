from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

receiptNumber = ["611", "884", "000", "034", "115"]

driver = webdriver.Chrome("./resources/chromedriver")
driver.get("http://myopinion.deltaco.com/")
timeout = 2

def wait(type, id):
    try:
        element_present = EC.presence_of_element_located((type, id))
        WebDriverWait(driver, timeout).until(element_present)
        return True
    except TimeoutException:
        print "Timed out waiting for page to load"
        return False

def clickID(id):
    if wait(By.ID, id):
        selection = driver.find_element_by_id(id)
        selection.click()

def clickIDs(ids):
    if wait(By.ID, ids[0]):
        for id in ids:
            selection = driver.find_element_by_id(id)
            selection.click()

def clickClass(classname):
    if wait(By.CLASS_NAME, classname):
        selection = driver.find_element_by_class_name(classname)
        selection.click()

def clickSelector(selector):
    if wait(By.CSS_SELECTOR, selector):
        selection = driver.find_element_by_css_selector(selector)
        selection.click()

def clickSelectors(selectors):
    if wait(By.CSS_SELECTOR, selectors[0]):
        for selector in selectors:
            selection = driver.find_element_by_css_selector(selector)
            selection.click()

# page 1

wait(By.ID, "promptInput_249796_0")

for i in range(0, 5):
    field = driver.find_element_by_id("promptInput_249796_{0}".format(i))
    field.send_keys(receiptNumber[i])

nextButton = driver.find_element_by_id("nextPageLink")
nextButton.click()

# page 2
clickID("option_628407_289359")

nextButton.click()

# page 3
clickID("option_522191_247003")

nextButton.click()

# page 4
clickID("option_522209_247008")

nextButton.click()

# page 5
clickSelectors(["div.option.option_522230_247015.last",
                "div.option.option_522235_247016.last",
                "div.option.option_522220_247013.last"])

nextButton.click()

# page 6
clickSelectors(["div.option.option_522246_247022.last",
                "div.option.option_522258_247026",
                "div.option.option_522261_247027.last",
                "div.option.option_522251_247025.last"])

nextButton.click()

# page 7
clickID("prompt_247033")

nextButton.click()

# page 8
clickID("option_522270_247036")

nextButton.click()

# page 9
clickID("prompt_305144")

nextButton.click()

# page 10
clickClass("option_772689_351323")

nextButton.click()

# page 11
clickID("prompt_351327")

nextButton.click()

# page 12
clickSelectors(["div.option.option_522349_247119.last",
                "div.option.option_522354_247120.last"])

nextButton.click()

# page 13
wait(By.ID, "commentArea")
selection = driver.find_element_by_id("commentArea")
selection.clear()
selection.send_keys("I like del taco very much" * 6)

nextButton.click()

# page 14
def find(driver):
    element = driver.find_element_by_xpath("//a[@ng-click='clickNoThanks()']")
    if element:
        return element
    else:
        return False

selection = WebDriverWait(driver, timeout).until(find)
selection.click()

# page 15
clickID("option_525421_247666")

nextButton.click()

clickID("option_745653_340084")

# if the demographics page comes up then the previous click will fail

clickIDs(["option_522363_247141",
        "option_522373_247142"])

nextButton.click()

clickID("option_745653_340084")

nextButton.click()
