# # importing pandas as pd
# import pandas as pd
 
# # importing numpy as np
# import numpy as np

# #empty df
# df1 = pd.DataFrame()
# print(df1)

# #df using list
# data2 = ["hello","my","name","is","shelvi"]
# df2 = pd.DataFrame(data2)
# print(df2)

# #df using dict of array/list
# data3 = {"Name":["Shelvi","Cp"],"Age": [23,24],"Address":["Gangoh","Balia"]}
# df3 = pd.DataFrame(data3)
# print(df3)

# #defining column differently
# data4 = [["shelvi",24],["archit",30]]
# df4 = pd.DataFrame(data4,columns=["name","age"])
# print(df4)

#defining rows(index) differently
# data5 = {"Name":["A","B"],"Marks":[100,88]}
# df5 = pd.DataFrame(data5,index=["rank1","rank2"])
# print(df5)

# # Define a dictionary containing employee data
# data6 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 'Age':[27, 24, 22, 32], 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
# df6 = pd.DataFrame(data6)
# print(df6[["Name","Address",'Qualification']])

# # Define a dictionary containing employee data
# data7 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 'Age':[27, 24, 22, 32], 'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
# df7 = pd.DataFrame(data7)
# print(df6.iloc[2])
# print(df6["Age"])

# data8 = dict = {'First Score':[100, 90, np.nan, 95],'Second Score': [30, 45, 56, np.nan],'Third Score':[np.nan, 40, 80, 98]}
# df8 = pd.DataFrame(data8)
# df8_new = df8.fillna(6)
# print(df8_new)

# data9 = {'name':["aparna", "pankaj", "sudhir", "Geeku"],'degree': ["MBA", "BCA", "M.Tech", "MBA"],'score':[90, 40, 80, 98]}
# df9 = pd.DataFrame(data9)
# for i,j in df9.iterrows():
#     print(i,j)

# columns = list(df9)
# for i in columns:
#     print(df9[i][2])


# # Creating empty series 
# ser1 = pd.Series() 
# print(ser1)

# #creating series from np array
# data10 = np.array([1,2,34,56,78])
# ser2 = pd.Series(data10)
# print(ser2)
# #accessing series element with position
# print(ser2[:3])

# #Creating a series from array with index :
# ser3 = pd.Series(data10,index = [11,12,13,14,15])
# print(ser3)
# #accessing series element with index 
# print(ser3[12])

# #Creating a series from Lists:
# data11 = [1,2,3,4,5]
# ser4 = pd.Series(data11)
# print(ser4)

# #Creating a series from Dictionary:
# data12 = {"Name":["Shelvi","Garg"],"Age": [23,24]}
# ser5 = pd.Series(data12)
# print(ser5)

# #Creating a series using NumPy functions :
# ser6 = pd.Series(np.linspace(2,33,3))
# print(ser6)

# data13 = dict = {'First Score':[100, 90, np.nan, 95],'Second Score': [30, 45, 56, np.nan],'Third Score':[np.nan, 40, 80, 98]}
# df10 = pd.DataFrame(data13)
# print(pd.Series(df10["First Score"]))


# ser7 = pd.Series([1,2,3,4])
# ser8 = pd.Series([5,6,7,8,9])
# ser9 = ser7.sub(ser8,fill_value=0)
# ser10 = ser7.add(ser8)
# print(ser10)
# print(ser9)

# filename = pd.read_csv("abcd_file.csv")
# #making passed row as header
# file1 = pd.read_csv("abcd_file.csv",header=1,index_col = 1)
# file2 = pd.read_csv("abcd_file.csv")
# print(file2)
# file1.dropna(inplace=True)

# #converting dtypes of series
# before = file2.dtypes
# # file2["ShortName"] = file2["ShortName"].astype(str)

# after =file2.dtypes

# print(before)
# print(after)

# #converting series to list
# # label_list = file1["GotoLbel"].tolist()
# # print(label_list.dtypes)


# #returning top n value
# file3 = file2.head(3) 
# print(file3)

# #bottom n
# file4 = file2.tail(3)
# print(file4)

# file5 = pd.read_csv("nba.csv")
# #Calling describe
# print(file5.describe())
# print(file5.describe(include=["object","float","int"]))

# #Convert Pandas Df to Numpy Array
# df11 = pd.DataFrame(file5["Weight"].head())
# df12 = df11.to_numpy()
# print(df12)
# print(type(df12))

# #providing dtype of what we are passing . Ensuring returned value is not a view of another array
# df13 = df11.to_numpy(dtype="float32",copy= False)    
# print(df13)
# print(type(df13))

# #converting series to numpy
# df14 = pd.Series(file5["Weight"].head())
# df15 = df14.to_numpy()
# print(df15)
# print(type(df15))

