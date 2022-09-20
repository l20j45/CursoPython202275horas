# Leer archivos json
# JSON = javascript Object Notation


import json
from urllib.request import Request,urlopen




respuesta = Request('https://www.globalmentoring.com.mx/api/personas.json')
respuesta.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
with urlopen(respuesta) as response:
    mensaje = response.read().decode('utf-8')
    json_respuesta = json.loads(mensaje)
    print(json_respuesta)
    for persona in json_respuesta['personas']:
        print(f"Personas: {persona['nombre']} ,Edad: {persona['edad']}")
    print(f"Personas total : {json_respuesta['total']}")