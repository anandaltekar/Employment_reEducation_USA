import os
import pandas
import pickle
from RBDA_project_dataClean import pickle_file2


infile = open(pickle_file2, 'rb')
allDatasets = pickle.load(infile)
infile.close()

output_path = 'allDatasets'

for index, dataset in enumerate(allDatasets):
    dataset.to_csv
    filepath = os.path.join(output_path, 'dataset_'+str(index)+'.csv')
    dataset.to_csv(filepath)
