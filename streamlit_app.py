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
try:
    fruit_choice = streamlit.text_input("Enter fruit name for info")
    streamlit.write ('Your Chocice : ' , fruit_choice)
    if not fruit_choice:
         streamlit.error(" In valid Fruit , Please enter proper fruit name for info ")
    else:
         #import requests
         fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
         #streamlit.text(fruityvice_response)
         #streamlit.text(fruityvice_response.json()) # Only writes data to Screen
         fruityvice_response = pandas.json_normalize(fruityvice_response.json())
         streamlit.dataframe(fruityvice_response)

except URLError as e:
    streamlit.error()

#streamlit.stop()
#import snowflake.connector as sf
my_cnx = sf.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select current_user(), current_account(), current_region()")
#my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake")
#streamlit.text(my_data_row)

#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.text("Data from Fruit load list")
#streamlit.text(my_data_row)

streamlit.text(" Application 2 Started for Badge 4 ")

my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
# put the dafta into a dataframe
df = pandas.DataFrame(my_catalog)
# temp write the dataframe to the page so I Can see what I am working with
# streamlit.write(df)
# put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)
# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
# use the option selected to go back and get all the info from the database

#"""
#def get_Fruit_load_list():
#    with my_cnx.cursor() as my_cur:
#        my_cur.execute("Select * from fruit_load_list")
#        return my_cur.fetchall()
#
#def insert_row_snowflake(new_fruit):
#    with my_cnx.cursor() as my_cur:
#        my_cur.execute("insert into fruit_load_list values ('"+ new_fruit +"')")
#        return "Thanks for Adding " + new_fruit
#    
#if streamlit.button('Get fruit load list'):
#    my_data_row = get_Fruit_load_list()
#    streamlit.dataframe(my_data_row)
#
#add_my_fruit = streamlit.text_input("Enter fruit name to add")
#if streamlit.button('Add fruit to list'):
#    back_from_function = insert_row_snowflake(add_my_fruit)
#    streamlit.text(back_from_function)
#    
#streamlit.write ('Your Added : ' , add_my_fruit)
#my_cur.execute("insert into fruit_data_list values ('"+ add_my_fruit +"')")
#"""
streamlit.text(" End of Application ")




