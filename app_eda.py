import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import platform

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Linux':
    rc('font', family='NanumGothic')    
else:
    print('Unknown system')


def run_eda_app():
    st.sidebar.image('https://images.trvl-media.com/lodging/26000000/25140000/25131000/25130973/0bd3d484.jpg?impolicy=resizecrop&rw=670&ra=fit.jpg',width=500)
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2f5AMPaQ7tniBEt8ADWUPUWPAH5akn4Erow&usqp=CAU.jpg',width=320)
    df = pd.read_csv('data/nyc0730.csv')
    df=df[['name','Number of reviewers','Overall score','Cleanliness','Comfort','Facilities','Staff','Value for money'
   ,'Location','good Fitness Center','Bar','Non-smoking Rooms']]
    df = df.dropna()
    st.subheader('데이터프레임 확인')
    st.dataframe(df.head(3))
    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())
    

    st.subheader('최대 / 최소 데이터 확인하기')
    column_list = df.columns[2:]
    selected_column=st.selectbox('컬럼을 선택하세요.',column_list)
    df_min=(df.loc[df[selected_column]==df[selected_column].min(),])
    df_max=(df.loc[df[selected_column]==df[selected_column].max(),])

    st.text('최소값 데이터입니다.')
    st.dataframe(df_min)
    st.text('최대값 데이터입니다.')
    st.dataframe(df_max)

    st.subheader('컬럼 별 히스토그램')

    histogram_column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.', column_list)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 10, 30, value=10, step=1)

    fig1 = plt.figure()
    plt.hist(data= df, x=histogram_column, rwidth=0.8, bins=my_bins)
    plt.title(histogram_column + ' Histogram')
    plt.xlabel(histogram_column)
    plt.ylabel('Count')
    st.pyplot(fig1)


    st.subheader('상관 관계 분석')

    selected_list=st.multiselect('상관 분석을 하고싶은 컬럼을 선택하세요',column_list)
    
    if len(selected_list) >= 2 :
        fig2=plt.figure()
        df_corr=df[selected_list].corr()
        sb.heatmap(data=df_corr,annot=True,fmt='.2f',cmap='coolwarm',linewidths=0.5)
        st.pyplot(fig2)