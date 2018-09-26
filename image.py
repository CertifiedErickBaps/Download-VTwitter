import requests
from bs4 import BeautifulSoup

def get_html_image(image_url):
    page = requests.get(image_url)
    html_doc = page.content

    soup = BeautifulSoup(html_doc, 'html.parser')
    links=[]
    for link in soup.find_all('img'):
        # if str(link)[0:26]=='https://pbs.twimg.com/media':
        links.append(link.get('src'))
    print(links)

    image_prefix = 'https://pbs.twimg.com/media'



def main():
    get_html_image("https://twitter.com/ChumelTorres/status/1044957699849539584")
main()