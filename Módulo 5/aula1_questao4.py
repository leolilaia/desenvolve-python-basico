#Biblioteca
import datetime

#Data atual
from datetime import date
data_atual = date.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print("Data: ", data_em_texto)

#Hora atual
hora_atual = datetime.datetime.now()
hora_em_texto = '{:02d}:{:02d}'.format(hora_atual.hour, hora_atual.minute)
print("Hora: ", hora_em_texto)