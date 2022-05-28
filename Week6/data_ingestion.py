""""
Importing the libraries and the config file
"""
import testutility as util
import time
import dask.dataframe as dd
import sys
import os
config_data = util.read_config_file("config.yaml")
file_type = config_data['file_type']
filename = "./" + config_data['file_name'] + f'.{file_type}'
file_size = str(os.stat("./" + config_data['file_name'] + f'.{file_type}').st_size)
"""
Reading the csv file using dask
"""
start = time.time()
df = dd.read_csv(filename)
end = time.time()
print("Read csv with dask: ", (end-start), "sec")

"""
Performing column validation
"""

util.col_header_val(df, config_data)
print("columns of files are:{}", df.read())
print("Expected columns from YAML are:{}", config_data['columns'])

"""
Carrying out an action based on the outcome of column validation
"""

if util.col_header_val(df, config_data) == 0:
    print("column validation failed. please check the input and yaml files")
    sys.exit()
else:
    print("column validation passed")
    df.to_csv(config_data['file_name']+f'.{file_type}', index=False, sep=config_data['outbound_delimiter'])
    shape = df.shape
    summary = open('summary.txt', 'w')
    summary.write('Total number of rows: ')
    summary.write(shape[0])
    summary.write('\nTotal number of columns: ')
    summary.write(shape[1])
    summary.write('\nFile size: ')
    summary.write(file_size)
    summary.write(' bytes')
    summary.close()
