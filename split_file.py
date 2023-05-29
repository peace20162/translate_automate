from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


# input novel path and chromedriver path
chromedriver_path= r"C:\Users\peace\Desktop\Translate automate\chromedriver_win32"
novel_file= r"D:\นิยาย\Hour of sage\현자의 시간 1-419 (完).txt"

# calculate number of splitted file 
# chapters/50 = number of files
num_chaps = 419

if num_chaps % 50 == 0 :
	num_files= num_chaps//50
else:
	num_files= (num_chaps//50)+1



website = "https://textfilesplitter.com/"



service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# send number of splitted file to website
num_file_container = driver.find_element(by="xpath",value='//input[@id="numbertext"]')
num_file_container.click()
num_file_container.clear()
num_file_container.send_keys(num_files)

# select UTF-8 encoding and line split
utf8_box = driver.find_element(by="xpath",value='//input[@id="utf8"]')
utf8_box.click()


# Upload file
upload_container = driver.find_element(by="xpath",value='//input[@id="file"]')
upload_container.send_keys(novel_file)


# Click split file button
split_box = driver.find_element(by="xpath",value='//div[@id="splitfile"]')
split_box.click()

time.sleep(30)
driver.quit()