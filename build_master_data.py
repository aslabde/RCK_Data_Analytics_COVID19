#INPUT:
#
#
#
#

#OUTPUT:
#
#
#
#

import pandas as pd
import matplotlib.pyplot as plt

#BUILD CSV A: OFFICAL DATA CONFIRMED CASES AT SPAIN BY DATE
datos=pd.read_csv('casos_tecnica_ccaa.csv')
cols =['fecha','num_casos']
datos_filtrados = datos[cols]
datos_agrupados = datos_filtrados.groupby('fecha').agg('sum')
datos_agrupados_df=pd.DataFrame(datos_agrupados)
datos_agrupados_df.to_csv('csv_A.csv')


#BUILD CSV B: JHU -> VACINNATION DATA AT SPAIN BY DATE
load_data=pd.read_csv('time_series_covid19_vaccine_global.csv')
columns_b = ['Country_Region','Date','People_fully_vaccinated']
data_filtered_b=load_data[columns_b]
aggregated_data_b=data_filtered_b[data_filtered_b["Country_Region"].str.contains("Spain")]
aggregated_data_b=aggregated_data_b.groupby('Date').agg('sum')
aggregated_data_b.to_csv('csv_B.csv')

#BUILD CSV C: OFFICIAL DATA HOSPITALIZATIONS, DEATHS AND RECOVERIES AT SPAIN BY DATE
