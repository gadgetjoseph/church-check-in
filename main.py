from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
from datetime import datetime
import data

# Get the Harrison Sign In site page
driver.get(data.URL)

# First Name
first_name = driver.find_element(By.NAME, "Field1").send_keys(data.FIRST_NAME)

# Last Name
last_name = driver.find_element(By.NAME, "Field2").send_keys(data.LAST_NAME)

# Email
email = driver.find_element(By.NAME, "Field3").send_keys(data.EMAIL)

# Area Code, Prefix, Number
area_code = driver.find_element(By.NAME, "Field207").send_keys(data.AREA_CODE)

pre_fix = driver.find_element(By.NAME, "Field207-1").send_keys(data.PREFIX)

last_four = driver.find_element(By.NAME, "Field207-2").send_keys(data.LAST_FOUR)

# Date
current_month = datetime.now().month
current_sunday_month = driver.find_element(By.XPATH, "//*[@id='Field210-1']").send_keys(current_month)

current_day = datetime.now().day
current_sunday = driver.find_element(By.XPATH, "//*[@id='Field210-2']").send_keys(current_day)

current_year = datetime.now().year
current_sunday_year = driver.find_element(By.XPATH, "//*[@id='Field210']").send_keys(current_year)

# Time
early_hour = driver.find_element(By.NAME, "Field211").send_keys("9")

early_minute = driver.find_element(By.NAME, "Field211-1").send_keys("30")

# Regular
checkbox_regular = driver.find_element(
    By.XPATH, "/html/body/div[1]/form/ul/li[6]/fieldset/div/span[3]/label/span[1]").click()

# With others
checkbox_with_others = driver.find_element(
    By.XPATH, "/html/body/div[1]/form/ul/li[7]/fieldset/div/span[2]/label/span[1]").click()

# Who
with_others = driver.find_element(By.NAME, "Field205").send_keys(data.OTHERS)

# Comments
comments = driver.find_element(By.NAME, "Field208").send_keys(data.COMMENTS)

# Submit Form
# submit = driver.find_element(By.XPATH, '//*[@id="saveForm"]').click()

# #close the website
# driver.close
