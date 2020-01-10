import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_present(browser):
	browser.get(link)
	try:
		button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
	except NoSuchElementException:
		button = False
	assert button, "The button is missing!!!"
	#time.sleep(30)