# #selecting single rowa 
# file6 = pd.read_csv("nba.csv", index_col ="Name") 
# first = file6.loc["Avery Bradley"] 
# second = file6.loc["R.J. Hunter"] 
# print(first,"\n\n",second)

# third = file6.loc[["Avery Bradley","R.J. Hunter"]]
# print(third)
# print(type(third))

# #applying yearly frequency
# index11 = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']  
# ser11 = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio'])
# ser11.index = index11
# print(ser11) 


# ser12 = pd.Series([11, 21, 8, 18, 65, 18, 32, 10, 5, 32, None]) 
# index12 = pd.date_range('2010-10-09 08:45', periods = 11, freq ='Y') 
# ser12.index = index12 
# print(ser12) 

# #Boolean Indexing in Pandas
# # dictionary of lists 
# dict16 = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 'degree': ["MBA", "BCA", "M.Tech", "MBA"], 'score':[90, 40, 80, 98]} 
# df16 = pd.DataFrame(dict, index = [True, False, True, False]) 
# print(df16)
# print(df16.loc[True])
# print(df16.iloc[1])     #iloc can only have integers

# #using insert  and assign 
# df16.insert(1,"id",[11,12,13,14],True)
# df16 = df16.assign(address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']) 

# #inserting new column directly
# Rank = [1,2,3,4]
# df16["Rank"]= Rank
# print(df16)

# #inserting series with different value for each row:
# id_new = pd.Series([]) 

# # running a for loop and asigning some values to series 

# # for i in range(len(df16)): 
# #     if df16["id"][i] == "11": 
# #         id_new[i]="21"
  
# #     elif df16["id"][i] == "12": 
# #         id_new[i]="22"
  
# #     elif df16["id"][i] == "13": 
# #         id_new[i]="23"

# #     else: 
# #         id_new[i]= df16["id"][i]        
# # # inserting new column with values of list made above         
# # df16_new = df16.insert(1,"Id New", id_new) 
# # print(df16_new)
  
# #Delete rows/columns from DataFrame using Pandas.drop()
# df17 = pd.read_csv("nba.csv",index_col = "Name")
# print(df17)

# #dropping passed rows
# df17.drop(["Avery Bradley", "John Holland", "R.J. Hunter","R.J. Hunter"], axis=0 ,inplace = True) #True make changes in original data
# print(df17)

# #Dropping columns with column name
# df18 = df17.drop(["Team","Weight"],axis = 1,inplace = False)
# print(df18)


# #indexing using truncate()
# df19 = pd.DataFrame({'Weight':[45, 88, 56, 15, 71], 
#                    'Name':['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'], 
#                    'Age':[14, 25, 55, 8, 21]}) 
# index_ = pd.date_range('2010-10-09', periods = 5, freq ='Y') 
# df19.index = index_  
# print(df19)

# df20 = df19.truncate(before="2012-10-09",after="2014-10-09")
# print(df20)

  
# #iterating over rows and columns : iteritems(), iterrows(), itertuples()
# dict21 = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
#         'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
#         'score':[90, 40, 80, 98]} 
# df21 = pd.DataFrame(dict21) 

# #ITERATING OVER ROWS : 

# # using iteritems():  iterates over each column as key, value pair with label as key and column value as a Series object.
# for key, value in df21.iteritems(): 
#     print(key, value)

# #using iterrows: return each index value along with a series containing the data in each row.
# for i,j in df21.iterrows():
#     print(i,j)

# #using itertuples : itertuples() this function return a tuple for each row in the DataFrame
# for i in df21.itertuples(): 
#     print(i) 

# #ITERATING OVER COLUMNS
# #create a list of dataframe columns and then iterating through that list to pull out the dataframe columns
# columns21 = list(df21)  
# for i in columns:  
#     # printing the third element of the column 
#     print (df21[i][2]) 
  
# #Working with Missing Data in Pandas
# #fillna isnull() notnull() dropna() replace() interpolate()

# data22 = pd.read_csv("employees.csv") 
# # creating a dataframe from list 
# df22 = pd.DataFrame(data22)  
# print(df22.isnull())
# bool_series = pd.isnull(df22["Gender"])  
# print(df22[bool_series]) 
# df23 = df22.fillna(0)
# print(df23)
# df24 = df22.fillna(method= "pad")   #filling with previous value
# print(df24)
# df25 = df22.fillna(method= "bfill")    #filling with next value
# print(df25)
# df26 = df22["Gender"].fillna("No Gender", inplace = True) 
# print(df26)
# df27 = df22.replace(to_replace = np.nan, value = -99)  

# #Using interpolate() function to fill the missing values using linear method.
# df28 = df22.interpolate(method ="linear",limit_direction="forward")  #replacing with next value
# print(df28)

