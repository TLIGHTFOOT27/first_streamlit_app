import streamlit
import snowflake.connector

streamlit.title("Zena's Amazing Athleisure Catalog")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
with my_cnx.cursor() as my_cur:
         my_sweatshirt_list=my_cur.execute("select $1 as style from ZENAS_ATHLEISURE_DB.PRODUCTS.SWEATSUITS")   
         my_cnx.close()
 
streamlit.dataframe(my_sweatshirt_list)
# my_sweatshirt_list=my_sweatshirt_list.set_index('style')
         
fruits_selected=streamlit.multiselect("Pick a sweatsuit color or style:", list(my_sweatshirt_list.index))
streamlit.dataframe(fruits_selected)

    



