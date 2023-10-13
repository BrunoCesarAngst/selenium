from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def iniciar_driver():
    chrome_options = Options()
    args = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for arg in args:
        chrome_options.add_argument(arg)

    chrome_options.add_experimental_option('prefs', {
        # alterar o local de download
        'download.default_directory': 'C:\\Users\\brangst\\selenium\\downloads',
        # notificar o google chrome sobre essas alterações
        'download.directory_upgrade': True,
        # desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # 0: Perguntar, 1: Permitir, 2: Bloquear
        # permitir multiple downloads
        'profile.default_content_setting_values.automatic_downloads': 1
    })

    # inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver


driver = iniciar_driver()

# acessando o site do curso
driver.get('https://cursoautomacao.netlify.app/')

botao = driver.find_element(By.ID, 'buttonalerta')
botoes = driver.find_elements(By.ID, 'buttonalerta')

if botao is not None:
    print(f'Botão encontrado: {botao.text}')
if botoes is not None:
    print(f'{len(botoes)} elementos encontrados!')

campo_nome = driver.find_element(By.NAME, 'seu-nome')
radio_buttons = driver.find_elements(By.NAME, 'exampleRadios')

if campo_nome is not None:
    print(f'Campo encontrado: {campo_nome.get_attribute("placeholder")}')
if radio_buttons is not None:
    print(f'{len(radio_buttons)} radio buttons encontrados!')

logo = driver.find_element(By.CLASS_NAME, 'navbar-brand')
links_menu = driver.find_elements(By.CLASS_NAME, 'nav-link')

if logo is not None:
    print(f'Logo encontrado: {logo.text}')
if links_menu is not None:
    print(f'{len(links_menu)} links encontrados!')

link_home = driver.find_element(By.LINK_TEXT, 'Home')
links_partial_text = driver.find_elements(By.PARTIAL_LINK_TEXT, 'Des')

if link_home is not None:
    print(f'Link encontrado: {link_home.text}')
if links_partial_text is not None:
    print(f'{len(links_partial_text)} links encontrados!')

titulo = driver.find_element(By.XPATH, '//*[text()="ZONA DE TESTES"]')

if titulo is not None:
    print(f'Título encontrado: {titulo.text}')

titulo_da_pagina = driver.find_element(By.TAG_NAME, 'h1')
elementos_h4 = driver.find_elements(By.TAG_NAME, 'h4')

if titulo_da_pagina is not None:
    print(f'Título encontrado: {titulo_da_pagina.text}')
if elementos_h4 is not None:
    print(f'{len(elementos_h4)} elementos encontrados!')

input('Pressione qualquer tecla para fechar o navegador...')
driver.close()
