from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By # deprecation warning removed


driver = webdriver.Chrome("/home/arvydas/Desktop/chromedriver")
driver.maximize_window()

def obelsdumas():

    driver.get("https://obelsdumas.lt/")
    print("I'm in obelsdumas.lt")
    time.sleep(2)
    print("Scroll To Bottom in 3")
    time.sleep(3)

    #scroll bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Click on Prekiu grazinimas in 3")
    time.sleep(3)

    # click prekiu grazinimas
    driver.find_element(By.LINK_TEXT, "Prekių grąžinimas").click()
    print("click on rukyti mesos gaminiai in 3")
    time.sleep(3)

    driver.find_element(By.LINK_TEXT, "Rūkyti mėsos gaminiai").click()
    print("Click on a product in 3")
    time.sleep(3)
    
    driver.find_element(By.XPATH,'//*[@id="content"]/div/div/section[2]/div/div/div/div[2]/div/div/ul/li[3]/a[3]').click()
    time.sleep(3)

obelsdumas()
print("obelsdumas done")
driver.close()
