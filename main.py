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
ほらね、ていうか全ての最後に、”空白スペース×２” は重要  
'''
  
  
  
'''# ③強調と斜体と打ち消し線と水平線
**強調**  
*斜体*  
~~テキスト~~  
***  
---  
'''  
  
  
  
'''# ④リンク
[グーグル](https://www.google.com/?hl=ja)  

'''

'''# ⑤リスト
* テキスト  
    * テキスト  
    * テキスト  
- テキスト  
1. テキスト  
2. テキスト  
    3. テキスト  

'''


'''# ⑥コードの挿入
  
```  
  
print('hello world')  
  
```  

'''


'''# ⑦テキストエリアの追加
> ここからはテキストエリアです  
こんな感じ  

'''



