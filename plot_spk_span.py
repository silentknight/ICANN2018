#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from matplotlib.figure import Figure

# # Dataset PTB
# y1 = np.array([1.951,1.920,1.862,1.833,1.652,1.582,1.549,1.532,1.522,1.517,1.514,1.513,1.513,1.512,1.512,1.512,1.512,1.512,1.512,1.512])
# y2 = np.array([3.328,2.322,1.886,1.758,1.690,1.642,1.608,1.581,1.560,1..537,1.524,1.507,1.495,1.485,1.474,1.460,1.458,1.445,1.438,1.433,1.426,1.421,1.417,1.414,1.411,1.404,1.400,1.392,1.397,1.389,1.392,1.382,1.378,1.376,1.372,1.371,1.368,1.363,1.368,1.364,1.356,1.353,1.353,1.350,1.347,1.347,1.349,1.344,1.340,1.340])
# y3 = np.array([3.395,2.786,2.438,2.185,1.995,1.889,1.802,1.750,1.708,1.660,1.629,1.597,1.575,1.562,1.532,1.520,1.511,1.494,1.484,1.472,1.462,1.447,1.434,1.428,1.418,1.412,1.405,1.398,1.394,1.388,1.380,1.372,1.360,1.360,1.356,1.349,1.343,1.336,1.339,1.330,1.327,1.325,1.320,1.318,1.316,1.311,1.309,1.309,1.310,1.301])
# y4 = np.array([2.03737,1.78536,1.68342,1.62017,1.58123,1.54640,1.51815,1.49652,1.48271,1.47021,1.45360,1.45414,1.44045,1.42687,1.43907,1.41865,1.41513,1.40777,1.39542,1.39670,1.41069,1.39256,1.39808,1.38736,1.39524,1.40657,1.38937,1.40214,1.39485,1.38843,1.38908,1.39172,1.38764,1.39171,1.39544,1.39460,1.40500,1.40674,1.41126,1.41762,1.41199,1.38509,1.40777,1.38842,1.41132,1.40277,1.39586,1.39956,1.43733,1.42642])
# y5 = np.array([1.780,1.607,1.530,1.489,1.458,1.430,1.430,1.418,1.410,1.418,1.393,1.413,1.415,1.445,1.426,1.420,1.439,1.435,1.416,1.449,1.471,1.492,1.489,1.471,1.534])


# # Dataset WikiText 2
# y1 = np.array([2.087,2.042,2.000,1.949,1.819,1.752,1.716,1.694,1.680,1.671,1.666,1.663,1.661,1.660,1.660,1.660,1.660,1.660,1.660,1.660]) #1.648
# y2 = np.array([])
# y3 = np.array([])
# y4 = np.array([])
# y5 = np.array([])

# # LSTM
# y1 = np.array([2.659,2.612,2.601,2.615,1.889,1.598,1.595,1.595,1.594,1.593])
# y2 = np.array([2.837,2.564,2.792,2.690,1.813,1.513,1.416,1.413,1.412,1.412])
# y3 = np.array([2.712,2.680,2.694,2.584,1.745,1.479,1.349,1.342,1.341,1.340])
# y4 = np.array([2.671,2.628,2.802,2.731,1.792,1.388,1.327,1.318,1.319,1.317])
# y5 = np.array([2.572,2.619,2.626,2.612,1.696,1.389,1.308,1.307,1.305,1.305])
# y6 = np.array([2.675,2.668,2.666,2.667,1.714,1.386,1.301,1.301,1.301,1.301])

# AWD-LSTM
# y1 = np.array([1.624,1.600,1.594,1.606,1.599,1.600,1.593,1.594,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593,1.593])
# y2 = np.array([1.413,1.413,1.410,1.407,1.408,1.406,1.395,1.404,1.414,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393,1.393])
# y3 = np.array([1.350,1.346,1.348,1.346,1.344,1.345,1.346,1.346,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344,1.344])
# y4 = np.array([1.318,1.319,1.321,1.322,1.322,1.321,1.320,1.321,1.321,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319,1.319])
# y5 = np.array([1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305,1.305])
# y6 = np.array([1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300,1.300])

