import streamlit as st
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt



df1 = pd.read_csv("./edx_precios.csv")

st.title("Analisis Gráfico")


st.markdown("### Segmentación del nivel de ventas de la plataforma EDX ###")
st.markdown("1)Segmentación por precio")

y = list(df1["price_int"])
x = list(df1["percentage"])

plt.barh(y,x, color = ["green","blue","yellow","orange","red"])
plt.title("Porcentaje de ventas por rango de precio")
plt.xlabel("porcentaje %")
plt.ylabel("rangos de precio")


st.pyplot(plt)
plt.clf()


edx_idiomas = pd.read_csv("./edx_idiomas.csv")

st.markdown("2)Segmentación por idioma")

idiomas = list(edx_idiomas["idioma"])
sizes = list(edx_idiomas["porcentaje"])
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = idiomas, autopct= "%1.1f%%")
ax1.axis("equal")
plt.title("Porcentaje de ventas por idioma del curso")
plt.legend()


st.pyplot(plt)
plt.clf()


edx_nivel = pd.read_csv("./edx_nivel.csv")

st.markdown("3)Segmentación por nivel")

niveles = list(edx_nivel["nivel"])
b = list(edx_nivel["porcentaje"])
fig1, ax1 = plt.subplots()
ax1.pie(b, labels = niveles, autopct= "%1.1f%%")
ax1.axis("equal")
plt.title("Porcentaje de ventas por nivel del curso")
plt.legend()


st.pyplot(plt)
plt.clf()

df2 = pd.read_csv("./udemy_precios.csv")
st.markdown("### Segmentación del nivel de ventas de la plataforma Udemy ###")
st.markdown("1)Segmentación por precio")



y = list(df2["price"])
x = list(df2["percentage"])

plt.barh(y,x, color = ["green"])
plt.title("Porcentaje de ventas por rango de precio")
plt.xlabel("porcentaje %")
plt.ylabel("rangos de precio")


st.pyplot(plt)
plt.clf()

udemy_nivel = pd.read_csv("./udemy_nivel.csv")

st.markdown("2)Segmentación por nivel")

niveles = list(udemy_nivel["nivel"])
b = list(udemy_nivel["porcentaje"])
fig1, ax1 = plt.subplots()
ax1.pie(b, labels = niveles, autopct= "%1.1f%%")
ax1.axis("equal")
plt.title("Porcentaje de ventas por nivel del curso")
plt.legend()

st.pyplot(plt)
plt.clf()

udemy_idiomas = pd.read_csv("./udemy_idiomas.csv")
st.markdown("3)Segmentación por idioma")

idiomas = list(udemy_idiomas["idioma"])
sizes = list(udemy_idiomas["porcentaje"])
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = idiomas, autopct= "%1.1f%%")
ax1.axis("equal")
plt.title("Porcentaje de ventas por idioma del curso")
plt.legend()

st.pyplot(plt)
plt.clf()

coursera_idiomas = pd.read_csv("./coursera_idiomas.csv")

st.markdown("### Segmentación del nivel de ventas de la plataforma Coursera ###")

st.markdown("De coursera la información que puedo aproximar es como se segmenta el nivel de ventas por idioma, más del 80 por ciento de los cursos se imparten en ingles por lo que se induce que la mayoria de los cursos vendidos sean en esta lengua.")

idiomas = list(coursera_idiomas["idioma"])
sizes = list(coursera_idiomas["porcentaje"])
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels = idiomas, autopct= "%1.1f%%")
ax1.axis("equal")
plt.title("Porcentaje de ventas por idioma del curso")
plt.legend()

st.pyplot(plt)
plt.clf()


st.markdown("### WORDCLOUD ###")

import streamlit as st
from PIL import Image

image = Image.open('./nube_output.png')

st.image(image)