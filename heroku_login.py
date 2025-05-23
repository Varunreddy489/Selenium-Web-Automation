import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=r"C:\Users\varun\OneDrive\Desktop\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

input_element = driver.find_element(By.ID, "username")
input_element.clear()
input_element.send_keys("tomsmith")

input_element = driver.find_element(By.ID, "password")
input_element.clear()
input_element.send_keys("SuperSecretPassword!")

button_element = driver.find_element(By.CLASS_NAME, "radius")
button_element.click()

time.sleep(1000)
driver.quit()
