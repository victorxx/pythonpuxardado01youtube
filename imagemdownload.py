from playwright.sync_api import sync_playwright
import time
import requests

try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://br.pinterest.com/uniter1265/garotas-japonesas/',timeout=5000000)
        page.wait_for_load_state('networkidle',timeout=500000)
        for x in range(10):
            imagens=page.locator('img')
            contagem=imagens.count()
            page.mouse.wheel(0,10000000)
        for y in range(contagem):
            try:
                src=imagens.nth(y).get_attribute('src')
                if src:
                    print(src)
            except Exception as e:
                print(f'error ao obter a imagem')
        browser.close()
        print('programa finalizado com sucesso')

     

        

except:
    print('ok deu algo errado')
