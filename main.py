from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date
import sys
import time

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
time.sleep(3)                                                                                                         
driver.find_element_by_tag_name('body').screenshot('lastfm_'+date.today().strftime("%Y %m %d") +'.png')


driver.quit()