from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

#Teste Funcional Autenticação do sistema:
# Teste de Login com as credenciais corretas
def test_login_sucesso():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("Debora")
        driver.find_element(By.NAME, "password").send_keys("Teste1234")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(3)
        assert "Accounts Overview" in driver.page_source, "Login falhou ou página incorreta"
        print("Teste de login com sucesso passou.")
    finally:
        driver.quit()

# Teste de Login com Senha incorreta
def test_login_senha_incorreta():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("Debora")
        driver.find_element(By.NAME, "password").send_keys("Debora1234")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(3)
        mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".error").text
        print("Mensagem de erro capturada:", mensagem_erro)

        assert "The username and password could not be verified." in mensagem_erro, "Mensagem de erro incorreta ou não exibida"
        print("Teste de login com senha incorreta passou.")
    finally:
        driver.quit()

# Teste de Login com Usuário inexistente
def test_login_usuario_inexistente():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("Vinicius")
        driver.find_element(By.NAME, "password").send_keys("Teste1234")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(3)
        mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".error").text
        print("Mensagem de erro capturada:", mensagem_erro)

        assert "The username and password could not be verified." in mensagem_erro, "Mensagem de erro incorreta ou não exibida"
        print("Teste de login com usuário inexistente passou.")
    finally:
        driver.quit()

# Teste Funcional Entrada de dados: 
# Testar caraceteres especiais no campo de usuário
def test_login_caracteres_especiais():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("Debora!@#")
        driver.find_element(By.NAME, "password").send_keys("Teste1234")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(3)
        mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".error").text
        print("Mensagem de erro capturada:", mensagem_erro)

        assert "The username and password could not be verified." in mensagem_erro, "Mensagem de erro incorreta ou não exibida"
        print("Teste de login com caracteres especiais passou.")
    finally:
        driver.quit()

# Teste de Login com Inserção de SQL Injetcion
def test_login_sql_injection():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("Debora' OR '1'='1")
        driver.find_element(By.NAME, "password").send_keys("Teste1234")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()

        try:
            mensagem_erro = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".error"))
            ).text
            print("Mensagem de erro capturada:", mensagem_erro)
            assert "The username and password could not be verified." in mensagem_erro, "Mensagem de erro incorreta"
            print("Teste de login com SQL injection passou.")
        except:
            print("Mensagem de erro não encontrada para tentativa de SQL Injection.")
            assert False, "Mensagem de erro não apareceu. O sistema pode estar vulnerável ou não retornou feedback visível."
    finally:
        driver.quit()

# teste de inserção de SQL Injection não passou no teste.

# Teste de Login com Limite de Caracteres
def test_login_limite_caracteres():
    driver = criar_driver()
    try:
        usuario_muito_longo = "Debora" * 20 
        senha_muito_longa = "Teste1234" * 20

        driver.find_element(By.NAME, "username").send_keys(usuario_muito_longo)
        driver.find_element(By.NAME, "password").send_keys(senha_muito_longa)
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(3)

        try:
            mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".error").text
            print("Mensagem de erro capturada (limite de caracteres):", mensagem_erro)
            assert "The username and password could not be verified." in mensagem_erro
            print("Teste de limite de caracteres passou.")
        except:
            print("Nenhuma mensagem de erro visível ao usar limite extremo de caracteres.")
            assert False, "Sistema não retornou mensagem clara para entrada muito longa."
    finally:
        driver.quit()

