#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([30.121,26.442,26.452,26.416,26.165,26.013,26.048,25.906,25.452,24.748,23.723,20.992,24.605,26.031,18.065,13.180,9.840,7.768,6.474,5.574,4.928,4.452,4.098,3.832,3.618,3.350,3.078,3.042,3.035,3.031,3.029,3.028,3.027,3.026,3.025])
y2 = np.array([38.660,29.835,29.632,29.634,29.616,29.540,29.533,29.593,29.562,29.565,29.514,29.596,29.470,29.585,19.135,13.344,9.946,7.807,6.378,5.377,4.663,4.148,3.769,3.491,3.282,3.122,2.940,2.705,2.669,2.663,2.660,2.658,2.657,2.656,2.655])
y3 = np.array([34.650,29.355,29.285,29.319,29.282,29.308,29.224,29.250,29.229,29.240,29.254,29.246,29.292,29.266,19.012,13.231,9.833,7.673,6.233,5.233,4.524,4.011,3.637,3.360,3.155,2.999,2.845,2.612,2.554,2.546,2.543,2.542,2.540,2.536,2.532])
y4 = np.array([40.074,40.151,33.373,29.155,29.077,29.057,29.041,29.042,29.064,29.021,29.003,29.009,29.037,29.033,18.892,13.175,9.778,7.616,6.176,5.179,4.470,3.960,3.571,3.297,3.091,2.931,2.779,2.571,2.507,2.498,2.494,2.491,2.490,2.488,2.487])
y5 = np.array([44.438,44.082,43.886,43.989,44.268,44.031,43.960,43.715,44.163,43.865,43.967,43.969,44.220,19.788,6.448,5.596,5.173,4.909,4.722,4.582,4.470,4.383,4.314,4.257,4.207,4.167,4.131,4.100,4.077,4.053,4.036,4.015,4.002,3.988,3.979])

# red dashes, blue squares and green triangles
with plt.style.context(('seaborn')):
    plt.loglog(np.arange(1,len(y1)+1), y1, label='Dataset 1 Perplexity')
    plt.loglog(np.arange(1,len(y2)+1), y2, label='Dataset 2 Perplexity')
    plt.loglog(np.arange(1,len(y3)+1), y3, label='Dataset 3 Perplexity')
    plt.loglog(np.arange(1,len(y4)+1), y4, label='Dataset 4 Perplexity')
    plt.loglog(np.arange(1,len(y5)+1), y5, label='PTB Perplexity')

    # plt.tick_params(labelsize='large', width=5)
    # plt.grid(True)
    # plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    # plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    # ax = plt.axes()
    # ax.set_xlim(1, len(y1))
    # ax.set_xlabel('Number of Epochs', fontsize=15)
    # ax.set_ylabel('Perplexity in bpc', fontsize=15)
    # lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=1, numpoints=1) 
    # plt.savefig('lstm_perplexity', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()