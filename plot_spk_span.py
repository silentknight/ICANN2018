#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# # Dataset SP2 20
# y1 = np.array([2.659,2.612,2.601,2.615,1.889,1.598,1.595,1.595,1.594,1.593])
# y2 = np.array([1.923,1.878,1.878,1.831,1.838,1.820,1.795,1.775,1.774,1.775,1.760,1.744,1.733,1.737,1.724,1.706,1.716,1.697,1.697,1.693])
# y3 = np.array([1.624,1.600,1.594,1.606,1.599,1.600,1.593,1.594,1.593,1.593])
# y4 = np.array([3.997,3.995,3.998,3.996,3.996,3.996,3.996,3.996,3.996,3.996])

# Dataset SP2 100
y1 = np.array([2.837,2.564,2.792,2.690,1.813,1.513,1.416,1.413,1.412,1.412])
y2 = np.array([1.656,1.682,1.675,1.651,1.689,1.688,1.646,1.648,1.634,1.624,1.604,1.586,1.564,1.566,1.564,1.550,1.541,1.548,1.534,1.527])
y3 = np.array([1.413,1.413,1.410,1.407,1.408,1.406,1.395,1.404,1.414,1.393])
y4 = np.array([3.219,3.217,3.217,3.219,3.218,3.217,3.217,3.218,3.217,3.217])

# # Dataset SP2 200
# y1 = np.array([2.712,2.680,2.694,2.584,1.745,1.479,1.349,1.342,1,341,1.340])
# y2 = np.array([])
# y3 = np.array([1.350,1.346,1.348,1.346,1.344,1.345,1.346,1.346,1.344,1.344])
# y4 = np.array([2.996,2.997,3.002,2.997,2.995,2.995,2.997,2.996,2.995,2.995])

# # Dataset SP2 500
# y1 = np.array([2.671,2.628,2.802,2.731,1.792,1.388,1.327,1.318,1.319,1.317])
# y2 = np.array([])
# y3 = np.array([1.318,1.319,1.321,1.322,1.322,1.321,1.320,1.321,1.321,1.319])
# y4 = np.array([2.899,2.892,2.896,2.892,2.893,2.892,2.892,2.891,2.891,2.891])

# # Dataset PTB
# y1 = np.array([1.961,1.928,1.860,1.805,1.790,1.776,1.756,1.742,1.744,1.722,1.606,1.561,1.539,1.527,1.520,1.517,1.516,1.515,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514,1.514])
# y2 = np.array([3.369,])
# y3 = np.array([3.328,2.322,1.886,1.758,1.690,1.642,1.608,1.581,1.560,1.537,1.524,1.507,1.495,1.485,1.474,1.460,1.458,1.445,1.438,1.433,1.426,1.421,1.417,1.414,1.411,1.404,1.400,1.392,1.397,1.389])
# y4 = np.array([])


with plt.style.context(('seaborn')):
    plt.loglog(np.arange(1,len(y1)+1), y1, label='Long Short-Term Memory')
    plt.loglog(np.arange(1,len(y3)+1), y3, label='ASGD Weight-Dropped LSTM')
    plt.loglog(np.arange(1,len(y2)+1), y2, label='Recurrent Highway Network')
    plt.loglog(np.arange(1,len(y4)+1), y4, label='Transformer-XL')

    plt.tick_params(labelsize='large', width=5)
    plt.grid(True)
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    ax = plt.axes()
    ax.set_xlabel('Number of Epochs', fontsize=15)
    ax.set_ylabel('Perplexity of the Model, bpc', fontsize=15)
    lgd = ax.legend(loc='upper right', shadow=True, fancybox=True, ncol=2, numpoints=1, prop={'size': 12})
    plt.savefig('peplexity_sp2_100', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
