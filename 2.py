from playwright.sync_api import sync_playwright
import time

url = "https://www.youtube.com/results?search_query=playsatation+1++games"

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_load_state('networkidle', timeout=30000)

        links = set()

        print('🔄 Iniciando rolagem para carregar vídeos...')
        for _ in range(3):
            page.mouse.wheel(0, 10000)
            time.sleep(2)

        # Localizar todos os vídeos após a rolagem
        videos = page.locator('a#video-title')
        contagem = videos.count()
        print(f"🎥 Total de vídeos localizados: {contagem}")

        for i in range(contagem):
            href = videos.nth(i).get_attribute('href')
            if href and "watch?v=" in href:
                video_id = href.split('v=')[1].split('&')[0]
                embed = f'"https://www.youtube.com/embed/{video_id}"'
                links.add(embed)

        # Gerar string final com quebras de linha
        final = ',\n'.join(sorted(links))
        print("✅ Links coletados com sucesso:\n", final)

        # Escreve no arquivo (modo append)
        with open(r'C:\Users\vitor\Desktop\imagenslinks.txt', 'a+', encoding='utf-8') as file:
            file.write(final + '\n')
            print('📝 Links salvos no arquivo com sucesso!')

        browser.close()

except Exception as e:
    print(f'❌ Ocorreu um erro: {e}')
