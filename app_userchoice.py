import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from PIL import Image

def run_userchoice_app():
    df = pd.read_csv('data/nyc0730.csv')
    df=df[['name','Number of reviewers','Overall score','Cleanliness','Comfort','Facilities','Staff','Value for money'
   ,'Location','good Fitness Center','Bar','Non-smoking Rooms']]
    df = df.dropna()
    select=['good Fitness Center','Bar','Non-smoking Rooms']
    choice=st.sidebar.selectbox('Select',select)
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSafLhNSoFG5g8_hLOPiShZmi-F5fM__71w_w&usqp=CAU.jpg',width=300)
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvUGeiNkm6qDnnO2MWeHT6janC0Q6Xm6ELFe7u4ay6vooF8sKul89DvFDi0exJTOWaGBU&usqp=CAU.jpg',width=300)

    if choice == 'good Fitness Center' :
        st.title('📌좋은 헬스장을 소유하고있는 호텔 리스트입니다.')
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSY-o2sFUj25Q6-BkjMVjTfu89KwYFq006J_A&usqp=CAU.jpg',width=450)

        st.dataframe(df.loc[df[choice] == 1,])

        st.subheader('📌좋은 헬스장을 소유하고있는 호텔 중 평점이 가장 높은 여기는 어때요?')
        max1 = df.loc[df[choice] == 1,]['Overall score'].max()
        max2 = df.loc[df[choice] == 1,]['Value for money'].max()
        st.dataframe(df.loc[(df[choice] == 1) & (df['Overall score'] == max1),])
        st.subheader('📌좋은 헬스장을 소유하고있는 호텔 중 가성비가 가장 좋은 여기는 어때요?')
        st.dataframe(df.loc[(df[choice] == 1) & (df['Value for money'] == max2),])


    elif choice == 'Bar' :
        st.title('📌분위기 좋은 바가 있는 호텔 리스트입니다.')
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxGq_YW0ButjXzSpyVtEVTFaTyyAI2HtBHOQ&usqp=CAU.jpg',width=450)

        st.dataframe(df.loc[df[choice] == 1,])
        st.subheader('📌분위기 좋은 바를 소유하고있는 호텔 중 평점이 가장 높은 여기는 어때요?')
        max1 = df.loc[df[choice] == 1,]['Overall score'].max()
        max2 = df.loc[df[choice] == 1,]['Value for money'].max()
        st.dataframe(df.loc[(df[choice] == 1) & (df['Overall score'] == max1),])
        st.subheader('📌분위기 좋은 바를 소유하고있는 호텔 중 가성비가 가장 좋은 여기는 어때요?')
        st.dataframe(df.loc[(df[choice] == 1) & (df['Value for money'] == max2),])

    elif choice == 'Non-smoking Rooms':
        st.title('📌방 내부에서 금연인 호텔 리스트입니다.')
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmKzlDGmUGY8I4itiiGCx-dopVisMASbtDOA&usqp=CAU.jpg',width=250)

        st.dataframe(df.loc[df[choice] == 1,])
        st.subheader('📌방 내부에서 금연인 호텔 중 평점이 가장 높은 여기는 어때요?')
        max1 = df.loc[df[choice] == 1,]['Overall score'].max()
        max2 = df.loc[df[choice] == 1,]['Value for money'].max()
        st.dataframe(df.loc[(df[choice] == 1) & (df['Overall score'] == max1),])
        st.subheader('📌방 내부에서 금연인 호텔 중 가성비가 가장 좋은 여기는 어때요?')
        st.dataframe(df.loc[(df[choice] == 1) & (df['Value for money'] == max2),])

        

