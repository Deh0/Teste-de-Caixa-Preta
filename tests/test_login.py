from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def criar_driver():
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    return driver

# Teste de Login com as credenciais corretas
def test_login_sucesso():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("Debora")
        driver.find_element(By.NAME, "password").send_keys("Teste1234")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(3)
        assert "Accounts Overview" in driver.page_source, "Login falhou ou página incorreta"
    finally:
        driver.quit()