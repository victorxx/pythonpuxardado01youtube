from playwright.sync_api import sync_playwright
import time

url = "https://www.youtube.com/results?search_query=megaman+detonado"

try:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto(url,timeout=50000000)
        page.wait_for_load_state('networkidle',timeout=500000)
        links=set()
        for _ in range(3):
            page.mouse.wheel(0,1000000)
            print('rolando para pegar os videos')
            time.sleep(2)
            videos=page.locator('a#video-title')
            contagem=videos.count()
        for i in range(contagem):
            href=videos.nth(i).get_attribute('href')
            if href and "watch?v=" in href:
                video_id=href.split('v=')[1]
                embed=f'"https://www.youtube.com/embed/{video_id}"'
                links.add(embed)
        final=','.join(links)
        print(final)
        with open(r'C:\Users\vitor\Desktop\imagenslinks.txt','a+',encoding='utf-8') as file:
            file.write(final+'\n')
            print('escrito no arquivo já pode abrir o arquivo verificar os videos la')
        browser.close()
except:
    print('deu algo errado')
