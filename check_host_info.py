import socket
import platform
import requests
from requests import get

try:
    request = str(requests.get("https://www.google.com", timeout=5))
except (requests.ConnectionError, requests.Timeout):
    print("Sin conexión a internet. Por favor verifique su conexión.")
else:
    if request == "<Response [200]>":  # evalúa si es que el cliente tiene conexión a internet

        mysystem = platform.system()  # obtener sistema operativo (windows, linux)
        if mysystem == "Linux":
            def obtener_datos_linux():
                try:
                    myhost = socket.gethostname()  # obtener nombre de host
                    myip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # obtener direcció ip privada
                    myip.connect(("8.8.8.8", 80))
                    mypublic = get('https://api.ipify.org').content.decode('utf8')  # obtener dirección ip pública
                    print("[+] Hostname:    ", myhost)
                    print("[+] IP privada:  ", myip.getsockname()[0])
                    print("[+] IP pública:  ", mypublic)
                except TypeError:
                    print("Error: no es posible obtener los datos")
            obtener_datos_linux()

        elif mysystem == "Windows":
            def obtener_datos_windows():
                try:
                    myhost = socket.gethostname()  # obtener nombre de host
                    myip = socket.gethostbyname(myhost)  # obtener dirección ip privada
                    mypublic = get('https://api.ipify.org').content.decode('utf8')  # obtener dirección ip pública
                    print("[+] Hostname:    ", myhost)
                    print("[+] IP privada:  ", myip)
                    print("[+] IP pública:  ", mypublic)
                except TypeError:
                    print("Error: no es posible obtener los datos")
            obtener_datos_windows()
        else:
            pass
