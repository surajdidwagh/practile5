import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fp=open("testmarks1.csv","r")
data=fp.read()
lines=data.splitlines()
x_rno=[]
y_eds_marks=[]

for line in lines:
    word=line.split(',')
    if(word[0].isdigit() or word[1].isdigit()):
        x_rno.append(word[0])
        y_eds_marks.append(word[0])

print(y_eds_marks)

plt.plot(x_rno,y_eds_marks)
plt.show()
plt.xlabel("Roll NO")
plt.xlabel("Marks")
plt.xlabel("ET ")
