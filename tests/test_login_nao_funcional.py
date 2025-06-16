from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
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

# Teste não Funcional:
# Teste de Brute Force
def test_brute_force_tentativas_multiplas():
    driver = criar_driver()
    try:
        for i in range(5):  
            driver.find_element(By.NAME, "username").clear()
            driver.find_element(By.NAME, "password").clear()
            driver.find_element(By.NAME, "username").send_keys("Debora")
            driver.find_element(By.NAME, "password").send_keys(f"SenhaIncorreta{i}")
            driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
            time.sleep(2)

        mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".error").text
        print("Mensagem após tentativas múltiplas:", mensagem_erro)

        assert "could not be verified" in mensagem_erro
        print("Teste de brute force passou, significa que deu os erros esperados.")

    finally:
        driver.quit()


#Teste de SQL Injection no campo Senha
def test_sql_injection_no_campo_senha():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("Debora")
        driver.find_element(By.NAME, "password").send_keys("' OR '1'='1")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(2)

        mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".error").text
        print("Mensagem após tentativa de SQL Injection:", mensagem_erro)

        assert "could not be verified" in mensagem_erro
        print("Teste de SQL Injection passou, significa que a aplicação está protegida contra esse tipo de ataque.")
    except:
        print("Erro ao tentar realizar o teste de SQL Injection.")
        assert False, "Teste de SQL Injection falhou, a aplicação não está protegida."
    finally:
        driver.quit()

# teste de inserção de SQL Injection não passou no teste.

# Teste de Verificação de mensagens de erro
def test_mensagem_erro_segura():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(2)

        mensagem_erro = driver.find_element(By.CSS_SELECTOR, ".error").text
        print("Mensagem de erro exibida:", mensagem_erro)

        # A mensagem não deve conter informações sensíveis como "Exception", "Stack trace", "SQL"
        termos_proibidos = ["Exception", "Stack", "Trace", "SQL", "Database", "root", "localhost"]
        for termo in termos_proibidos:
            assert termo not in mensagem_erro, f"Mensagem de erro contém termo sensível: {termo}"
        print("Teste de mensagem de erro segura, não obteve informações sensíveis.")
    finally:
        driver.quit()


# Teste de Feedback Visual
def test_feedback_visual_apos_erro():
    driver = criar_driver()
    try:
        driver.find_element(By.NAME, "username").send_keys("Debora")
        driver.find_element(By.NAME, "password").send_keys("senhaErrada")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(2)

        elemento_erro = driver.find_element(By.CSS_SELECTOR, ".error")
        visivel = elemento_erro.is_displayed()
        print("Mensagem de erro visível:", visivel)

        assert visivel, "A mensagem de erro não está visível após tentativa inválida."
        print("Teste de feedback visual passou no teste .")
    finally:
        driver.quit()

# Teste de tempo de resposta
def test_tempo_resposta_erro():
    driver = criar_driver()
    try:
        inicio = time.time()
        driver.find_element(By.NAME, "username").send_keys("Debora")
        driver.find_element(By.NAME, "password").send_keys("senhaErrada")
        driver.find_element(By.CSS_SELECTOR, ".button:nth-child(1)").click()
        time.sleep(2)  
        fim = time.time()
        tempo = fim - inicio
        print(f"Tempo de resposta do login: {tempo:.2f} segundos")

        assert tempo < 5, "Tempo de resposta muito alto"
        print("Teste de tempo de resposta obeteve a resposta esperada.")
    finally:
        driver.quit()

