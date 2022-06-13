import streamlit
streamlit.title("My Parents new healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text('1. Dosa')
streamlit.text("2. Idly")
streamlit.text("3. Wada")
streamlit.text('🥣 🥗 🐔 🥑🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Pick list
fruits_selected = streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index),['Avacardo','Strawberries'])
# Display the streamlit dataframe 
# streamlit.dataframe(my_fruit_list)

#fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the streamlit dataframe 
#streamlit.dataframe(fruits_to_show)
