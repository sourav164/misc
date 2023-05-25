import pandas as pd
import os, glob

os.chdir(r"C:\Users\sourav\Desktop\test")
raw_files = glob.glob("*csv")

# user inputs
start_time = "2023-05-19-16-48-30"
drop_cells = 500

data_lists = []
devices = []

data = pd.DataFrame() 
for raw_file in raw_files:
    devices.append(raw_file[:-4])
    df = pd.read_csv(raw_file)
    time_data = df["Timestamp"].tolist()
    index = [idx for idx, s in enumerate(time_data) if start_time in s][0]
    print (index)
    data_lists.append(df["Acc_Z(m/s^2)"][index:].tolist()) 
    
low_val =min([len(data_list) for data_list in data_lists])
for i in range(len(data_lists)):
    data[devices[i]] = data_lists[i][:low_val]
data.drop(data.tail(drop_cells).index, inplace = True) # remove last 5 sececonds
data.to_csv("results.csv")
