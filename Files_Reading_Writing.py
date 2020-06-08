# Writing and Reading Files
# pandas 
import pandas as pd 

# Arrays 
# list
my_list = ["Hello", "goodbye","Car","Airplane","road"]
my_2nd_list = [1,2,3,4,5]
#my_list_list = [my_list,my_2nd_list]

# Create dataframe
#my_dataframe = pd.DataFrame(my_list_list)
my_dataframe = pd.DataFrame( {"GameNumber":my_2nd_list,"Word" :my_list} )

# Write data frame to flie
my_dataframe.to_csv("my_file.csv") # Remove the row number
