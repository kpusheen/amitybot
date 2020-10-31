#THIS IS A SHIT WEBSITE. HAVE FUN.
#AMITY FEEDBACK FORM BOT
#Prashant Kumar 
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver  = webdriver.Chrome(ChromeDriverManager().install())

name= 'username'
password= 'password'
comment= '.........'

driver.get('https://www.amizone.net')
driver.find_element_by_name("_UserName").send_keys(name)
driver.find_element_by_name("_Password").send_keys(password)
driver.find_element_by_css_selector("button.login100-form-btn").click();
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div/div/div[1]/button").click()
time.sleep(2)
driver.find_element_by_css_selector("i.menu-icon.fa.fa-users").click()
time.sleep(2)
f=[2,3,4,5,6,7,8,9]

for m in f:
      driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li[{0}]/div[1]".format(m)).click()
      time.sleep(2)
      driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/div/ul/li[{0}]/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/a".format(m)).click()
      time.sleep(2)
      a=[1,2,3,4]
      for n in a:
          driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[1]/div[2]/div/div/table/tbody/tr[{0}]/td[5]/label/span".format(n)).click()
          time.sleep(0.1)
      a=[1,2,3,4,5,6,7]
      time.sleep(0.35)
      for n in a:
          driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[{0}]/td[5]/label/span".format(n)).click()
          time.sleep(0.1)
      a=[1,2,3,4,5,6]
      time.sleep(0.35)
      for n in a:
          driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[3]/div[2]/div/div/table/tbody/tr[{0}]/td[5]/label/span".format(n)).click()
          time.sleep(0.1)

      a=[1,2,3,4]
      time.sleep(0.35)
      for n in a:
          driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[4]/div[2]/div/div/table/tbody/tr[{0}]/td[5]/label/span".format(n)).click()
          time.sleep(0.1)

      time.sleep(0.35)
      for n in a:
          driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[5]/div[2]/div/div/table/tbody/tr[{0}]/td[5]/label/span".format(n)).click()
          time.sleep(0.1)

      a=[1,2,3]
      time.sleep(0.35)
      for n in a:
          driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[{0}]/td[3]/label/span".format(n)).click()
          time.sleep(0.1)
      driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[4]/td[2]/textarea").send_keys(comment)
      driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[7]/input").click();
      time.sleep(5)
      driver.find_element_by_xpath("/html/body/div[3]/a").click()
