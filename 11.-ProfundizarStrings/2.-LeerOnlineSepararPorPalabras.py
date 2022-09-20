from urllib.request import Request,urlopen


palabras = []
request = Request("https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt")
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
with urlopen(request) as response:
    for linea in response:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabras_por_linea)

print (palabras)