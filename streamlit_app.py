import streamlit
import pandas
import requests
import snowflake.connector as sf
from urllib.error import URLError


streamlit.title("My Parents new healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text('1. Dosa')
streamlit.text("2. Idly")
streamlit.text("3. Wada")
streamlit.text('🥣 🥗 🐔 🥑🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
#fruits_selected = streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index))
# Pick list
fruits_selected = streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_selected = streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index))
# Display the streamlit dataframe 
# streamlit.dataframe(my_fruit_list)

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the streamlit dataframe 
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruity Vice Advice")
fruit_choice = streamlit.text_input("Enter fruit name for info","Kiwi")
streamlit.write ('Your Chocice : ' , fruit_choice)


#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json()) # Only writes data to Screen

fruityvice_response = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_response)

streamlit.stop()
#import snowflake.connector as sf
my_cnx = sf.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select current_user(), current_account(), current_region()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake")
streamlit.text(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Data from Fruit load list")
streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

add_my_fruit = streamlit.text_input("Enter fruit name to add")
streamlit.write ('Your Added : ' , add_my_fruit)
my_cur.execute("insert into fruit_data_list values ('"+ add_my_fruit +"')")

