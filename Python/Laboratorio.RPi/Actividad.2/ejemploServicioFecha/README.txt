#Ejemplo de usar systemctl
--------------------------------------------
@Laura Arjona
@October 2020


El archivo del servicio (.service) y del timer (.timer) se deben llamar IGUAL y ambos
deben estar en la carpeta 
 /etc/systemd/system/

En este ejemplo, el serivio ejecuta el arhivo en python savetime.py.
Este archivo python puede estar donde quieras, pero tienes que poner la ruta donde está
dentro del fichero .service.

En este ejemplo, yo lo tengo en /home/pi/servicioHora/
Por tanto, dentro del servicio tengo las siguientes líneas:

ExecStart=/usr/bin/python /home/pi/servicioHora/savetime.py  
WorkingDirectory=/home/pi/servicioHora/

----------------------------------------------------------------
# Documentación sobre el uso del timer. En español! :)
https://wiki.archlinux.org/index.php/Systemd_(Espa%C3%B1ol)/Timers_(Espa%C3%B1ol)


---------------------------------------------------------------------------


Comandos para empezar, parar, y ver el estado de servicios
Ejecuta esto dentro de la terminal de la RPi (por SSH o VNC)

# Antes de lanzar el servicio
 $ sudo systemctl daemon-reload

# Empezar el servicio
$ sudo systemctl start dateService

# Arrancar el servicio al arrancar la RPi
$ sudo systemctl enable dateService

# Parar el servicio
$ sudo systemctl stop dateService

# Ver el estado del servicio
 $ sudo systemctl status dateService

