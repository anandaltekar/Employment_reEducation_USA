import sys
import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import pickle

# data = pd.read_csv("CES-dataOG.txt", sep='\t', )
# data = data[data.year < 2019]
# data = data.drop(['footnote_codes'], axis=1)
# data = data[data.year > 2006]
# data.to_csv("CES-Data_updated.txt", sep='\t', index=False)

# tsv_file='CES-Data_updated.txt'
# csv_table=pd.read_table(tsv_file,sep='\t')
# csv_table.to_csv('CES_data_csv.csv',index=False)


data = pd.read_csv("CES_data_csv.csv")
data.columns = data.columns.str.replace(" ", "")
data['id'] = data.series_id.str.slice(start=3, stop=5)


dict_df = {}
for unique_id in data.id.unique():
    dict_df[unique_id] = data[data.id == unique_id]

#print(dict_df)
pickle_file1 = 'supersector_dict'
outfile = open(pickle_file1, 'wb')
pickle.dump(dict_df, outfile)
outfile.close()
