import streamlit as st
import pandas as pd

# まずタイトル
st.title('【テスト】Streamlitでタイトル')

# 文字列
st.write('データフレーム')

# 手書きのデータフレーム
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})
df