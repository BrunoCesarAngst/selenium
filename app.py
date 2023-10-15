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

# como saber se um elemento está habilitado ou não?
campo_idade = driver.find_element(By.ID, 'campoIdade')

if campo_idade.is_enabled():
    # printar o valor do atributo disabled
    print(f'O campo está habilitado? {campo_idade.get_attribute("disabled")}')
else:
    print(f'O campo está habilitado? {campo_idade.get_attribute("disabled")}')

input('Pressione qualquer tecla para fechar o navegador...')

# com seletores css
# tags(section, div, span, etc) e classes(.class)
# combinação de tags e classes (section.class) ou (section .class)
# id(#id)
# combinação de tags e id (section#id) ou (section #id)
# atributos([name=nome_do_atributo])
# combinação de tags e atributos (section[name=nome_do_atributo]) ou (section [name=nome_do_atributo])
# combinação de classes e atributos (.class[name=nome_do_atributo]) ou (.class [name=nome_do_atributo])
# combinação de id e atributos (#id[name=nome_do_atributo]) ou (#id [name=nome_do_atributo])
# combinação de tags, classes e atributos (section.class[name=nome_do_atributo]) ou (section .class [name=nome_do_atributo])
# combinação de tags, id e atributos (section#id[name=nome_do_atributo]) ou (section #id [name=nome_do_atributo])
# combinação de classes, id e atributos (.class#id[name=nome_do_atributo]) ou (.class #id [name=nome_do_atributo])
# combinação de tags, classes, id e atributos (section.class#id[name=nome_do_atributo]) ou (section .class #id [name=nome_do_atributo])
# com ^, $ e * (começa com, termina com e contém)
# quando se quer buscar um elemento que começa com um determinado texto, usa-se o sinal de ^ (section[class^=nome_da_classe])
# quando se quer buscar um elemento que termina com um determinado texto, usa-se o sinal de $ (section[class$=nome_da_classe])
# quando se quer buscar um elemento que contém um determinado texto, usa-se o sinal de * (section[class*=nome_da_classe])
# combinando ^, $ e * (section[class^=nome_da_classe][class$=nome_da_classe][class*=nome_da_classe])
# combinando ^, $ e * com tags (section[class^=nome_da_classe][class$=nome_da_classe][class*=nome_da_classe])
# combinando ^, $ e * com classes (section[class^=nome_da_classe][class$=nome_da_classe][class*=nome_da_classe])
# combinando ^, $ e * com id (section[class^=nome_da_classe][class$=nome_da_classe][class*=nome_da_classe])
# combinando ^, $ e * com atributos (section[class^=nome_da_classe][class$=nome_da_classe][class*=nome_da_classe])
# combinando ^, $ e * com tags, classes, id e atributos (section[class^=nome_da_classe][class$=nome_da_classe][class*=nome_da_classe])

driver.close()
driver.maximize_window() # maximiza a janela do navegador
driver.minimize_window() # minimiza a janela do navegador
driver.fullscreen_window() # coloca a janela do navegador em tela cheia
driver.back() # volta para a página anterior
driver.forward() # avança para a próxima página
driver.refresh() # atualiza a página
driver.get_screenshot_as_file('C:\\Users\\brangst\\selenium\\screenshot.png') # tira um screenshot da página
driver.get_screenshot_as_png() # tira um screenshot da página
driver.get_screenshot_as_base64() # tira um screenshot da página
print(driver.title) # retorna o título da página
print(driver.current_url) # retorna a url da página
print(driver.page_source) # retorna o código fonte da página
get_attribute('atributo') # retorna o valor do atributo do elemento

