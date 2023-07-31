import streamlit as st
import pandas as pd

st.write("Hello")
st.write(1234)
st.write(pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [10, 20, 30, 40],
}))

st.markdown('#제목1')
st.markdown('##제목2')
st.markdown('###제목3')
st.markdown('Streamlit is **_really_cool**.')


st.write('1 + 1 = ', 2)
st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')