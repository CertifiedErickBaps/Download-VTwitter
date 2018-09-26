#!/usr/bin/env python
# Descarga todas la imagenes del hilo
import requests
from bs4 import BeautifulSoup

def get_html_image(image_url):
    # Obtiene el html del url
    page = requests.get(image_url)
    html_doc = page.content
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Busca los links que sean img
    links=[]
    for link in soup.find_all('img'):
        if(link.get('src') != None):
            links.append(link.get('src'))
    # print(links)

    # Limpia los links que no sean media
    links_clean =[]
    image_prefix = 'https://pbs.twimg.com/media'
    for link_image in links:
        link_image_media = str(link_image).split('/')[3]
        link_image_prefix = str(image_prefix).split('/')[3]
        if( link_image_media == link_image_prefix):
            links_clean.append(link_image)
    # Modifica si quieres todos las imagenes del hilo
    return links_clean[0]

def main():
    x = get_html_image("https://twitter.com/Fortnite_ES/status/1044965200984776705")
    # print(x)
main()