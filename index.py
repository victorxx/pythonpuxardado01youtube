from playwright.sync_api import sync_playwright
import time

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Acessa a página do canal
        page.goto('https://www.youtube.com/@CardioDF/videos', timeout=60000)
        page.wait_for_load_state('networkidle', timeout=60000)

        links = set()  # Usar set para evitar links duplicados

        # Faz scroll várias vezes para carregar mais vídeos
        for _ in range(10):
            page.mouse.wheel(0, 10000)
            print('rolando para pegar os videos...')
            time.sleep(2)  # Espera carregar os novos vídeos

            videos = page.locator('a#video-title-link')
            count = videos.count()
            
            for i in range(count):
                href = videos.nth(i).get_attribute('href')
                if href and "/watch?v=" in href:
                    video_id = href.split('v=')[1]
                    embed_link = f'"https://www.youtube.com/embed/{video_id}"'
                    links.add(embed_link)

        # Junta todos os links separados por vírgula
        final = ','.join(links)
        print(final)

        browser.close()

except Exception as e:
    print('Deu algo errado:', e)
