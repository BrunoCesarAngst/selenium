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


def verificar_estado_botao(botao):
    """
    Imprime o estado do botão: habilitado ou desabilitado.

    :param botao: Instância do botão do Selenium.
    """
    if botao:
        print(f'Botão encontrado: {botao.text}')
        print('Botão habilitado!' if botao.is_enabled() else 'Botão desabilitado!')


def main():
    driver = iniciar_driver()
    driver.get('https://cursoautomacao.netlify.app/desafios')

    btn1 = driver.find_element(By.ID, 'btn1')
    btn2 = driver.find_element(By.CSS_SELECTOR, 'button[class^="btn2"]')
    btn3 = driver.find_element(By.CSS_SELECTOR, 'button[class$="btn-warning"]')

    for botao in [btn1, btn2, btn3]:
        verificar_estado_botao(botao)

    input('Pressione qualquer tecla para fechar o navegador...')
    driver.close()


if __name__ == "__main__":
    main()
