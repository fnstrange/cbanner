import platform
import socket
import requests
import psutil
from datetime import datetime

# Obtener la versión del sistema operativo
version_so = platform.platform()

# Obtener la dirección IP pública
ip_publica = requests.get('https://api64.ipify.org?format=json').json()['ip']

# Obtener la dirección IP privada del sistema
adaptador_activo = ""
for adapter, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
        if addr.family == socket.AF_INET and not addr.address.startswith('127'):
            adaptador_activo = adapter
            ip_privada = addr.address
            break

# Obtener la hora actual
hora_actual = datetime.now().time()

# Determinar el saludo del banner según la hora del día
if hora_actual >= datetime.strptime('00:00:00', '%H:%M:%S').time() and hora_actual <= datetime.strptime('12:00:00', '%H:%M:%S').time():
    saludo = f"""
   _____                 _   __  __                  _             
  / ____|               | | |  \/  |                (_)            
 | |  __  ___   ___   __| | | \  / | ___  _ __ _ __  _ _ __   __ _ 
 | | |_ |/ _ \ / _ \ / _` | | |\/| |/ _ \| '__| '_ \| | '_ \ / _` |
 | |__| | (_) | (_) | (_| | | |  | | (_) | |  | | | | | | | | (_| |
  \_____|\___/ \___/ \__,_| |_|  |_|\___/|_|  |_| |_|_|_| |_|\__, |
                                                              __/ |
                                                             |___/ 
    """
elif hora_actual >= datetime.strptime('12:01:00', '%H:%M:%S').time() and hora_actual <= datetime.strptime('20:00:00', '%H:%M:%S').time():
    saludo = f"""
   _____                 _             __ _                                    
  / ____|               | |     /\    / _| |                                   
 | |  __  ___   ___   __| |    /  \  | |_| |_ ___ _ __ _ __   ___   ___  _ __  
 | | |_ |/ _ \ / _ \ / _` |   / /\ \ |  _| __/ _ \ '__| '_ \ / _ \ / _ \| '_ \ 
 | |__| | (_) | (_) | (_| |  / ____ \| | | ||  __/ |  | | | | (_) | (_) | | | |
  \_____|\___/ \___/ \__,_| /_/    \_\_|  \__\___|_|  |_| |_|\___/ \___/|_| |_|
    """

else:
    saludo = f"""
   _____                 _   ______               _             
  / ____|               | | |  ____|             (_)            
 | |  __  ___   ___   __| | | |____   _____ _ __  _ _ __   __ _ 
 | | |_ |/ _ \ / _ \ / _` | |  __\ \ / / _ \ '_ \| | '_ \ / _` |
 | |__| | (_) | (_) | (_| | | |___\ V /  __/ | | | | | | | (_| |
  \_____|\___/ \___/ \__,_| |______\_/ \___|_| |_|_|_| |_|\__, |
                                                           __/ |
                                                          |___/ 
    """

# Generar banner
banner = f"""
==========================================================================
{saludo}
{hora_actual}
Sistema Operativo: {version_so}
Dirección IP Pública: {ip_publica}
Dirección IP Privada: {ip_privada}
==========================================================================
"""

# Mostrar banner generado
print(banner)