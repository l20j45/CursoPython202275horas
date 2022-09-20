from urllib.request import Request,urlopen

request = Request("https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt")
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
with urlopen(request) as response:
    mensaje=response.read().decode('utf-8')
    for renglon in mensaje.split("\n"):
        print (renglon)
        for palabara in renglon.split(" "):
            print (palabara)

with open('archivo_Internet.txt','w',encoding='utf8') as archivo:
    archivo.write(mensaje)
    