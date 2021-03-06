import streamlit
streamlit.title (" My parents are in Home")
streamlit.header("🥣 Today Menu Break Fast")
streamlit.text("1. 3 Mangoes")
streamlit.text("2. Bananas & Cake")
streamlit.header('🥗Breakfast Menu')
streamlit.text(' 🐔 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑Kale, Spinach & Rocket Smoothie')
streamlit.text('🍞Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
myfruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruit_list = myfruit_list.set_index('Fruit')


#Let's Put a pickUp list for the customers then they can pick up the Fruit want to include

#streamlit.multiselect("pickup Some Fruits:",list(myfruit_list.index),('Avocado','Strawberris'))
fruits_selected=streamlit.multiselect("pickup Some Fruits:",list(myfruit_list.index))
fruits_to_show = myfruit_list.loc[fruits_selected]
#Display the table on the page(table format)

streamlit.dataframe(fruits_to_show)

streamlit.dataframe(myfruit_list)

