from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument("--disable-popup-blocking")
driver=webdriver.Chrome(options=options)
driver.get("https://www.dice.com/dashboard/login")
time.sleep(10)
email=""
password=""
email_input=driver.find_element(By.ID,"email")
password_input=driver.find_element(By.ID,"password")
email_input.send_keys(email)
password_input.send_keys(password)
x=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary.btn-lg.btn-block")
x.send_keys(Keys.ENTER)
time.sleep(20)
try:
    close_button = driver.find_element(By.ID, "sms-remind-me")
    close_button.click()
    print("SMS pop-up closed successfully")
except Exception as e:
    print(f"Error closing SMS pop-up: {str(e)}")

time.sleep(5)
popup=driver.find_element(By.CLASS_NAME,"fe-button-leter")
popup.click()

if driver.current_url=="https://www.dice.com/home/home-feed":
    print("login sucessfull")
time.sleep(5)
location_input = driver.find_element(By.ID, "google-location-search")
location_input.clear()
locaton="California"
location_input.send_keys(locaton)
skill_input=driver.find_element(By.ID,"typeaheadInput")
skill="Django"
skill_input.send_keys(skill)
time.sleep(3)
search_button=driver.find_element(By.ID,"submitSearch-button")
search_button.click()
time.sleep(15)
select_today = driver.find_element(By.CSS_SELECTOR, "button[data-cy='posted-date-option'][data-cy-index='1']")
select_today.click()
time.sleep(6)
try:
    # Wait for the element with the specified class to be clickable, then click it
    card_title = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "card-title-link"))
    )
    card_title.click()
except Exception as e:
    print("Error clicking on the card title:", e)
time.sleep(5)
easy_apply=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary")
easy_apply.click()
time.sleep(8)
next_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-next.btn-block")
next_button.click()
time.sleep(2)
apply_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-next.btn-split")
time.sleep(10)
