import requests

direccion = "http://www.omdbapi.com/?apikey=da22215a&i=tt3896198" #url a la que quiero llamar

#hacer peticion http
respuesta= request.get(direccion)

if respuesta.status == 200:
    print(respuesta.text)
    datos= respuesta.json()
else:
    print("se ha producido un error", respuesta.status_code)