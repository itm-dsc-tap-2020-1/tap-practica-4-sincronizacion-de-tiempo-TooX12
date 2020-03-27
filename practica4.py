import datetime
from time import ctime
import ntplib
import os

time_1 = datetime.datetime.now()

servidor_de_tiempo = "time-a-g.nist.gov"
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
time_2=datetime.datetime.now()

time_server = datetime.datetime.fromtimestamp(respuesta.orig_time)
time_server.strftime('%a %b %d %H:%M:%S.%f %Y')

adjust = (time_2-time_1)/2

clock = time_server+adjust

print('\nTiempo Inicio: '+str(time_1))
print('Tiempo Llegada: '+str(time_2))
print('Tiempo Servidor: '+str(time_server))
print('Ajuste: '+str(adjust))
print('Reloj: '+str(clock))

os.system(f"date --set '{clock}'")
