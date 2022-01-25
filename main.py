import streamlit as st
import pandas as pd
from PIL import Image

st.title('【テスト】Streamlitでタイトル')

st.write('目指せサブ３')


df = pd.read_csv('csv/runキロ換算表.csv')

df


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
  
  
  
'''# ④リンク
[グーグル](https://www.google.com/?hl=ja)

'''

'''# ⑤カラー
<font color="Red">テキスト</font>  
* テキスト  
    * テキスト  
    * テキスト  
- テキスト  
1. テキスト  
2. テキスト  
    3. テキスト  
1行目  
2行目
<br>
<br>
3行目  

  
```java:title  
int i = 0; //コード  
```  


'''
