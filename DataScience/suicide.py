import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from statistics import mean
#SuicideWord=pd.read_csv("master.csv")
SuicideWordR = pd.read_csv('masterR.csv')
suicideSexpop = pd.read_csv('suicideSexpop.csv')
is_male = SuicideWordR['sex'].isin(['male'])
suicideWordSexMale = SuicideWordR[is_male]
is_potenci = suicideWordSexMale['country'].isin(['Brazil','Canada', 'Chile', 'Colombia','France', 'Germany','Mexico','Spain','United Kingdom','United States'])
suicideWordSexMaleP = suicideWordSexMale[is_potenci]
suicideYearSex = pd.read_csv('suicideSexYearGpt.csv')
#Sacar los paises que necesito para cada grafica de forma individual
is_male = suicideSexpop['sex'].isin(['female'])
suicideSexpop = suicideSexpop[is_male]
#print(suicideYearSexMale[suicideYearSexMale['country']== 'Brazil'])
is_potenci = suicideSexpop['country'].isin(['Brazil','Canada', 'Chile', 'Colombia','France', 'Germany','Mexico','Spain','United Kingdom','United States'])
suicideSexpop = suicideSexpop[is_potenci]
fig, ax = plt.subplots()
suicideSexpop[suicideSexpop['country']== 'Brazil'].plot(x='year',y='population',ax=ax)
suicideSexpop[suicideSexpop['country']== 'Canada'].plot(x='year',y='population',ax=ax)
suicideSexpop[suicideSexpop['country']== 'Chile'].plot(x='year',y='population',ax=ax)
suicideSexpop[suicideSexpop['country']== 'Colombia'].plot(x='year',y='population',ax=ax)
suicideSexpop[suicideSexpop['country']== 'France'].plot(x='year',y='population',ax=ax)
suicideSexpop[suicideSexpop['country']== 'Germany'].plot(x='year',y='population',ax=ax)
suicideSexpop[suicideSexpop['country']== 'Mexico'].plot(x='year',y='population',ax=ax)
suicideSexpop[suicideSexpop['country']== 'Spain'].plot(x='year',y='population',ax=ax)
suicideSexpop[suicideSexpop['country']== 'United Kingdom'].plot(x='year',y='population',ax=ax)
#suicideSexpop[suicideSexpop['country']== 'United States'].plot(x='suicides_no',y='gdp_per_capita ($)',ax=ax)
ax.legend(['Brazil','Canada', 'Chile', 'Colombia','France', 'Germany','Mexico','Spain','United Kingdom','United States'])
plt.show()
#suicideYearSexMalePotenci.to_csv('potenci.csv',index=False)
'''
is_potenci = SuicideWordR['country'].isin(['Brazil','Canada', 'Chile', 'Colombia','France', 'Germany','Mexico','Spain','United Kingdom','United States'])
suicideWordPotenci = SuicideWordR[is_potenci]
is_male = suicideWordPotenci['sex'].isin(['male'])
print(suicideWordPotenci[is_male])
suicideSexYearGpt = pd.read_csv('suicideSexYearGpt.csv')
suicideSexYearGpt.set_index("country",inplace=True)
'''
#fig, ax = plt.subplots()
#suicideSexYearGpt.plot(kind='bar',color='b',ax=ax)
#suicideSexF.plot(kind='bar',color='r',ax=ax)
#ax.legend(["Male","Female"])
#plt.savefig('countryVSsuicideSex')
#plt.show()
#Sacar los paises que no se tienen en cuenta 
#is_country = suicideSexYearGpt['country'].isin(['Argentina', 'Australia', 'Austria', 'Belarus', 'Belgium', 'Brazil','Bulgaria', 'Canada', 'Chile', 'Colombia', 'Cuba', 'Czech Republic','Denmark', 'Ecuador', 'Finland', 'France', 'Germany', 'Hungary','Italy', 'Japan', 'Kazakhstan', 'Kyrgyzstan', 'Latvia', 'Lithuania','Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Philippines','Poland', 'Portugal', 'Puerto Rico', 'Republic of Korea', 'Romania','Russian Federation', 'Spain', 'Sri Lanka', 'Sweden', 'Switzerland','Thailand', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay'])
#suicideSexYearGpt[is_country].to_csv('suicideSexYearGpt.csv',index=False)
#print(SuicideWordR[SuicideWordR['year']==2015])  
#SuicideWord.set_index("country",inplace=True)
#SuicideWordR = SuicideWord[['country', 'year', 'sex', 'age', 'suicides_no', 'population','suicides/100k pop', 'country-year',' gdp_for_year ($) ', 'gdp_per_capita ($)', 'generation']]
suicideSex =pd.read_csv("suicideSex.csv")
suicidegpt = pd.read_csv("suicidegpt.csv")
suicideSexM = pd.read_csv("suicideSexM.csv")
suicideSexM.set_index("country",inplace=True)
suicideSexF = pd.read_csv("suicideSexF.csv")
suicideSexF.set_index("country",inplace=True)
#print(suicideSex.head(50))
#colNames=['country','suicides_no',' gdp_for_year ($) ','gdp_per_capita ($)']
#Suicidegpt = pd.DataFrame(columns=colNames)
#print(SuicideWord.columns)
#colNames=['country','sex','suicides_no']
#suicideSex = pd.DataFrame(columns=colNames)
#TODO como agregar datos al DataFrame
#suicideSex = suicideSex.append([{'country' : 'co','sex':'male','suicides_no':2},{'country' : 've','sex':'male','suicides_no':2}], ignore_index=True)
#tempc = ""
#sm = 0
#sf = 0
#print(SuicideWordR)
#print(SuicideWordR.values[0][0])
#TODO 1 selecionar datos y cotejarlos SUICIDESEX
'''for i in range(27820):
    print(i)
    if(SuicideWordR.values[i][0] == tempc):
        if(SuicideWordR.values[i][2]=='male'):
            sm = sm + SuicideWordR.values[i][4]
            #print('sm : ',sm)
        if(SuicideWordR.values[i][2]=='female'):
            sf = sf + SuicideWordR.values[i][4]
            #print('sf : ',sm)
    else:
        if(i==0):
            tempc = SuicideWordR.values[i][0]
        else:
            print(tempc,'sm: ',sm,'sf: ',sf)
            suicideSex = suicideSex.append([{'country' : tempc,'sex':'male','suicides_no':sm},{'country' : tempc,'sex':'female','suicides_no':sf}], ignore_index=True)
            sm = 0
            sf = 0
            tempc = SuicideWordR.values[i][0]
suicideSex.to_csv('suicideSex.csv',index=False)
'''
'''
tems = []
for i in range(44):
    tems.append(suicideSexM.values[i][1]/suicideSexF.values[i][1])
print(mean(tems))
'''
#TODO 2 Seleccionar datos population/suicides_no y gpt por año y per capita
'''
sn = 0
gptc = 0
gpty = 0
tempc = ''
for i in range(27820):
    print(i)
    if(SuicideWordR.values[i][0] == tempc):
        sn = sn + SuicideWordR.values[i][4] 
    else:
        if(i==0):
            tempc = SuicideWordR.values[i][0]
            gpty = SuicideWordR.values[i][8]
            gptc = SuicideWordR.values[i][9]
        else:
            print(tempc, 'sn :',sn)
            Suicidegpt = Suicidegpt.append([{'country' : tempc,'suicides_no':sn,' gdp_for_year ($) ': gpty , 'gdp_per_capita ($)':gptc}], ignore_index=True)
            sn = 0
            tempc = SuicideWordR.values[i][0]
            gpty = SuicideWordR.values[i][8]
            gptc = SuicideWordR.values[i][9]
print(Suicidegpt.head(100))
Suicidegpt.to_csv('suicidegpt.csv',index=False)
'''
#TODO 3 separar por sexos
"""
suicideSexF = pd.DataFrame(columns=['country','suicides_no'])
suicideSexM = pd.DataFrame(columns=['country','suicides_no'])
for i in range(200):
    if(suicideSex.values[i][1] == 'male'):
        suicideSexM = suicideSexM.append([{'country':suicideSex.values[i][0],'suicides_no':suicideSex.values[i][2]}])
    if(suicideSex.values[i][1] == 'female'):
        suicideSexF = suicideSexF.append([{'country':suicideSex.values[i][0],'suicides_no':suicideSex.values[i][2]}])
suicideSexM.to_csv('suicideSexM.csv',index=False)
suicideSexF.to_csv('suicideSexF.csv',index=False)
"""
#TODO graficar los datos pais vs sexo
'''
fig, ax = plt.subplots()
suicideSexM.plot(kind='barh',color='b',ax=ax)
suicideSexF.plot(kind='barh',color='r',ax=ax)
ax.legend(["Male","Female"])
plt.savefig('countryVSsuicideSex')
plt.show()
'''
#SuicideWordR.plot.scatter('')
#TODO graficar suicidios por capital 
#suicide_no ambos sexos
#is_country = SuicideWord['country'].isin()
#print(is_country.head(50))
#is_country = SuicideWord['country'].isin(['Argentina', 'Australia', 'Austria', 'Belarus', 'Belgium', 'Brazil','Bulgaria', 'Canada', 'Chile', 'Colombia', 'Cuba', 'Czech Republic','Denmark', 'Ecuador', 'Finland', 'France', 'Germany', 'Hungary','Italy', 'Japan', 'Kazakhstan', 'Kyrgyzstan', 'Latvia', 'Lithuania','Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Philippines','Poland', 'Portugal', 'Puerto Rico', 'Republic of Korea', 'Romania','Russian Federation', 'Spain', 'Sri Lanka', 'Sweden', 'Switzerland','Thailand', 'Ukraine', 'United Kingdom', 'United States', 'Uruguay'])
#print()
#SuicideWord[is_country].to_csv('masterR.csv',index=False)
'''
suicideWordgpt = pd.DataFrame(columns=['country','suicides_no','gdp_for_year ($)', 'gdp_per_capita ($)'])
sn = 0
tempc = ''
for i in range(200):
    if(suicideSexM.values[i][0] == tempc):
        sn = sn + suicideSexM.values[i][1] + suicideSexF.values[i][1]
    else:
        if(i==0):
            tempc = suicideSexM.values[i][0]
        else:
            suicidegpt = suicidegpt.append([{'country':tempc,'suicides_no':sn}])
'''
'''
#TODO grupo 3
tempc = ''
tempy = 0
sm = 0
sf = 0
colNames = ['country','year','sex','suicides_no','gdp_for_year ($)','gdp_per_capita ($)']
suicideSexYearGpt = pd.DataFrame(columns=colNames)
for i in range(14540):
    if(SuicideWordR.values[i][0] == tempc):
        if(SuicideWordR.values[i][1] == tempy):
            if(SuicideWordR.values[i][2]=='male'):
                sm = sm + SuicideWordR.values[i][4]
                #print('sm : ',sm)
            if(SuicideWordR.values[i][2]=='female'):
                sf = sf + SuicideWordR.values[i][4]
                #print('sf : ',sm)
        else:
            if(tempy==0):
                tempy = SuicideWordR.values[i][1]
            else:
                #print('country:',tempc,'year',tempy,'sex','male','suicides_no',sm,'country',tempc,'year',tempy,'sex','female','suicides_no',sf)
                suicideSexYearGpt = suicideSexYearGpt.append([{'country':tempc,'year':tempy,'sex':'male','suicides_no':sm,'gdp_for_year ($)':SuicideWordR.values[i][9], 'gdp_per_capita ($)':SuicideWordR.values[i][10]},{'country':tempc,'year':tempy,'sex':'female','suicides_no':sf,'gdp_for_year ($)':SuicideWordR.values[i][9],'gdp_per_capita ($)':SuicideWordR.values[i][10]}], ignore_index=True)
                tempy = SuicideWordR.values[i][1]
    else:
        if(i==0):
            tempc = SuicideWordR.values[i][0]
        else:
            suicideSexYearGpt = suicideSexYearGpt.append([{'country':tempc,'year':tempy,'sex':'male','suicides_no':sm,'gdp_for_year ($)':SuicideWordR.values[i][9], 'gdp_per_capita ($)':SuicideWordR.values[i][10]},{'country':tempc,'year':tempy,'sex':'female','suicides_no':sf,'gdp_for_year ($)':SuicideWordR.values[i][9],'gdp_per_capita ($)':SuicideWordR.values[i][10]}], ignore_index=True)
            sm = 0
            sf = 0
            tempy = 0
            tempc = SuicideWordR.values[i][0]
suicideSexYearGpt.to_csv('suicideSexYearGpt.csv',index=False)
'''
#TODO 4
'''
tempc = ''
tempy = 0
sm = 0
sf = 0
pm = 0
pf = 0
colNames = ['country','year','sex','suicides_no','population','gdp_for_year ($)','gdp_per_capita ($)']
suicideSexpop = pd.DataFrame(columns=colNames)
for i in range(14540):
    print(i)
    if(SuicideWordR.values[i][0] == tempc):
        if(SuicideWordR.values[i][1] == tempy):
            if(SuicideWordR.values[i][2]=='male'):
                sm = sm + SuicideWordR.values[i][4]
                pm = pm +SuicideWordR.values[i][5]
                #print('sm : ',sm)
            if(SuicideWordR.values[i][2]=='female'):
                sf = sf + SuicideWordR.values[i][4]
                pf = pf +SuicideWordR.values[i][5]
                #print('sf : ',sm)
        else:
            if(tempy==0):
                tempy = SuicideWordR.values[i][1]
            else:
                #print('country:',tempc,'year',tempy,'sex','male','suicides_no',sm,'country',tempc,'year',tempy,'sex','female','suicides_no',sf)
                suicideSexpop = suicideSexpop.append([{'country':tempc,'year':tempy,'sex':'male','suicides_no':sm,'population':pm,'gdp_for_year ($)':SuicideWordR.values[i][9], 'gdp_per_capita ($)':SuicideWordR.values[i][10]},{'country':tempc,'year':tempy,'sex':'female','suicides_no':sf,'population':pm,'gdp_for_year ($)':SuicideWordR.values[i][9],'gdp_per_capita ($)':SuicideWordR.values[i][10]}], ignore_index=True)
                tempy = SuicideWordR.values[i][1]
    else:
        if(i==0):
            tempc = SuicideWordR.values[i][0]
        else:
            suicideSexpop = suicideSexpop.append([{'country':tempc,'year':tempy,'sex':'male','suicides_no':sm,'population':pm,'gdp_for_year ($)':SuicideWordR.values[i][9], 'gdp_per_capita ($)':SuicideWordR.values[i][10]},{'country':tempc,'year':tempy,'sex':'female','suicides_no':sf,'population':pm,'gdp_for_year ($)':SuicideWordR.values[i][9],'gdp_per_capita ($)':SuicideWordR.values[i][10]}], ignore_index=True)
            sm = 0
            sf = 0
            tempy = 0
            tempc = SuicideWordR.values[i][0]
suicideSexpop.to_csv('suicideSexpop.csv',index=False)
'''
