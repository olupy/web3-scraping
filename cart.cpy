import os
import glob
import pandas as pd
os.chdir("C:/Users/biodun/.vscode/python")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "web3fundings.csv", index=False, encoding='utf-8-sig')
            

