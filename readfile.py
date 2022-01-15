import pandas as pd
import matplotlib.pyplot as plt

datos=pd.read_csv('casos_tecnica_ccaa.csv')
datos.head()
datos.info()

cols =['fecha','num_casos']
datos_filtrados = datos[cols]
datos_filtrados.info()

datos_agrupados = datos_filtrados.groupby('fecha').agg('sum')
datos_agrupados.info()
print(datos_agrupados)
datos_agrupados_df=pd.DataFrame(datos_agrupados)
datos_agrupados_df.to_csv('datos_agrupados.csv')
#plt.scatter(x=datos_agrupados.fecha, y=datos_agrupados.num_casos)
#plt.show