# Add the import steps to bring in the different packages
import streamlit
import snowflake.connector
import pandas

# Give the page a title
streamlit.title("Zena's Amazing Athleisure Catalog")

# Connect to Snowflake then assign the cursor
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Execute a SQL step to pull back data from snowflake and save it into a variable 'my_catalog'
my_cur.execute("select color_or_style from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")   
my_catalog = my_cur.fetchall()

# put the dafta into a pandas dataframe
df=pandas.DataFrame(my_catalog)

# create a list from the above dataframe, with '0' being the positional variable chosen
color_list=df[0].tolist()

# Create a selection box based on the list above
option=streamlit.selectbox("Pick a sweatsuit color or style:", list(color_list))

# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
# use the option selected to go back and get all the info from the database
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
streamlit.image(df2[0],width=400,caption= product_caption)
streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])



         


    



