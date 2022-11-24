import streamlit 
import pandas as pd
import requests 
import snowflake.connector 
from urllib.error import URLError

streamlit.title('My Healthy Diner')

streamlit.subheader('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard Boiled free-range eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list is a pandas data_frame

my_fruit_list = my_fruit_list.set_index('Fruit')
# Displaying only selected fruits in the grid
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#streamlit.dataframe(my_fruit_list)

#########################################
# Add on package
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
#########################################

streamlit.stop()

#--------------------------------------------------------------#
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()

streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
#--------------------------------------------------------------#

fruit_add = streamlit.text_input('What fruit would you like ADD?','jackfruit')
streamlit.write('Thanks for adding ', fruit_add)

my_cur.execute("insert into fruit_load_list values ('from st')")
