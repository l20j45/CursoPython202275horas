import json
from urllib import request
from urllib.request import Request,urlopen

respuesta = Request('https://www.globalmentoring.com.mx/api/clima.json')
respuesta.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
with urlopen(respuesta) as response:
    mensaje= response.read().decode('utf-8')
    json_respuesta = json.loads(mensaje)
    #descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
    descripcion_clima = json_respuesta.get('clima')[0]['descripcion']
    print(f"Descripcion del clima {descripcion_clima} ")
    temperaturaMinima = json_respuesta['principal']['temp_min']
    temperaturaMaxima = json_respuesta.get('principal')['temp_max']
    print(f"Temperatura minima {temperaturaMinima} ")
    print(f"Temperatura maxima {temperaturaMaxima} ")
    