import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
            
app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction'])

if app_mode=='Home':
    df_mobil = pd.read_csv('CarPrice.csv')
    st.image('gambar.jpg',width=600)
    st.markdown('Dataset :')
    data=pd.read_csv('CarPrice.csv')
    st.write(data.head())
    st.markdown('Grafik :')
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.title('Car Prize Distribution Plot')
    sns.histplot(df_mobil.price)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()