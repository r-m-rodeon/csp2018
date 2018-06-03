import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imread

'''
# Part 1
import csv

x = []
y = []

with open('museum_visitors.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Museum Attendance')
'''


x, y = np.loadtxt('museum2.txt', delimiter= ',', unpack=True)
plt.plot(x,y, color='black', linewidth=3, label='Museum Attendance')


img = imread("lights.jpg")
plt.imshow(img, extent=[1976,2019,30.5000,90.5000])


plt.xlabel('Year Recorded')
plt.ylabel('Attendance')
plt.title('How has LA Museum attendance changed over the years?')
plt.legend()
plt.xlim(1978,2018)
plt.ylim(30.5000,90.5000)
plt.minorticks_on()
plt.yticks([30.5000,40.0000,50.0000,60.0000,70.0000,80.0000,90.0000],['300,000','400,000','500,000','600,000','700,000','800,000','900,000'])
plt.xticks([1980,1990,2000,2010,2017])
plt.grid(True)
plt.show()