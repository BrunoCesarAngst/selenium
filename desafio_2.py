import time
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
    botao_login = driver.find_element(By.LINK_TEXT, 'Desafios')
    time.sleep(1)
    # clicar no botão de login
    botao_login.click()
    time.sleep(1)
    # rolar a página 1000 pixels
    driver.execute_script('window.scrollBy(0, 400);')
    time.sleep(1)
    # # encontrar o campo de senha
    dados_usuario = driver.find_element(By.ID, 'dadosusuario')
    time.sleep(1)
    # # digitar a senha
    dados_usuario.send_keys('Bruno César Angst')
    time.sleep(1)
    # encontrar o botão de enviar
    click_aqui = driver.find_element(By.ID, 'desafio2')
    time.sleep(1)
    # clicar no botão de enviar
    click_aqui.click()
    time.sleep(5)
    input_escondido = driver.find_element(By.ID, 'escondido')
    time.sleep(1)
    # digitar novamente dados_usuario
    input_escondido.send_keys('Bruno César Angst')
    time.sleep(1)
    # encontrar o botão de validar
    validar = driver.find_element(By.ID, 'validarDesafio2')
    time.sleep(1)
    # clicar no botão de validar
    validar.click()

    input('Pressione qualquer tecla para fechar o navegador...')
    driver.close()


if __name__ == "__main__":
    main()
