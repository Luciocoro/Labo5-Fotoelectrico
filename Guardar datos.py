#Guardar datos
import pandas as pd
import time

l_onda = 300
v_min = -3
v_max = 1
t_integracion = 2

corriente = range(100)
retardo = range(100)
esc_temp =range(100)
esc_corr = range(100)

df = pd.DataFrame() #DataFrame vacio
df['Corriente [A]'] = corriente
df['Potencial de retardo [V]'] =  retardo
df['Escala temp'] = esc_temp
df['Escala corriente'] = esc_corr
df['Tiempo integracion'] = pd.Series([t_integracion],index = [0])
df['Tiempo'] = pd.Series([time.ctime()],index = [0])

df.to_csv(rf'Barrido {l_onda}nm - V[{v_min}-{v_max}].csv')