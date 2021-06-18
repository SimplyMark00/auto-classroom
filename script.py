from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/marco/chromedriver"
driver = webdriver.Chrome(PATH)

username = 'your username'
password = 'your password'

driver.get("https://classroom.google.com/u/0/h")

driver.find_element_by_id("identifierId").send_keys(username)

driver.find_element_by_class_name("VfPpkd-vQzf8d").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']" ))).send_keys(password)

driver.find_element_by_class_name("VfPpkd-vQzf8d").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='onkcGd kj3hr YVvGBb']"))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='dbEQNc']//div[@class='QRiHXd']//div[1]"))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Partecipa')]"))).click  # text 'Partecipa' must be modified based on your language
