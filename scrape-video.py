from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def download_videos(link, id):
    cookies = {
    '_gid': 'GA1.2.587426574.1692300404',
    '__gads': 'ID=c80298901d7060c3-223630eafbdf0080:T=1692300404:RT=1692300404:S=ALNI_MaNLIygbSupgy77_YA-UJEIREOXyA',
    '__gpi': 'UID=00000d8bf21db0cf:T=1692300404:RT=1692300404:S=ALNI_MYJmRxMmRxb-8aIIH93fvBSThMA3g',
    '__cflb': '0H28v8EEysMCvTTqtu4Ydr4bADFLp2DZp8EDQ7iJmEu',
    '_gat_UA-3524196-6': '1',
    'FCNEC': '%5B%5B%22AKsRol_C7mFskC6CS3WYjdezGquaXQGjmtMqxS0HTd4ovUNCwEn28R8U-qspYiMWKqBVogs4Ufk67kjfs7u2ihlZDJRBwmekXNycgz00ksxGOjR08GaWZhZj5v_PmvZ7vTOy3TAzc5AWPR3FlfYhkmglxKG9jsW80w%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
    '_ga': 'GA1.2.2041002378.1692300404',
    '_ga_ZSF3D6YSLC': 'GS1.1.1692300404.1.1.1692300650.0.0.0',
    }
    
    headers = {
    'authority': 'ssstik.io',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.587426574.1692300404; __gads=ID=c80298901d7060c3-223630eafbdf0080:T=1692300404:RT=1692300404:S=ALNI_MaNLIygbSupgy77_YA-UJEIREOXyA; __gpi=UID=00000d8bf21db0cf:T=1692300404:RT=1692300404:S=ALNI_MYJmRxMmRxb-8aIIH93fvBSThMA3g; __cflb=0H28v8EEysMCvTTqtu4Ydr4bADFLp2DZp8EDQ7iJmEu; _gat_UA-3524196-6=1; FCNEC=%5B%5B%22AKsRol_C7mFskC6CS3WYjdezGquaXQGjmtMqxS0HTd4ovUNCwEn28R8U-qspYiMWKqBVogs4Ufk67kjfs7u2ihlZDJRBwmekXNycgz00ksxGOjR08GaWZhZj5v_PmvZ7vTOy3TAzc5AWPR3FlfYhkmglxKG9jsW80w%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; _ga=GA1.2.2041002378.1692300404; _ga_ZSF3D6YSLC=GS1.1.1692300404.1.1.1692300650.0.0.0',
    'hx-current-url': 'https://ssstik.io/en',
    'hx-request': 'true',
    'hx-target': 'target',
    'hx-trigger': '_gcaptcha_pt',
    'origin': 'https://ssstik.io',
    'referer': 'https://ssstik.io/en',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    params = {
    'url': 'dl',
    }
    
    data = {
    'id': link,
    'locale': 'en',
    'tt': 'ejlRN3Bh',
    }
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")
    downloadLink = downloadSoup.a["href"]

    mp4File = urlopen(downloadLink)
    with open(f"tiktoks/{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

driver = webdriver.Chrome()
driver.get("https://www.tiktok.com/@leannachester")

time.sleep(1)

scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source, "html.parser")
videos = soup.find_all("div", {"class":"tiktok-16ou6xi-DivTagCardDesc eih2qak1"})

print(len(videos))

for index, video in enumerate(videos):
    download_videos(video.a["href"], index)
    time.sleep(10)