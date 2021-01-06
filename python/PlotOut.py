'''
读取IMD生成的文件并绘图
'''
#import numpy as npy
import matplotlib.pyplot as plt

fileIMD=r"130 10"
#* 在这里标记要读取的IMD文件

fp = open(fileIMD, "r")

l=[] # 波长lambda
Rs=[] # 反射率R
Rp=[]
for line in fp:
    if line[0]!=";": # 找到不以「;」开头的行
        line=line[:-1]
        lines=line.split(" ")
        lines=[lines[i] for i in range(0,len(lines)) if lines[i]!=""]
        l.append(lines[0])
        Rs.append(lines[2])
        Rp.append(lines[3])
fp.close()

lines = plt.plot(l, Rs, color='green', lw=2)
linep = plt.plot(l, Rp, color='blue', lw=2)
plt.ylabel("R")
plt.xlabel("theta (unit:deg)")
fileFig=fileIMD+".jpg"
plt.savefig(fileFig)
