#INPUT:
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
load_data_c=pd.read_csv('casos_hosp_uci_def_sexo_edad_provres.csv')
aggregated_data_c=load_data_c.groupby(['sexo','grupo_edad','fecha']).agg('sum')
aggregated_data_c.to_csv('csv_C.csv')

#BUILD CSV D: HOLIDAYS IN SPAIN
load_data_d=pd.read_csv('calendario_laboral_spain.csv')
columns_d = ['Fecha/Data','Festivo']
holidays_dataset_filtered = load_data_d[columns_d]
holidays_dataset_filtered.to_csv('csv_D.csv')

