
from watson_developer_cloud import VisualRecognitionV3
import json
import itertools
import requests
from bs4 import BeautifulSoup
import time

def get_html_image(image_url):
	image_url = 'http://' + image_url
	# Obtiene el html del url
	page = requests.get(image_url)
	html_doc = page.content
	soup = BeautifulSoup(html_doc, 'html.parser')
	# Busca los links que sean img
	links=[]
	for link in soup.find_all('img'):
		if(link.get('src') != None and link.get('src') != ''):
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
	#print(links_clean)
	if len(links_clean)==0:
		return 'NotFound'
	else:
		return links_clean[0]
	
def analize(file, idTweet, fecha,  imageURL, replays, retweets, likes):
	visual_recognition = VisualRecognitionV3(
		version='2018-03-19',
		iam_apikey='dC3S4OLO1_CRvVQVrwVO1E8OqfYnAp5nN4VY7U5_fHIZ'
	)
	classes = visual_recognition.classify(url = imageURL)
	encode = json.dumps(classes.get_result())
	decode = json.loads(encode)
	res = list(decode["images"][0]["classifiers"][0]["classes"])
	res1 = []
	for c in res:
		res1.append(dict(itertools.islice(c.items(), 2)))
	res2=[]
	for c in res1:
		res2.append(str(c.values()))
	res3=[]
	for c in res2:
		a=c[13:]
		b=a[:-2]
		res3.append(b.split(','))
	res4=[]
	for i in res3:
		a=i.pop(0)
		b=a[1:]
		c=b[:-1]
		i.insert(0,c)
		res4.append(i)

	with open(file[:-4] +'ANA.txt', 'a') as myfile:
		for i in res4:
			myfile.write(idTweet+','+fecha+','+imageURL+','+replays+','+retweets+','+likes+','+i[0]+','+i[1])
			myfile.write('\n')
		myfile.write('\n')

def run(file):
	file_url=open(file, 'r')
	list_lines=file_url.readlines()
	list_lines_clean=[]
	for i in list_lines:
		list_lines_clean.append(i.rstrip())
	for i in list_lines_clean:
		line=i.split(',')
		print(line)
		if len(line)>1:
			truelink=get_html_image(line[2])
			print(truelink)
			if not truelink is 'NoEsImagen':
				analize(file, line[0],line[1],get_html_image(line[2]),line[3],line[4],line[5])
			#time.sleep(5)
# run('UNICEFlinkstweets.csv')
# analize('FAOlinkstweets.csv','1043892747583684608','2018-09-23',get_html_image('pic.twitter.com/qb3zBcuEzd'),'0','5','2')
# print(get_html_image('pic.twitter.com/xVWjFENv53'))
