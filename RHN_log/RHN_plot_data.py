#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([1.935,1.856,1.854,1.865,1.829,1.841,1.820,1.804,1.794,1.782])
y2 = np.array([1.656,1.681,1.669,1.672,1.663])
y3 = np.array([1.588,1.661,1.633,1.590,1.633,1.644])
y4 = np.array([1.530,1.592,1.593,1.595,1.601])
y5 = np.array([3.437,2.812,2.453,2.211,2.016])

# red dashes, blue squares and green triangles
with plt.style.context(('seaborn')):
    plt.plot(np.arange(1,len(y1)+1), y1, label='Dataset 1 Perplexity')
    plt.plot(np.arange(1,len(y2)+1), y2, label='Dataset 2 Perplexity')
    plt.plot(np.arange(1,len(y3)+1), y3, label='Dataset 3 Perplexity')
    plt.plot(np.arange(1,len(y4)+1), y4, label='Dataset 4 Perplexity')
    plt.plot(np.arange(1,len(y5)+1), y5, label='PTB Perplexity')

    # plt.tick_params(labelsize='large', width=5)
    # plt.grid(True)
    # plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    # plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    # ax = plt.axes()
    # ax.set_xlim(1, len(y1))
    # ax.set_xlabel('Number of Epochs', fontsize=15)
    # ax.set_ylabel('Perplexity in bpc', fontsize=15)
    # lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=1, numpoints=1) 
    # plt.savefig('rhn_perplexity', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()