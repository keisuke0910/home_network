import streamlit as st
import pandas as pd

st.title('【テスト】Streamlitでタイトル')

st.write('目指せサブ３')


df = pd.read_csv('csv/runキロ換算表.csv')

df

from PIL import Image
img = Image.open('tigers.jpeg')

st.image(img, caption='tiger')
'''
# タイトル<h1>
## 見出し２<h2>
'''

'''
*で箇条書き１  
*で箇条書き２

'''





'''


1.でそのままナンバリング  
2.でそのままナンバリング


---で水平線
___でどう？

-[]でチェックボックス<br>
-[]でチェックボックス<br>
-[]でチェックボックス<br>

**強調**

*斜体*

テーブル
❘い❘❘ろ❘
❘１❘❘２❘

リンク
表記：[グーグル](URL)
表示：https://www.google.com/?hl=ja


'''


