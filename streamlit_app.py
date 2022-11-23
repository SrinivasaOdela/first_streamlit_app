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

my_fruit_list = my_fruit_list.set_index('Fruit')

st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#pick list 
st.text(my_fruit_list.index)
#fruits_to_show = my_fruit_list.loc[fruits_selected]

st.dataframe(my_fruit_list)
#st.dataframe(fruits_to_show)
