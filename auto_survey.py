from selenium import webdriver
import time

driver = webdriver.Chrome("./resources/chromedriver")

driver.get("http://myopinion.deltaco.com/")

receiptNumber = ["611", "884", "000", "034", "115"]

wait_time = 1.5

# page 1
for i in range(0, 5):
    field = driver.find_element_by_id("promptInput_249796_{0}".format(i))
    field.send_keys(receiptNumber[i])


nextButton = driver.find_element_by_id("nextPageLink")
nextButton.click()
time.sleep(wait_time)

# page 2
selection = driver.find_element_by_id("option_628407_289359")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 3
selection = driver.find_element_by_id("option_522191_247003")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 4
selection = driver.find_element_by_id("option_522209_247008")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 5
selection = driver.find_element_by_css_selector("div.option.option_522230_247015.last")
selection.click()
selection = driver.find_element_by_css_selector("div.option.option_522235_247016.last")
selection.click()
selection = driver.find_element_by_css_selector("div.option.option_522220_247013.last")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 6
selection = driver.find_element_by_css_selector("div.option.option_522246_247022.last")
selection.click()
selection = driver.find_element_by_css_selector("div.option.option_522261_247027.last")
selection.click()
selection = driver.find_element_by_css_selector("div.option.option_522251_247025.last")
selection.click()

# wait for user to select '3'
time.sleep(3)

nextButton.click()
time.sleep(wait_time)

# page 7
selection = driver.find_element_by_id("prompt_247033")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 8
selection = driver.find_element_by_id("option_522270_247036")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 9
selection = driver.find_element_by_id("prompt_305144")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 10
selection = driver.find_element_by_class_name("option_772689_351323")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 11
selection = driver.find_element_by_id("prompt_351327")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 12
selection = driver.find_element_by_css_selector("div.option.option_522349_247119.last")
selection.click()
selection = driver.find_element_by_css_selector("div.option.option_522354_247120.last")
selection.click()

nextButton.click()
time.sleep(wait_time)

# page 13
selection = driver.find_element_by_id("commentArea")
selection.clear()
selection.send_keys("I like del taco very much" * 6)

nextButton.click()
time.sleep(wait_time)

time.sleep(4)

driver.quit()
