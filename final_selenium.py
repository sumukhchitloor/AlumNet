import time
#import element as element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import string
import random

service = Service(executable_path="/snap/bin/chromium.chromedriver")
options = webdriver.ChromeOptions()
options.headless = True

driver=webdriver.Chrome(service=service, options=options)



# serv_obj=Service("C:\Drivers\chromedriver_win32/chromedriver")
# driver = webdriver.Chrome(service=serv_obj)
driver.get("http://localhost/alumni")
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//*[@id='login']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='new_account']").click()
time.sleep(1)

def generate_random_name():
  names = ['Vyas', 'Lad', 'Chitloor', 'Parida', 'Fadill', 'Maniyar', 'Khan', 'Maguire']
  return random.choice(names)

n= generate_random_name()

driver.find_element(By.XPATH,"//*[@id='create_account']/div[1]/div[1]/input").send_keys(n)
time.sleep(1)
def generate_random_name():
  names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank', 'Gary', 'Helen']
  return random.choice(names)

m= generate_random_name()

driver.find_element(By.XPATH,"//*[@id='create_account']/div[1]/div[2]/input").send_keys(m)
time.sleep(1)
def generate_random_name():
  names = ['zubair', 'gagan', 'hashira', 'durant', 'lebron', 'eminem', 'lionel', 'andrew']
  return random.choice(names)

k= generate_random_name()
driver.find_element(By.XPATH,"//*[@id='create_account']/div[1]/div[3]/input").send_keys(k)
time.sleep(1)


ele = driver.find_element(By.XPATH,"//*[@id='create_account']/div[2]/div[1]/select")
drp = Select(ele)
drp.select_by_visible_text("Female")
time.sleep(1)


ab = driver.find_element(By.XPATH,"//*[@id='create_account']/div[2]/div[2]/input")
driver.execute_script("arguments[0].value = '2022';", ab)
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='create_account']/div[2]/div[3]/span/span[1]/span/span[2]").click()
driver.find_element(By.XPATH,"//*[@id='page-top']/span/span/span[1]/input").send_keys("BE Aeronautical Engineering")
driver.find_element(By.XPATH,"//*[@id='page-top']/span/span/span[1]/input").send_keys(Keys.RETURN)
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='create_account']/div[3]/div[1]/textarea").send_keys("Promac")
time.sleep(1)
def generate_random_email():
  # Generate a random string of length 10
  random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
  # Return the email address
  return f"{random_string}@gmail.com"

# Generate a random email address
email = generate_random_email()
driver.find_element(By.XPATH,"//*[@id='create_account']/div[4]/div[1]/input").send_keys(email)
time.sleep(1)

def generate_password(length):
  # Get a random selection of characters from the set of lowercase letters, uppercase letters, and digits
  characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
  password = ''.join(random.choices(characters, k=length))
  return password

password = generate_password(16)

driver.find_element(By.XPATH,"//*[@id='create_account']/div[4]/div[2]/input").send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='create_account']/div[6]/div/button").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='login']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='login-frm']/div[1]/input").send_keys("varuns@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='login-frm']/div[2]/input").send_keys("varun")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='login-frm']/button").click()
time.sleep(1)


pixels = 200
driver.execute_script("window.scrollBy(0, arguments[0])", pixels)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='page-top']/div[2]/div[1]/div[2]/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[1]/a").click()
time.sleep(2)
pixels = 700
driver.execute_script("window.scrollBy(0, arguments[0])", pixels)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='page-top']/div[2]/div[2]/div[2]/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[1]/a").click()
time.sleep(2)
pixels = 1100
driver.execute_script("window.scrollBy(0, arguments[0])", pixels)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='page-top']/div[2]/div[3]/div[2]/div/div/button").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[1]/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[2]/a").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='filter']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='filter']").send_keys("Rujuta")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='search']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[3]/a").click()
time.sleep(2)
pixels = 1600
driver.execute_script("window.scrollBy(0, arguments[0])", pixels)
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[4]/a").click()
time.sleep(1)


driver.find_element(By.XPATH,"//*[@id='filter']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='filter']").send_keys("Data Analyst")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='search']").click()
time.sleep(2)
pixels = 300
driver.execute_script("window.scrollBy(0, arguments[0])", pixels)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[4]/a").click()
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='new_career']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-career']/div[1]/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-career']/div[1]/div/input").send_keys("Google")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-career']/div[2]/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-career']/div[2]/div/input").send_keys("Web Developer")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-career']/div[3]/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-career']/div[3]/div/input").send_keys("Bangalore")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-career']/div[4]/div/div/div[3]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-career']/div[4]/div/div/div[3]").send_keys("A Web Developer is responsible for the design, development, and maintenance of websites and web applications. They work with a variety of programming languages and frameworks to create functional and visually appealing sites that meet the needs of clients.")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='submit']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[5]/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='filter']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='filter']").send_keys("Welcome To The Computer Forum")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='search']").click()
time.sleep(3)
pixels = 100
driver.execute_script("window.scrollBy(0, arguments[0])", pixels)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='page-top']/div[2]/div[6]/div/div/div/button").click()

time.sleep(3)
pixels = 700
driver.execute_script("window.scrollBy(0, arguments[0])", pixels)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='manage-comment']/div/div/div[3]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-comment']/div/div/div[3]").send_keys("Amazing!")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='manage-comment']/button").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[5]/a").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='new_forum']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-forum']/div[1]/div/input").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-forum']/div[1]/div/input").send_keys("ML on the rise")
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='manage-forum']/div[2]/div/div/div[3]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='manage-forum']/div[2]/div/div/div[3]").send_keys("Yes, machine learning (ML) has become increasingly popular in recent years and is being applied to a wide range of industries and applications. ML algorithms use statistical methods to enable computers to 'learn' from data without being explicitly programmed.")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='submit']").click()
time.sleep(4)


driver.find_element(By.XPATH,"//*[@id='navbarResponsive']/ul/li[6]/a").click()
time.sleep(5)














































