import streamlit as st
from PIL import Image

def run_home_app():

    image_url1='https://i0.wp.com/blog.allstay.com/wp-content/uploads/2021/11/2.jpeg?resize=768%2C473&ssl=1.jpg'
    image_url2='https://i0.wp.com/blog.allstay.com/wp-content/uploads/2021/11/6-23.jpg?resize=768%2C504&ssl=1.jpg'
    image_url3='https://ak-d.tripcdn.com/images/0221d120008z8ynm2397C_R_960_660_R5_D.jpg'

    st.sidebar.image(image_url2, width=300)
    st.sidebar.image(image_url3, width=300)
    st.sidebar.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0pmsRADg_SF56CBTgXZ95JEP1NFywsim2eG-tP58kujkSMzFJlLhK8wMDCHJ1fyl3Tus&usqp=CAU.jpg',width=300)
    st.title('NY 호텔은 여기야 놀자!')
    st.video('https://youtu.be/h3fUgOKFMNU',start_time=10,format='video/mp4')
    st.info('뉴욕에 있는 호텔의 리뷰 데이터를 기반으로 EDA, 유저의 선택에 맞는 호텔을 추천해주는 기능을 구현한 앱입니다. ')
    st.image(image_url1,use_column_width=True)