# # RHN
# y1 = np.array([1.923,1.878,1.878,1.831,1.838,1.820,1.795,1.775,1.774,1.775,1.760,1.744,1.733,1.737,1.724,1.706,1.716,1.697,1.697,1.693])
# y2 = np.array([1.656,1.682,1.675,1.651,1.689,1.688,1.646,1.648,1.634,1.624,1.604,1.586,1.564,1.566,1.564,1.550,1.541,1.548,1.534,1.527])
# y3 = np.array([1.621,1.624,1.579,1.632,1.607,1.604,1.601,1.580,1.670,1.533,1.524,1.515,1.558,1.503,1.487,1.509,1.465,1.470,1.474,1.449])
# y4 = np.array([1.603,1.607,1.660,1.840,1.592,1.540,1.590,1.544,1.524,1.502,1.496,1.501,1.507,1.486,1.487,1.453,1.471,1.458,1.457,1.437])
# y5 = np.array([1.590,1.576,1.598,1.581,1.576,1.564,1.533,1.534,1.528,1.511,1.505,1.487,1.493,1.474,1.467,1.435,1.442,1.440,1.429,1.422])
# y6 = np.array([1.600,1.603,1.544,1.604,1.595,1.583,1.569,1.555,1.576,1.525,1.525,1.502,1.502,1.509,1.484,1.469,1.467,1.453,1.451,1.442])

# # Transformer-XL
# y1 = np.array([1.596,1.594,1.594,1.593,1.596,1.593,1.594,1.594,1.594,1.594])
# y2 = np.array([1.422,1.422,1.422,1.422,1.422,1.422,1.422,1.422,1.422,1.422])
# y3 = np.array([1.391,1.381,1.381,1.381,1.381,1.381,1.381,1.381,1.381,1.381])
# y4 = np.array([1.320,1.320,1.320,1.320,1.320,1.320,1.320,1.320,1.320,1.320])
# y5 = np.array([1.315,1.315,1.315,1.315,1.315,1.315,1.315,1.315,1.315,1.315])
# y6 = np.array([1.310,1.310,1.310,1.310,1.310,1.310,1.310,1.310,1.310,1.310])

# # Transformer-XL Large
# y1 = np.array([1.998,1.998,1.998,1.998,1.998,1.998,1.998,1.998,1.998,1.998])
# y2 = np.array([1.688,1.688,1.688,1.688,1.688,1.688,1.688,1.688,1.688,1.688])
# y3 = np.array([1.587,1.587,1.587,1.587,1.587,1.587,1.587,1.587,1.587,1.587])
# y4 = np.array([1.529,1.529,1.529,1.529,1.529,1.529,1.529,1.529,1.529,1.529])
# y5 = np.array([1.500,1.500,1.500,1.500,1.500,1.500,1.500,1.500,1.500,1.500])
# y6 = np.array([1.486,1.486,1.486,1.486,1.486,1.486,1.486,1.486,1.486,1.486])

with plt.style.context(('seaborn')):
    # plt.plot(np.arange(1,len(y1)+1), y1, label='Long Short-Term Memory')
    # plt.plot(np.arange(1,len(y3)+1), y3, label='ASGD Weight-Dropped LSTM')
    # plt.plot(np.arange(1,len(y2)+1), y2, label='Recurrent Highway Network')
    # plt.plot(np.arange(1,len(y4)+1), y4, label='Transformer-XL (14M)')
    # plt.plot(np.arange(1,len(y5)+1), y5, label='Transformer-XL (41M)')

    plt.plot(np.arange(1,len(y1)+1), y1, label='SP2, L=20')
    plt.plot(np.arange(1,len(y2)+1), y2, label='SP2, L=100')
    plt.plot(np.arange(1,len(y3)+1), y3, label='SP2, L=200')
    plt.plot(np.arange(1,len(y4)+1), y4, label='SP2, L=500')
    plt.plot(np.arange(1,len(y5)+1), y5, label='SP2, L=5000')
    plt.plot(np.arange(1,len(y6)+1), y6, label='SP2, L=10000')

    plt.tick_params(labelsize='large', width=5)
    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-.', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle=':', linewidth='0.2', color='grey')
    plt.xlim(1, len(y7))
    plt.ylim(1, 4.5)
    plt.xlabel('Number of Epochs', fontsize=15)
    plt.ylabel('Perplexity of the Model, bpc', fontsize=15)
    lgd = plt.legend(loc='upper right', shadow=True, fancybox=True, numpoints=1, prop={'size': 12})
    ax = plt.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.savefig('perplexity_PTB', bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()