# #using dropna
# dict29 = {'First Score':[100, np.nan, np.nan, 95], 
#         'Second Score': [30, np.nan, 45, 56], 
#         'Third Score':[52, np.nan, 80, 98], 
#         'Fourth Score':[68,65,64, 65]} 
# df29 = pd.DataFrame(dict29)
# df30 = df29.dropna()     #drop all na values rows and columns
# print(df30)
# df31 = df29.dropna(how="all")
# print(df31)

# #dropping columns with atleast 1 na value
# df32 = df29.dropna(how ="any",axis=1)
# print(df32)

# #dropping rows with atleast 1 na value
# df33 = df29.dropna(how="any",axis=0)
# print(df33)

# df34 = pd.read_csv("nba.csv")
# df35 = df34.sort_values("Name",axis=0,ascending=True,inplace=True,na_position="last")
# print(df35)

# #sorting df by team and then by names
# df36 = df34.sort_values(["Team","Name"],axis=0,ascending=True,inplace=True)
# print(df36)

# #Using Groupby 
# data37 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',  
#                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],  
#         'Age':[27, 24, 22, 32,  
#                33, 36, 27, 32],  
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj', 
#                    'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],  
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd', 
#                          'B.Tech', 'B.com', 'Msc', 'MA']}  
        
# df37 = pd.DataFrame(data37) 
# print(df37)
# df38 = df37.groupby("Name")
# df38.get_group("Jai")
# print(df38)
# print(df38.groups)

# #group a data of “Name” and “Qualification” together using multiple keys 
# df39 = df37.groupby(["Name","Qualification"]).groups
# #print(df39.get_group(("Jai","Msc")))

# df40 = pd.read_csv("nba.csv")
# new = df40["Team"].copy()
# df40["Name"]= df40["Name"].str.cat(df40["Team"],sep=",")
# print(df40)

# #Handling null values while concatenating using na_rep 
# df40["College"]= df40["College"].str.cat(df40["College"],sep=",",na_rep="No College")
# print(df40)

# #Grouping rows in pandas
# dict41 = {'Team':['Arsenal', 'Manchester United', 'Arsenal', 
#                    'Arsenal', 'Chelsea', 'Manchester United', 
#                    'Manchester United', 'Chelsea', 'Chelsea', 'Chelsea'], 
                     
#            'Player':['Ozil', 'Pogba', 'Lucas', 'Aubameyang', 
#                        'Hazard', 'Mata', 'Lukaku', 'Morata',  
#                                          'Giroud', 'Kante'], 
                                           
#            'Goals':[5, 3, 6, 4, 9, 2, 0, 5, 2, 3] } 
# df41 = pd.DataFrame(dict41)
# total_goals= df41["Goals"].groupby(df41["Team"])
# print(total_goals.mean())
  
# data42 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',  
#                  'Gaurav', 'Anuj', 'Princi', 'Abhi'],  
#         'Age':[27, 24, 22, 32,  
#                33, 36, 27, 32],  
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj', 
#                    'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],  
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd', 
#                          'B.Tech', 'B.com', 'Msc', 'MA']}  
# df42 = pd.DataFrame(data42)
# grp42 = df42.groupby('Name') 
# print(grp42["Age"].aggregate([np.sum,np.mean,np.std]))
# print(grp42.filter(lambda x:len(x)>2))
# sc = lambda x:(x-x.mean()/x.std()*10)
# print(grp42.transform(sc))

# df43 = pd.DataFrame({'Last': ['Gaitonde', 'Singh', 'Mathur'], 
#                    'First': ['Ganesh', 'Sartaj', 'Anjali']}) 
# df43["Name"]= df43["First"].str.cat(df43["Last"],sep=" ")
# print(df43)

# import datetime

# # Create date and time with dataframe 
# df44 = pd.date_range('1/1/2011', periods = 10, freq ='H') 
# print(df44)
# x = datetime.datetime.now()
# print(x.month,x.year)


# ts = pd.Timestamp(year = 2009, month = 5, day = 30, hour = 4, second = 49, tz = 'US/Central')
# ts_new = ts.replace(year=2020,month=11)
# print(ts) 
# print(ts.now())
# print(ts.isoformat())

# #Now we will use the Timestamp.timestamp() function to find the number of seconds that 
# # has passed since epoch : 1jan , 1970
# print(ts.timestamp())

# #Pandas Timestamp.date() function return a datetime object with same year, 
# # month and day as that of the given Timestamp object.
# print(ts.date())
# print(ts_new)


# # Series.dt.floor() function to floor the datetime data to the specified frequency.
# ts1 = pd.Series(['2012-12-31 08:45', '2019-1-1 12:30', '2008-02-2 10:30', 
#                '2010-1-1 09:25', '2019-12-31 00:00']) 
# index1 = ["Day1", "Day 2",'Day 3', 'Day 4', 'Day 5']
# ts1.index = index1
# ts1_new = pd.to_datetime(ts1)
# print(ts1_new)

