import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena's Amazing Athleisure Catalog")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select color_or_style from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")   
my_catalog = my_cur.fetchall()

selected_df=dataframe(selected)
streamlit.write(selected_df)

#color_list=

#selected=streamlit.selectbox("Pick a sweatsuit color or style:", list(my_catalog))
#streamlit.dataframe(selected)




         


    



