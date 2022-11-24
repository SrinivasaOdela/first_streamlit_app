import streamlit as st
import pandas as pd
import requests 

st.title('My Healthy Diner')

st.subheader('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket smoothie')
st.text('🐔 Hard Boiled free-range eggs')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list is a pandas data_frame

my_fruit_list = my_fruit_list.set_index('Fruit')
# Displaying only selected fruits in the grid
fruits_selected= st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)


#st.dataframe(my_fruit_list)

#########################################
# Add on package
st.header("Fruityvice Fruit Advice!")

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
#st.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)
#########################################
