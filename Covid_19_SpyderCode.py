#importing pandas
import pandas as pd 

#importing requests library of python
import requests 

#Step 1 : Data Collection :  

#Variable url saves the path of the website from where I am collecting data from
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'

#req is the variable which stores all the data fethced from the URL
req = requests.get(url) 

#pd.read_html is a function of pandas which extracts the tabular information and stores
#it in our variable raw_data_wiki
raw_data_from_wiki = pd.read_html(req.text)

#the dataframe on which we want to work is assigned to target_data
target_data = raw_data_from_wiki[10]


#Step 2 : Data Cleaning :

#We rename the column names for my dataframe
target_data.columns = ['col0', 'Country', 'Total_Cases', 'Total_Deaths', 'Total_Recoveries', 'col5']

#We remove columns which I do not require for our analysis
target_data = target_data[['Country', 'Total_Cases', 'Total_Deaths', 'Total_Recoveries']]

#The last rwo does not contain data that I require so I assign it to a variable(row 243 and 244)
last_index = target_data.index[-1]

#The variable containing the last index is dropped.
#I made sure not to hardcode it so that if changes are made data is not lost.
target_data = target_data.drop([last_index,last_index-1])

#Removed country names with brackets and replace them with space using the replace method of strings and regex
target_data['Country'] = target_data['Country'].str.replace('\[.*\]','')

#Removing "No data" entries in columns and replacing them with zero so as to not mess up my analysis.
target_data['Total_Recoveries'] = target_data['Total_Recoveries'].str.replace('No data','0')
target_data['Total_Cases'] = target_data['Total_Cases'].str.replace('No data','0')
target_data['Total_Deaths'] = target_data['Total_Deaths'].str.replace('No data','0')

#Removing data in Total_Deaths columns containing a + and replacing them with space.
target_data['Total_Deaths'] = target_data['Total_Deaths'].str.replace('+','')

#Changing data type of Total_Case,Total_Deaths and Total_Recoveries from string to integer for easier analysis
target_data['Total_Cases'] = pd.to_numeric(target_data['Total_Cases'])
target_data['Total_Deaths'] = pd.to_numeric(target_data['Total_Deaths'])
target_data['Total_Recoveries'] = pd.to_numeric(target_data['Total_Recoveries'])

#Step 3 : Data Storage :

#Exporting cleaned dataset to excel for using in Tableau
target_data.to_excel(r'covid19_dataset.xlsx')










