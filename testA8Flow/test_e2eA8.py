import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C://Users//Venkateshwaranlu//Documents//chromedriver.exe")
driver.get("https://dev-flow.autonom8.com/#/signin")
driver.maximize_window()
driver.find_element(By.ID, 'username').send_keys("superAdmin")
driver.find_element(By.ID, "password").send_keys("a8Passw0rd!")
driver.find_element(By.ID,"loginBtn").click()
# time.sleep(5)
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card-grid-assignee")))

cards = driver.find_elements(By.XPATH,"//div[@class='card-grid-footer']")

for card in cards:
    CardName = card.find_element(By.XPATH, "div/div/span[2]").text
    print(CardName)
    if CardName == "DemoHideShow":
        card.find_element(By.XPATH, "div/div/span[2]").click()


driver.switch_to.frame("iframe")
CardNames = driver.find_elements(By.XPATH,'//div[@class="sections_sectionheader__2RYkq"]')


for CardName in CardNames:
    FindCardName = CardName.find_element(By.XPATH,'div').text
    print(FindCardName)
    if FindCardName == "section1":
        CardName.find_element(By.XPATH,'div').click()

