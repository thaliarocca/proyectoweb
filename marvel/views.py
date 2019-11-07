from django.shortcuts import render
from django.http import HttpResponse
import hashlib
import urllib
import json
from urllib.request import urlopen


# Create your views here.
def show(request):
	publickey = "5c465051a788252db815c7bd342d97a1"
	privatekey = "68d5d07dd7a4ff064c19956ba9b3027df293824c"
	ts = "1"
	character="hulk"
	if request.method =='POST':
		character = request.POST['name']
		if len(character.split())>1:
			character=character.replace(" ","%20")

	word = ts+privatekey+publickey
	otrohash = hashlib.md5()
	otrohash.update(bytes(word, 'UTF-8'))
		
	url = ("https://gateway.marvel.com/v1/public/characters?name="+character+"&ts="+ts+"&apikey="+publickey+"&hash="+otrohash.hexdigest())
	response = urlopen(url)
	jsonResponse=json.loads(response.read())
	nombre="sin datos"
	descripcion="sin datos"
	imagen="sin datos"
	if jsonResponse['data']['total']!=0:
		nombre = jsonResponse['data']['results'][0]['name']
		descripcion = jsonResponse['data']['results'][0]['description']
		imagen = jsonResponse['data']['results'][0]['thumbnail']['path']+"."+jsonResponse['data']['results'][0]['thumbnail']['extension']
	return render(request, 'mostrar.html', {'nombre':nombre, 'descripcion':descripcion, 'imagen':imagen})
def cget(request):
	token="123456"
	url = ("http://localhost/servicioweb/servidor.php?hash=123456")
	response = urlopen(url)
	jsonResponse=json.loads(response.read())
	nombres=jsonResponse["datos"][0]["nombres"]
	apellidos=jsonResponse["datos"][0]["apellidos"]
	pa=jsonResponse["datos"][0]["pa"]
	codigo=jsonResponse["datos"][0]["codigo"]
	return render(request,'cget.html',{'nombres':nombres,'apellidos':apellidos})
