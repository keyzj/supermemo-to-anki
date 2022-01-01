import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def prepare_auth_input_str_by_placeholder(placeholder):
    return f".authorization-input input[placeholder='{placeholder}']"


def auth_by_credentials(driver, email, pw):
    email_selector = prepare_auth_input_str_by_placeholder("Email")
    email_elem = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, email_selector)))
    email_elem.clear()
    email_elem.send_keys(email)
    email_elem.send_keys(Keys.RETURN)

    pw_selector = prepare_auth_input_str_by_placeholder("Password")
    pw_elem = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, pw_selector)))
    pw_elem.clear()
    pw_elem.send_keys(pw)
    pw_elem.send_keys(Keys.RETURN)

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".menu-top-container button[class='button menu-logo']")))


def prepare_auth_session(driver):
    s = requests.Session()
    s.headers.update({'cookie-session-key': 'PROD-SMSESSIONID'})

    cookies = driver.get_cookies()
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])

    return s
