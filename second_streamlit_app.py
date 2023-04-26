import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena's Amazing Athleisure Catalog")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select color_or_style from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")   
my_catalog = my_cur.fetchall()



#streamlit.dataframe(my_sweatshirt_list)        
 
#my_sweatshirt_list = my_sweatshirt_list.set_index('0')
         
#fruits_selected=streamlit.multiselect("Pick a sweatsuit color or style:", list(my_sweatshirt_list))
#streamlit.dataframe(fruits_selected)

    



