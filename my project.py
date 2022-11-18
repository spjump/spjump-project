import matplotlib as mpl 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt 
 
import json
import time
import sys
#4 moon phases
phases=['New Moon', 'First Quarter', 'Full Moon', 'Third Quarter']
list=phases



columns = ['New Moon', 'First Quarter', 'Third Quarter', 'Full Moon']
df = pd.read_csv(r'C:\Users\spjum_000\OneDrive\Desktop\My Repo\moon-phases\moon-phase 2021.csv', usecols=columns)
print("Contents in csv file:", df)


print(list)
print('What moon phase do you like?')
plt.plot(df.'New Moon', df.'First Quarter', df.'Full Moon')

plt.show()