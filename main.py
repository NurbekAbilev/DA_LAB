__author__ = '21224'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wv.csv",encoding='cp1252')
df2 = pd.read_csv("codes.csv")

print(df2)
# Time,Time Code,Country Name,Country Code,GDP per person,Population,Life expectancy
# plt.plot(x = data["Country Name"].values,y = data["Life expectancy"].values)

# x = GDP
# y = Life Expectancy
# rad = pop

le_col = "Life expectancy"
gdp_col = "GDP per person"
pop_col = "Population"
code_col = "Country Code"
df = df[ (df[le_col]!="..") & (df[gdp_col]!="..") & (df[pop_col]!="..")]

df[[gdp_col,le_col,pop_col]] = df[[gdp_col,le_col,pop_col]].apply(pd.to_numeric)
x = df[gdp_col].values
y = df[le_col].values
r = df[pop_col].values
country_names = df[code_col].values

regions = {
    "Asia":"yellow",
    "Europe":"blue",
    "Africa":"pink",
    "Americas":"brown"
}

colors = []
for index, row in df2.iterrows():
    code = row['alpha-3']
    region = row['region']

    if(region not in regions):
        colors.append("black")
        continue

    # print(code)
    found = False
    for index2 , row2 in df.iterrows():
        if(row2[code_col] == code):
            found = True

    if(not found):
        colors.append("black")
        continue

    colors.append(regions[region])



for i, txt in enumerate(country_names):
    plt.annotate(txt, (x[i], y[i]))

plt.scatter(x,y,s=r/100000,c = colors, alpha=0.5)
plt.show()
