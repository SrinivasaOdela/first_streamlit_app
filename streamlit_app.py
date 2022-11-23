import streamlit as st
import pandas as pd
st.title('My Healthy Diner')

st.subheader('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket smoothie')
st.text('🐔 Hard Boiled free-range eggs')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list is a pandas data_frame

st.multiselect("Pick some fruits:", list(my_fruit_list.index))
#pick list 
st.dataframe(my_fruit_list)
