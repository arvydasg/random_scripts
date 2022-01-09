from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By # deprecation warning removed


driver = webdriver.Chrome("/home/arvydas/Desktop/chromedriver")
driver.maximize_window()

def dailyspoon_form():

    driver.get("https://dailyspoon.lt/")
    print("I'm in")

    driver.find_element(By.XPATH,'//*[@id="menu-item-159"]/a').click()
    
    driver.find_element(By.ID,"menu-item-7187").click()

    driver.find_element(By.XPATH,'//*[@id="et-boc"]/div/div/div[1]/div[3]/div/div/a').click()

    driver.find_element(By.ID,"lytis3").click()

    driver.find_element(By.ID,"odos-tipas2").click()
    time.sleep(2)
    print("Scroll in 3...")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("scroll 800px!")
    time.sleep(2)

    # scroll
    driver.execute_script("window.scrollBy(0,800)");
    time.sleep(2)

    driver.find_element(By.NAME, "daznas-maistas1").click()

    driver.find_element(By.NAME, "daznas-maistas2").click()

    driver.find_element(By.NAME, "daznas-maistas3").click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,800)");
    time.sleep(2)

    driver.find_element(By.NAME,"retas-maistas2").click()

    driver.find_element(By.NAME,"retas-maistas3").click()

    driver.find_element(By.NAME,"retas-maistas4").click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,800)");
    time.sleep(2)

    driver.find_element(By.NAME,"problema11").click()

    driver.find_element(By.NAME,"problema10").click()

    driver.find_element(By.NAME,"problema9").click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,400)");
    time.sleep(2)

    driver.find_element(By.ID,"sportas1").click()

    driver.find_element(By.ID,"m-sportas2").click()

    driver.execute_script("window.scrollBy(0,800)");
    time.sleep(2)

    driver.find_element(By.ID,"stresas1").click()

    driver.find_element(By.ID,"liga1").click()

    driver.execute_script("window.scrollBy(0,500)");
    time.sleep(2)

    driver.find_element(By.NAME,"rezultatas1").click()

    driver.find_element(By.NAME,"rezultatas2").click()

    driver.find_element(By.NAME,"rezultatas3").click()

    driver.find_element(By.NAME,"rezultatas6").click()
    time.sleep(2)

    driver.execute_script("window.scrollBy(0,100)");
    time.sleep(2)

    driver.find_element(By.NAME,"submit").click()
    time.sleep(2)

    elem = driver.find_element(By.NAME, "email")
    elem.send_keys("antanas@gmail.com")
    time.sleep(2)
    elem.send_keys(Keys.RETURN)
    
x = range(2)
for n in x:
    dailyspoon_form()
    print("klausimynas done")
    
# close 
driver.close()
