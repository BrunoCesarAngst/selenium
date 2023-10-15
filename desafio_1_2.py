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
    driver.get('https://cursoautomacao.netlify.app/')

    botao_dropdown = driver.find_element(By.ID, 'dropdownMenuButton')
    # botao_dropdown.click()  # essa é uma forma de clicar no botão
    # outra forma de clicar no botão é usando o execute_script
    driver.execute_script('arguments[0].click();', botao_dropdown)

    input('Pressione qualquer tecla para fechar o navegador...')
    driver.close()


if __name__ == "__main__":
    main()
