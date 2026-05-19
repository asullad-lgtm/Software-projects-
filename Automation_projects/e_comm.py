from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login")
wait = WebDriverWait(driver,10)
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR,"button.radius").click()
message = wait.until(EC.presence_of_element_located((By.ID,"flash"))).text
print('Login result',message)
driver.quit()