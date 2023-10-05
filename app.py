from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
args = ['--lang=pt-BR', '--window-size=700,700', '--incognito']
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

# acessando o site da pagina do wikipedia sobre o brasil
driver.get('https://pt.wikipedia.org/wiki/Brasil')

input('Pressione qualquer tecla para fechar o navegador...')
