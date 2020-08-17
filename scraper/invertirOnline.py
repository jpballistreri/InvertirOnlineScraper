import requests
import json
from connectMongo import Dict2Mongo
from random import randint
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep

config = json.load(open('config.json'))
urls = []

for x in config["urls"]:
	urls.append(config["urls"][x])

collection = config["collection"]

timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
#collection = datetime.now().strftime("%Y/%m/%d") 
fecha = datetime.now().strftime("%d/%m/%Y")
hora = datetime.now().strftime("%H:%M:%S")
contador=0

dictSalida = {}
dictSalida[contador] = {}
'''
dictSalida[fecha] = {}
dictSalida[fecha][hora] = {}
'''


def clean(string):
	return string.replace('  ','').replace('\r','').replace('\n','')

def startScraper(url, contador):
	print(f'Scraping {url}')

	accion = url.split('/')[-1]
	#dictSalida[fecha][hora][accion]={}

	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	tabla = soup.find('tbody').find_all('tr')

	#document.querySelector('tbody').querySelectorAll('tr')
	
	for x in range(len(tabla)):
		
		fila = tabla[x].find_all('td')

		nombre = clean(fila[0].find('span').text)
		simbolo = clean(fila[0].find('b').text)
		ultimoOperado = clean(fila[1].text)
		variacionDiaria = clean(fila[2].text)
		cantidadCompra = clean(fila[3].text)
		precioCompra = clean(fila[4].text)
		precioVenta = clean(fila[5].text)
		cantidadVenta = clean(fila[6].text)
		apertura = clean(fila[7].text)
		minimo = clean(fila[8].text)
		maximo = clean(fila[9].text)
		ultimoCierre = clean(fila[10].text)
		montoOperado = clean(fila[11].text)
		fechaHora = clean(fila[12].text)

		
		'''
		dictSalida[fecha][hora][accion][simbolo.replace('.','_')] = { 'accion':accion,'nombre': nombre, 
						'simbolo': simbolo, 'ultimoOperado': ultimoOperado, 
						'variacionDiaria':variacionDiaria, 'cantidadCompra':cantidadCompra, 
						'precioCompra':precioCompra, 'precioVenta':precioVenta,
						'cantidadVenta':cantidadVenta, 'apertura':apertura, 'minimo':minimo, 
						'maximo':maximo, 'ultimoCierre':ultimoCierre, 'montoOperado':montoOperado,
						 'fechaHora':fechaHora, 'fecha':fecha, 'hora':hora } 
		'''

		dictSalida[contador] = { 'accion':accion,'nombre': nombre, 
						'simbolo': simbolo, 'ultimoOperado': ultimoOperado, 
						'variacionDiaria':variacionDiaria, 'cantidadCompra':cantidadCompra, 
						'precioCompra':precioCompra, 'precioVenta':precioVenta,
						'cantidadVenta':cantidadVenta, 'apertura':apertura, 'minimo':minimo, 
						'maximo':maximo, 'ultimoCierre':ultimoCierre, 'montoOperado':montoOperado,
						 'fechaHora':fechaHora, 'fecha':fecha, 'hora':hora } 

		contador += 1

for url in urls:
	#sleep(randint(1,5))
	
	startScraper(url, 0)

print('creando archivo de salida Json..')
with open('./tempJson/result.json', 'w') as fp:
	json.dump(dictSalida, fp)


dict2Mongo = Dict2Mongo(dictSalida, collection.replace('/',''))
