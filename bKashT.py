#import xl
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import  Keys

driver: WebDriver = webdriver.Chrome(executable_path="C:\selenium browser drivers\chromedriver.exe")

driver.maximize_window()

driver.get("http://172.16.229.132:9083/login.html#!")

driver.save_screenshot("C:\screenshoot auto\T.B\home.png")









#driver.get_screenshot_as_file("filename")

#sign in

time.sleep(1)
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div/div[2]/div[2]/input").send_keys("mahtab")

time.sleep(1)
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div[2]/input").send_keys("123456")

driver.save_screenshot("C:\screenshoot auto\T.B\h1.png")

time.sleep(1)
driver.find_element_by_xpath("/html/body/section/div/div/div[2]/form/div/div[4]/div/input[2]").click()

driver.save_screenshot("C:\screenshoot auto\T.B\h2.png")

#dashboard

time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/nav/div/div/ul/li[5]/a").click()
driver.save_screenshot("C:\screenshoot auto\T.B\h3.png")

time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/div/div[1]/div/a").click()
driver.save_screenshot("C:\screenshoot auto\T.B\h4.png")


time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/section/div/div/div/div/div/div/div/select").click()
driver.save_screenshot("C:\screenshoot auto\T.B\h5.png")


time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/section/div/div/div/div/div/div/div/select/option[5]").click()
driver.save_screenshot("C:\screenshoot auto\T.B\h6.png")


time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/section/div/div/div/div/div/div/form/div[1]/input").send_keys("wyjtub")

time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/section/div/div/div/div/div/div/form/div[2]/div[1]/input[4]").send_keys("01755575455")
driver.save_screenshot("C:\screenshoot auto\T.B\h7.png")


time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/section/div/div/div/div/div/div/form/div[6]/button").send_keys(Keys.ENTER)
driver.save_screenshot("C:\screenshoot auto\T.B\h8.png")


time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/section/div/div/div/div/div/div/form/div[2]/button[2]").click()
driver.save_screenshot("C:\screenshoot auto\T.B\h9.png")


time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/section/div/div/div/div/div[2]/form/div[1]/input").send_keys("4534")
driver.save_screenshot("C:\screenshoot auto\T.B\h10.png")



time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/section/div/div/div/div/div[2]/form/div[2]/button").click()
driver.save_screenshot("C:\screenshoot auto\T.B\h11.png")




time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/section/div/section/div/div/div/div/div/div/div[4]/a").click()
driver.save_screenshot("C:\screenshoot auto\T.B\h12.png")












