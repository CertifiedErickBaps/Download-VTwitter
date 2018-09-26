#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import shutil
import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
import m3u8
from pathlib import Path
import re

def download(video_url):
	url_prefix = 'https://twitter.com/i/videos/tweet/'
	tweet_id = video_url.split('/')[5]
	video_host = ''
	output_dir = './output' #Directorio creado

	#Crear el directorio
	tweet_dir = Path(output_dir)
	Path.mkdir(tweet_dir, parents=True, exist_ok=True)

	#Busca el video por HTML
	video_player_url = url_prefix + tweet_id
	video_player_response = requests.get(video_player_url)


	#Obtiene el JS
	js_file = BeautifulSoup(video_player_response.text, 'html.parser')
	js_file_url = js_file.find('script')['src'] #Busca el script y el src
	js_file_response = requests.get(js_file_url)

	#Token out
	bearer_token_pattern = re.compile('Bearer ([a-zA-Z0-9%-])+')
	bearer_token = bearer_token_pattern.search(js_file_response.text)
	bearer_token = bearer_token.group(0)

	#Transferir a m3u8
	player_config = requests.get('https://api.twitter.com/1.1/videos/tweet/config/' + tweet_id + '.json', headers={'Authorization': bearer_token})
	m3u8_url_get = json.loads(player_config.text)
	m3u8_url_get = m3u8_url_get['track']['playbackUrl']

	#Obtener el m3u8


# def main()
	# Download videos from twitter
# 	download("https://twitter.com/CamiloVIImx/status/1044303777644326913")
# main()