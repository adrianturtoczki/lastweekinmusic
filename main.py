from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

user_name = sys.argv[1]

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'https://www.last.fm/user/'+user_name+'/listening-report/week'

driver.get(URL)

button = driver.find_element_by_id('onetrust-accept-btn-handler')
button.click()

S = lambda l: driver.execute_script('return document.body.parentNode.scroll'+l)
driver.set_window_size(S('Width'),S('Height'))                                                                                                          
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')


driver.quit()