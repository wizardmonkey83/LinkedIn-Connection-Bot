from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from dotenv import load_dotenv
import os

# to run headless (optional)
chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

load_dotenv()
driver = webdriver.Chrome()

LOGIN_PAGE = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
ACCOUNT = os.getenv("LINKEDIN_USER")
PASSWORD = os.getenv("LINKEDIN_PASS")

# login
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
# to avoid detection
time.sleep(random.uniform(1, 10))
wait = WebDriverWait(driver, 3)
try:
    username = driver.find_element(By.ID, "username")
    username.send_keys(ACCOUNT)
except NoSuchElementException:
    print("Unable to locate username field")
try: 
    password = driver.find_element(By.ID, "password")
    password.send_keys(PASSWORD)
except NoSuchElementException:
    print("Unable to locate password field")
try: 
    submit_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]/button')
    submit_button.click()
except NoSuchElementException:
    print("Unable to locate login submission")


# connecting
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(random.uniform(1, 10))
# to connect with locals
try:
    show_all_local = driver.find_element(By.XPATH, '//*[@id="workspace"]/div/div/main/div/div/div/div[4]/section/div/div[1]/div/button')
    show_all_local.click()
    time.sleep(3)
    
    SCROLL_PAUSE_TIME = 2

    # limit to one connect for testing
    count = 0
    while count < 14:
            # finds connect buttons
            connect_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'to connect')]")))
            driver.execute_script("arguments[0].scrollIntoView(true);", connect_button)
            connect_button.click()
            count += 1
            # pauses in case the end of the page is reached, in order to give the site time to load in new results
            time.sleep(SCROLL_PAUSE_TIME)
    driver.quit()
    print(f"{count} connections made")

except NoSuchElementException:
    print("Unable to find connection button")
except KeyboardInterrupt:
    print("Script manually stopped")