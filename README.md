# NY호텔은 여기야 놀자! 👀
## 📌 Project Explanation 
* python의 Library들을 활용하여 각 리뷰의 평점에따라 사용자가 원하는 호텔을 찾아낼 수 있도록 하는 웹 대시보드입니다.
* EDA를 눌러보시면 데이터별로 분석된 차트를 확인하실 수 있습니다.
* booking.com의 호텔 리뷰 데이터를 이용하였습니다.
* AWS EC2를 이용하여 서버를 관리하였습니다.
* Github Actions를 이용한 CI/CD를 사용하였습니다.


## 📌hyunsungKR
<a href="https://github.com/hyunsungKR/"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/></a> <a href="https://hyunsungstory.tistory.com/"><img src="https://img.shields.io/badge/Tistory-466BB0?style=flat-square&logo=Tistory&logoColor=white"/></a>

## 📌Languages
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>



# 📌Library
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/matplotlib.pyplot-40AEF0?style=flat-square&logo=&logoColor=white"/> <img src="https://img.shields.io/badge/Seaborn-006600?style=flat-square&logo=&logoColor=white"/> 

# 📌Tool
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/>

## 📌Code block
```python
    # 유저가 선택한 컬럼으로 데이터 시각화 과정
    histogram_column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.', column_list)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 10, 30, value=10, step=1)

    fig1 = plt.figure()
    plt.hist(data= df, x=histogram_column, rwidth=0.8, bins=my_bins)
    plt.title(histogram_column + ' Histogram')
    plt.xlabel(histogram_column)
    plt.ylabel('Count')
    st.pyplot(fig1)
```
```python
    # 유저가 선택한 컬럼으로 상관관계 분석과정
    selected_list=st.multiselect('상관 분석을 하고싶은 컬럼을 선택하세요',column_list)
    
    if len(selected_list) >= 2 :
        fig2=plt.figure()
        df_corr=df[selected_list].corr()
        sb.heatmap(data=df_corr,annot=True,fmt='.2f',cmap='coolwarm',linewidths=0.5)
        st.pyplot(fig2)
```
```python
    # 유저가 선택한 메뉴의 평점이 가장 높은 곳과, 가성비가 가장 좋은 곳 추천
    select=['good Fitness Center','Bar','Non-smoking Rooms']
    choice=st.sidebar.selectbox('Select',select)
        if choice == 'good Fitness Center' :
        st.title('좋은 헬스장을 소유하고있는 호텔 리스트입니다.')
        
        st.dataframe(df.loc[df[choice] == 1,])
        
        st.subheader('좋은 헬스장을 소유하고있는 호텔 중 평점이 가장 높은 여기는 어때요?')
        max1 = df.loc[df[choice] == 1,]['Overall score'].max()
        max2 = df.loc[df[choice] == 1,]['Value for money'].max()
        st.dataframe(df.loc[(df[choice] == 1) & (df['Overall score'] == max1),])
        st.subheader('좋은 헬스장을 소유하고있는 호텔 중 가성비가 가장 좋은 여기는 어때요?')
        st.dataframe(df.loc[(df[choice] == 1) & (df['Value for money'] == max2),])
```

## 📌 URL
  - http://ec2-3-36-77-30.ap-northeast-2.compute.amazonaws.com:8502/

## 📌 Screen Shot
![image](https://user-images.githubusercontent.com/120348500/207800332-72945408-0875-4355-9b2f-90450b909d34.png)
![image](https://user-images.githubusercontent.com/120348500/207800402-d3d495ae-9ea0-43de-afa7-552a92081c5f.png)
![image](https://user-images.githubusercontent.com/120348500/207800476-e78001d3-a893-4aeb-b799-1f7d96e44b47.png)
![image](https://user-images.githubusercontent.com/120348500/207800570-490bc326-57f0-46ab-9c0f-ba4700d89767.png)


## 📌 Reference

호텔 리뷰 데이터 : https://www.kaggle.com/datasets/thedevastator/30000-booking-com-reviews-for-hotels-worldwide

메인화면 동영상 : https://youtu.be/h3fUgOKFMNU
