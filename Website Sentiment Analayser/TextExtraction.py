import pandas as pd
import DataCleaning as cleaning
number = 0
link_data = pd.read_csv("D:\ADITYA\DATASETS\BlackCoffer\Input-csv.csv")

link_data = link_data.dropna()

for i in range(0, len(link_data)):
    data_para = cleaning.collect_website_data(link_data['URL'][i])
    data_para = cleaning.clean_data(data_para)
    data_title = cleaning.collect_website_title(link_data['URL'][i])
    data_title = cleaning.clean_data(data_title)
    name = link_data['URL_ID'][i]
    newfile = open( '{0}.txt'.format(link_data['URL_ID'][i]), "w+")
    newfile.write(data_title)
    newfile.write(data_para)
    newfile.close()   
    

    
