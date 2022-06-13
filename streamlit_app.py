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

# Pick list
streamlit.multiselect("Pick some Fruits", list(my_fruit_list.index))
# Display the streamlit dataframe 
streamlit.dataframe(my_fruit_list)
