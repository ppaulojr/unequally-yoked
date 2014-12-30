#!/usr/bin/env python
#
# Usage: ./uyf.py
#
# Dependency "Matplotlib"
#
# Don't Abuse Patheos server
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os, sys

# Helvetica-Neue is cooler than stock font
matplotlib.rc('font', family='sans-serif') 
matplotlib.rc('font', serif='Helvetica Neue') 

# Remove top and right axis
def simpleaxis(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

N=26                # Number of Chars
ind = np.arange(N)  # the x locations for the groups
width = 0.8         # the width of the bars

# Letter Frequency in Plain English Text
# Source Huffman Algorithm for English text compression.
letFreqEn = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,
             0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,
             6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074] 

# Read Input Text - TODO: Pass as a argv[]
# Create Frequency Array for the current text.txt
txt = "".join(open("text.txt","rt").readlines())
txt = txt.upper()                   # Remove Case Info
letFreq = [0 for i in xrange(N)]    # Init Array
for i in txt:
    idx = ord(i) - 65               # 65 is 'A' in ASCII
    if (idx >= 0 and idx < 26):
        letFreq[idx] += 1
letFreq = [100*float(i)/sum(letFreq) for i in letFreq] 

# create error bars
errDiff = [[(a_i - b_i),0] if ((a_i - b_i)>0) else [0,(b_i - a_i)] for a_i, b_i in zip(letFreqEn, letFreq)]
errDiff = map(list, zip(*errDiff)) # transpose matrix

#plot all using MatplotLib
fig, ax = plt.subplots() # Create Plot Area
# Create Vertical Bars
rects1 = ax.bar(ind, letFreq, width, align='center', color='#1EA1BE', edgecolor = "#4ED1EE", yerr=errDiff, ecolor='k')
ax.set_ylabel('Frequency %')    # Y-Axis Label
ax.set_title("Letter frequency Pope Francis's bookclub compared to English letter freq.") # Chart Title
ax.set_xticks(ind)
ax.set_xticklabels( [chr(65+i) for i in xrange(26)])
simpleaxis (ax)
plt.show()
