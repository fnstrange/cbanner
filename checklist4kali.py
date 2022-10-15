import os
from colorama import Cursor, init, Fore, Back, Style
from time import sleep
from art import text2art

banner = text2art("Checklist4Kali")

print(banner)

if os.path.isdir('/etc/apt/'):

	if os.path.isfile('/etc/apt/sources.list'): #  revisar la existencia de archivo de repositorio
		print(Fore.BLUE+Style.BRIGHT+"<<< Respaldando archivo de repositorio\n") #  respaldar archivo de repositorio
		os.system('sudo mkdir /home/kali/Desktop/Backup')
		os.system('sudo chmod 775 /home/kali/Desktop/Backup')
		os.system('sudo cp /etc/apt/sources.list /home/kali/Desktop/Backup')
		print(Fore.GREEN+Style.BRIGHT+Back.BLACK+u"\U0001F3C1" + ">>> Archivo respaldado")
		
		archSource = open("/etc/apt/sources.list","w+") #  integrar lista de repositorios oficiales
		archSource.seek(2)
		print(Fore.BLUE+Style.BRIGHT+"<<< Agregando repositorios\n")
		archSource.write("#Listado de repositorios\n")
		archSource.write("deb http://http.kali.org/kali kali-rolling main non-free contrib\n")
		archSource.write("deb-src http://http.kali.org/kali kali-rolling main contrib non-free\n")
		archSource.write("deb http://http.kali.org/kali kali-last-snapshot main contrib non-free\n")
		archSource.write("deb http://http.kali.org/kali kali-bleeding-edge main contrib non-free\n")
		archSource.seek(0)
		print(Fore.YELLOW+Style.BRIGHT+archSource.read())
		print(Fore.GREEN+Style.BRIGHT+Back.BLACK+u"\U0001F3C1" + ">>> Repositorios agregados")
		
		print(Fore.BLUE+Style.BRIGHT+"<<< Actualizando repositorios\n") #  actualización de repositorios
		os.system('sudo apt update -y')
		print(Fore.GREEN+Style.BRIGHT+Back.BLACK+u"\U0001F3C1" + ">>> Repositorios actualizados")
		
		print(Fore.BLUE+Style.BRIGHT+"<<< Actualizando paquetes\n") #  instalación de paquetes
		os.system('sudo apt install dsniff driftnet armitage yersinia httrack hostapd-wpe dhcpd lighttpd bettercap asleap hostapd mdk4 xterm isc-dhcp-server mdk4 hcxdumptool beef-xss hcxtools -y')
		os.system('sudo git clone --depth 1 https://github.com/v1s1t0r1sh3r3/airgeddon.git')
		os.system('sudo chmod 775 airgeddon')
		os.system('sudo git clone https://github.com/moxie0/sslstrip.git')
		os.system('sudo chmod 775 sslstrip')
		os.system('cd ..')
		print(Fore.GREEN+Style.BRIGHT+Back.BLACK+u"\U0001F3C1" + ">>> Paquetes actualizados")
			
else:
	print(Fore.RED+Style.BRIGHT+u"\U0001F593"+"Error: el archivo de repositorios no existe")
