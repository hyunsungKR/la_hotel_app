import streamlit as st
from PIL import Image
from app_home import run_home_app
from app_eda import run_eda_app
from app_userchoice import run_userchoice_app

img = Image.open('data/image_newyork.jpg')
st.set_page_config(page_title='Newyork Hotel')


def main() :

    menu =['Home','User Choice','EDA']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home':
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'User Choice' :
        run_userchoice_app()




if __name__=='__main__':
    main()