# result_ts1= ts1_new.dt.floor(freq="H")
# print(result_ts1)

# ts2 = pd.Timestamp(year=2020, month = 11 , day=23,hour=8 , second=58,tz="Asia/Calcutta",freq="H")
# print(ts2)

# ts3 = pd.date_range("23/11/2020", periods=4 , freq="H" )
# print(ts3)

# ts4 = pd.date_range(start="23/11/2020",end="29/11/2020",freq="10H")
# for val in ts4:
#     print(val)

# #str.lstrip() : remove spaces from the left side of string, 
# # str.rstrip(): remove spaces from right side of the string
# #  str.strip():  removes spaces from both sides



# df45 = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 
  
# # replacing team name and adding spaces in start and end 
# df45_new = df45["Team"].replace("Boston Celtics", "  Boston Celtics  ").copy() 
  
# # checking with custom removed space string 
# df45_new.str.lstrip()=="Boston Celtics  "
# df45_new.str.rstrip()=="Boston Celtics  "
# print(df45_new)
# print(df45["Team"])

# #reading excel files
# import xlrd
# df46 = pd.read_excel("Sample3.xlsx",sheet_name = "TN Updated Decision Tree",usecols=[0,1])
# print(df46)

# # XlsxWriter is a Python module for writing files in the XLSX file format
# # Create some Pandas dataframes from some data. 
# df51 = pd.DataFrame({'Data': [11, 12, 13, 14]}) 
# df52 = pd.DataFrame({'Data': [21, 22, 23, 24]}) 
# df53 = pd.DataFrame({'Data': [31, 32, 33, 34]}) 
  
# # Create a Pandas Excel writer object  
# # using XlsxWriter as the engine. 
# writer = pd.ExcelWriter('pandas_multiple.xlsx',  
#                           engine ='xlsxwriter') 
  
# # Write each dataframe to a different worksheet. 
# df51.to_excel(writer, sheet_name ='Sheet1') 
# df52.to_excel(writer, sheet_name ='Sheet2') 
# df53.to_excel(writer, sheet_name ='Sheet3') 
  
# # Close the Pandas Excel writer object 
# # and output the Excel file. 
# print(writer.save())
# print(df51)

# #Apply function to every row in a Pandas DataFrame
# def add(a,b,c):
#     return a+b+c

# data55 = {'A':[1, 2, 3],  'B':[4, 5, 6],  'C':[7, 8, 9] } 
# df55 = pd.DataFrame(data55)
# print("Original Data:\n",df55)
# df55["addition"] = df55.apply(lambda row: add(row["A"],row["B"],row["C"]),axis=1)
# print("updated data\n",df55)

# df55["sum"]= df55.apply(np.sum,axis=1)    #easily done with sum 
# print(df55)
      
# #Normalising Data
# def normalize(x,y):
#     x_new= ((x -np.mean([x,y]))/(max(x,y)-min(x,y)))
#     return x_new

# data56 = {'X':[1, 2, 3], 'Y':[45, 65, 89] } 
# df56 = pd.DataFrame(data56) 
# print("Original DataFrame:\n", df56)
# df56["Normalized"] = df56.apply(lambda  row: normalize(row["X"],row["Y"]),axis = 1)

# print("Updated DF:\n",df56)

import pandas as pd
import numpy as np

wine = pd.read_csv("wine.csv")
dfwine = pd.DataFrame(wine)

print(dfwine)
print(dfwine.columns)


# print(dfwine.shape)

# print(dfwine["taster_twitter_handle"])

# handlers = dfwine.groupby("taster_twitter_handle").taster_twitter_handle.count()
# print(handlers)
# reviews_written = pd.Series(handlers,dfwine.taster_twitter_handle)
# # print(reviews_written)

# rating =  dfwine.groupby('points').points.max()
# best_rating_per_price = rating.sort_value(by="price")
# best_rating_per_price.index = dfwine.prices

# print(best_rating_per_price)

price_extremes = dfwine.groupby('variety').price.agg([min, max])
print(price_extremes)
sorted_varieties = price_extremes.sort_values(by = ["min","max"], ascending= False)
print(sorted_varieties)

print(dfwine.groupby(["country","variety"]).size().sort_values(ascending=False))

p1=dfwine.groupby('variety').price.min()
p2 = dfwine.groupby('variety').price.max()
p3 = {"min":p1,"max":p2}
p4 = pd.DataFrame(p3)
print(p4)

ser = pd.isnull(dfwine["price"])
def count(ser): 
    return sum(bool(x) for x in ser) 
y = count(ser)
print(y)



reviews_per_region = dfwine.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)
print(reviews_per_region)