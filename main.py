import requests

nombre = input("Ingresa tu nombre: ")
r = requests.get("https://api.github.com")

if r.status_code == 200:
    print(f"Hola {nombre} Conexión exitosa con la API")
else:
    print(" Error en la conexión")