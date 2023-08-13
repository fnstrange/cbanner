CBANNER.PY es un programilla escrito en python que te permitirá configurar un banner personalizado para tu sistema operativo Linux. Para utilizarlo sólo debes seguir estos pasos:


![Captura](https://github.com/fnstrange/scripts/assets/101374780/4231abb7-8525-45f5-be21-4d5f94be4ddd)

0. Preparación del sistema descargando los paquetes necesarios:
    #pip install requests
    #pip install psutil

1. Descarga el archivo desde Github.

2. Deshabilitar el banner predefinido:
    #sudo chmod -x /etc/update-motd.d/*

3. Crear los directorios:
    #sudo mkdir -p ~/bin/
    #sudo cp [directorio_de_descarga]/cbanner.py ~/bin/

4. Editar el archivo de sesión bashrc:
    #sudo vim ~/.bashrc

5. Agregar la siguiente línea al final del archivo bashrc:
     python3 ~/bin/cbanner.py
