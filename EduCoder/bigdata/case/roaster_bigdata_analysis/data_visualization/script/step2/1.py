from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
# options.headless = True
driver = webdriver.Firefox(executable_path=r'/opt/geckodriver')
driver.get("http://127.0.0.1:8080/factors_affecting_quality")
time.sleep(3)
driver.find_element_by_id('main').screenshot('/data/workspace/myshixun/secret/step2/result/factors_affecting_quality.png')
driver.close()