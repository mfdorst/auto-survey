from selenium import webdriver

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

receiptNumber = ["611", "884", "000", "034", "115"]

driver = webdriver.Chrome("./resources/chromedriver")
driver.get("http://myopinion.deltaco.com/")
timeout = 5

def wait(type, id):
    try:
        element_present = EC.presence_of_element_located((type, id))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print "Timed out waiting for page to load"

def clickID(id):
    wait(By.ID, id)
    selection = driver.find_element_by_id(id)
    selection.click()

def clickClass(classname):
    wait(By.CLASS_NAME, classname)
    selection = driver.find_element_by_class_name(classname)
    selection.click()

def clickSelector(selector):
    wait(By.CSS_SELECTOR, selector)
    selection = driver.find_element_by_css_selector(selector)
    selection.click()

def clickSelectors(selectors):
    wait(By.CSS_SELECTOR, selectors[0])
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
                "div.option.option_522261_247027.last",
                "div.option.option_522251_247025.last"])

# wait for user to select '3'
# TODO: fix this

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
# wait for user to select "No Thanks, Continue"
# TODO: fix this

# page 15
clickID("option_525421_247666")

nextButton.click()

clickID("option_745653_340084")

nextButton.click()

