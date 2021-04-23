import os
import glob
import pandas as pd
#os.chdir("/dirname")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

writer = pd.ExcelWriter('newfile.xlsx', engine='xlsxwriter')

for i in all_filenames:
    df = pd.read_csv(i)        
    print(i[:-4])    
    df.to_excel(writer, sheet_name=i[:-4], index = False)
writer.save()
