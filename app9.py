import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Etkinlik Katılım Veri Seti İle Dashboard Oluşturalım")
st.write("Bu dashboard, etkinlik verilerini değişken filtrelere göre analiz edip. Bu analizleri görsselleştirerek daha iyi anlamayı sağlamaktadır.")
df = pd.read_csv(r"C:\Users\emirh\Downloads\Dashboard_Etkinlik_Katilim.csv")
st.subheader("Veri Seti ilk 5 Satırı")
st.dataframe(df.head(5))

st.sidebar.header("Filtreler")

tum_sehirler = sorted(df["Sehir"].unique())
secili_sehirler = st.sidebar.multiselect(
    "Şehirleri Seçiniz:",
    options=tum_sehirler,
    default=tum_sehirler
)
tum_etkinlikler = sorted(df["Etkinlik"].unique())
secili_etkinlikler = st.sidebar.multiselect(
    "Etkinlik Türlerini Seçiniz:",
    options=tum_etkinlikler,
    default=tum_etkinlikler
)

tum_puanlar = sorted(df["Memnuniyet"].unique())
secili_puanlar = st.sidebar.multiselect(
    "Memnuniyet Puanlarını Seçiniz:",
    options=tum_puanlar,
    default=tum_puanlar
)
df_filtreli = df[
    (df["Sehir"].isin(secili_sehirler)) & 
    (df["Etkinlik"].isin(secili_etkinlikler)) &
    (df["Memnuniyet"].isin(secili_puanlar))
]
if df_filtreli.empty:
    st.warning("Seçilen filtrelere uygun veri yok")
else:
    st.subheader("Temel Göstergeler")
    col1, col2, col3 = st.columns(3)
    col1.metric("Toplam Katılımcı", df_filtreli.shape[0])
    col2.metric("Ort. Memnuniyet", round(df_filtreli["Memnuniyet"].mean(), 2))
    col3.metric("Şehir Sayısı", df_filtreli["Sehir"].nunique())

    st.subheader("Grafikler")

    st.write("### Memnuniyet Dağılımı")
    fig1, ax1 = plt.subplots()
    ax1.hist(df_filtreli["Memnuniyet"], bins=10, color='orange', edgecolor='black')
    st.pyplot(fig1)
    yorum = st.text_area(
    label="Grafik yorumu: ",
    placeholder="Yorumunuzu buraya yazın...",
    height=150)


    st.write("### Etkinlik Türlerinin Dağılımı")
    fig2, ax2 = plt.subplots()
    pasta_verisi = df_filtreli["Etkinlik"].value_counts()
    ax2.pie(pasta_verisi, labels=pasta_verisi.index, autopct='%1.1f%%')
    st.pyplot(fig2)
    yorum1 = st.text_area(
    label="Grafik yorumu:",
    placeholder="Yorumunuzu buraya yazın...",
    height=150)
