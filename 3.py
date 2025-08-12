from playwright.sync_api import sync_playwright
import time
import requests
import os

caminho_destino=r'C:\Users\vitor\Desktop\\'
if not os.path.exists(caminho_destino):
    os.makedirs(caminho_destino)


try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page()
        page.goto('https://www.serra.es.gov.br/', timeout=5000000)
        page.wait_for_load_state('networkidle',timeout=500000)
        for x in range(1):
            page.mouse.wheel(0,100000)
            time.sleep(1)
        imagens=page.locator('img')
        contagem=imagens.count()
        print(f'total de imagens encontradas')
        for y in range(contagem):
            try:
                src=imagens.nth(y).get_attribute('src')
                if src and src.startswith('https'):
                    nome_arquivo=f'imagem_{y}.jpg'
                    caminho_arquivo=os.path.join(caminho_destino,nome_arquivo)
                    resposta=requests.get(src,timeout=5000)
                    if resposta.status_code==200:
                        with open(caminho_arquivo,'wb') as file:
                            file.write(resposta.content)
                            print(f'IMAGEM salva {y}:{caminho_arquivo}')
                    else:
                        print('falha ao baixar imagem {y}')
            except Exception as e:
                print('error ao processar imagem')
        
except:
    print('ok deu algo errado')
