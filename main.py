import streamlit as st
import pandas as pd

st.title('【テスト】Streamlitでタイトル')

st.write('目指せサブ３')


df = pd.read_csv('csv/runキロ換算表.csv')

df

from PIL import Image
img = Image.open('tigers.jpeg')

st.image(img, caption='tiger')
'''# ①タイトル
<h1>は#×１＋半角スペース  
<h2>は#×２＋半角スペース
'''
  
  
  
'''# ②改行
改行は後ろに空白スペース×２  
ほらね
'''
  
  
  
'''# ③強調と斜体
**強調**  
*斜体*
'''
  
  
  
'''# リンク④
[グーグル](https://www.google.com/?hl=ja)

'''


