
# import pandas as pd
 
# # Define a dictionary containing employee data
# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# # Convert the dictionary into DataFrame 
# df = pd.DataFrame(data)
 
# # select two columns
# print(df[['Name', 'Qualification']])


import pandas as pd
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
 
# creating a dataframe from list
dictionary = pd.DataFrame(dict)
 
# using isnull() function  
print(dictionary.isnull())

# filling missing value using fillna()  
print(dictionary.fillna(0))