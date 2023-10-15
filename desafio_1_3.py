from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def configurar_opcoes_chrome():
    """
    Configura as opções do Google Chrome para iniciar o navegador.

    :return: Options configuradas para o Chrome.
    """
    chrome_options = Options()
    configuracoes = [
        '--lang=pt-BR',
        '--window-size=800,600',
        '--incognito'
    ]

    for config in configuracoes:
        chrome_options.add_argument(config)

    prefs = {
        'download.default_directory': 'C:\\Users\\brangst\\selenium\\downloads',
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1
    }
    chrome_options.add_experimental_option('prefs', prefs)

    return chrome_options


def iniciar_driver():
    """
    Inicializa o driver do Chrome com as opções configuradas.

    :return: Instância do driver do Chrome.
    """
    chrome_options = configurar_opcoes_chrome()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver


def main():
    driver = iniciar_driver()
    # acessando o site do curso
    driver.get('https://cursoautomacao.netlify.app/')
    # encontrar o botão de login
    botao_login = driver.find_element(By.LINK_TEXT, 'Login')
    sleep(2)
    # clicar no botão de login
    botao_login.click()
    # encontrar o campo de email
    campo_email = driver.find_element(By.NAME, 'email')
    sleep(2)
    # digitar o email
    campo_email.send_keys('mbcangst@gmail.com')
    # encontrar o campo de senha
    campo_senha = driver.find_element(By.ID, 'senha')
    sleep(2)
    # digitar a senha
    campo_senha.send_keys('123456')
    # encontrar o botão de enviar
    botao_enviar = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    sleep(2)
    # clicar no botão de enviar
    botao_enviar.click()

    input('Pressione qualquer tecla para fechar o navegador...')
    driver.close()


if __name__ == "__main__":
    main()
