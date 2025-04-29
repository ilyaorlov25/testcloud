from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

url_first = "https://example.com"
url_last = "https://www.iana.org/help/example-domains"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url_first)
h1 = WebDriverWait(driver, 5).until(
    expected_conditions.visibility_of_element_located((By.TAG_NAME, "h1"))
)
assert "Example" in h1.text

link = driver.find_element(by=By.CSS_SELECTOR, value="[href]")
link.click()
assert driver.current_url == url_last

driver.close()
driver.quit()
