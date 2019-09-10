import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
datos=pd.read_csv("saberbta.csv")
print(datos.head(50))
#datos=pd.read_csv("homicidios.csv",parse_dates=True)
#print(datos.head())
#datos=pd.read_csv("homicidios.csv",parse_dates=True,index_col='Fecha')
#print(datos.head(20))
print(datos.describe())
datosResumidos=datos[['ESTU_EDAD','ESTU_GENERO','PUNT_C_NATURALES','PUNT_SOCIALES_CIUDADANAS','PUNT_INGLES','PUNT_GLOBAL']]
print(datosResumidos.corr())
fig = plt.gcf()
datosResumidos.plot.scatter('ESTU_EDAD','PUNT_GLOBAL')
fig.savefig('output.png')
datosResumidos.plot.scatter('PUNT_C_NATURALES','PUNT_INGLES')
datosResumidos.boxplot('PUNT_GLOBAL')
datosResumidos.boxplot('ESTU_EDAD')
#datosResumidos.sort_values(by='ESTU_EDAD', ascending=1)
datosResumidos.plot('ESTU_EDAD','PUNT_GLOBAL')
datosResumidos.hist('ESTU_EDAD')
fig.savefig('histEdades.png')
datosResumidos.hist('PUNT_GLOBAL')
fig.savefig('histPuntaje.png')
fig.savefig('cienciasXingles.png')
fig.savefig('boxPlotPuntaje.png')
fig.savefig('boxPlotEdad.png')

#print(fechaDepto.describe())
#print(datosResumidos.describe())
