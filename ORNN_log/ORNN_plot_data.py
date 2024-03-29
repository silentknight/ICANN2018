#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([6.51120015417,2.65914440874,2.59454459157,2.58470486614,2.58140266172,2.57990662227,2.57892127583,2.57834224435,2.57783726623,2.57759839973,2.57740764922,2.57717077275,2.57702959255,2.57691047997,2.57682406264,2.57676199094])
y2 = np.array([6.53032148291,2.64896653676,2.57818493391,2.56855529958,2.56557452115,2.56409838813,2.5633282519,2.56277365255,2.56249119346,2.56217680236,2.56198914228,2.56177684816,2.56163279526,2.56148383059,2.56139645164,2.56131801864])
y3 = np.array([5.11934803701,2.67442004202,2.63960259999,2.61807523318,2.60191561519,2.58979906098,2.57936218149,2.56890768442,2.55497120229,2.5290137239,2.50604907109,2.49533581364,2.49091413328,2.48875113479,2.48731832162,2.48628515236])
y4 = np.array([4.73292420122,2.69912066855,2.66913336903,2.65452055116,2.63780068143,2.62209454667,2.61135158167,2.60103370173,2.58941784675,2.57642351314,2.56054390583,2.53966555209,2.51975815704,2.50772758118,2.50087876287,2.49645036566])
y5 = np.array([42.4321422241,30.7374137611,24.6913149474,22.003735207,20.8540602145,20.1897453952,19.7055022284,19.3026203375,18.9443261163,18.6203592587,18.3139203446,18.0198727078,17.7344910266,17.4557096949,17.1805124624,16.9086134704])

# red dashes, blue squares and green triangles
with plt.style.context(('seaborn')):
    plt.loglog(np.arange(1,len(y1)+1), y1, label='Dataset 1 Perplexity')
    plt.loglog(np.arange(1,len(y2)+1), y2, label='Dataset 2 Perplexity')
    plt.loglog(np.arange(1,len(y3)+1), y3, label='Dataset 3 Perplexity')
    plt.loglog(np.arange(1,len(y4)+1), y4, label='Dataset 4 Perplexity')
    plt.loglog(np.arange(1,len(y5)+1), y5, label='PTB Perplexity')

    plt.tick_params(labelsize='large', width=5)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax = plt.axes()
    ax.set_xlim(1, len(y1))
    ax.set_xlabel('Number of Epochs', fontsize=15)
    ax.set_ylabel('Perplexity in bpc', fontsize=15)
    lgd = ax.legend(loc='lower left', shadow=True, fancybox=True, ncol=1, numpoints=1, prop={'size': 12})
    plt.savefig('ornn_perplexity', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
