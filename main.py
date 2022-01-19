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
# タイトル




□□で改行
あああ　　あああ



*で箇条書き１
*で箇条書き２



1.でそのままナンバリング
2.でそのままナンバリング


---で水平線
___でどう？


-[]でチェックボックス
-[]でチェックボックス
-[]でチェックボックス


**強調**で強調

*斜体*で斜体

テーブル
❘い❘❘ろ❘
❘１❘❘２❘

リンク
表記：[グーグル](URL)
表示：https://www.google.com/?hl=ja


'''


