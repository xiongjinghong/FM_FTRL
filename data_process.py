# 数据转换成alphafm需要的格式
filePath=r"C:\Users\XXX\Downloads\train\train.csv"
p_D = 22
D = 2 ** p_D
hashSalt = "salty"
from FM_FTRL_machine import data
for t, date, ID, x, label in  data(filePath, D, hashSalt):
    features = []
    for j,value in enumerate(x):
        features.append(f"f_{value}:{1}")
    line =  f"{int(label)} " + " ".join(features) + "\n"
    with open('data/'+str(date), 'a') as f:
         f.write(line)
    if t%1000000==0:
        print(t)
