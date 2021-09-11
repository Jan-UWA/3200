import math 
from mpmath import *
from scipy import interpolate
import numpy as np
import random
import csv
#2 4 6 20 40 60
t0 = 20
T_hat2 = np.array([2.22680814, 2.27603123, 2.33681247, 2.40552142, 2.4640043,  2.53888546,
 2.61964172, 2.68920892, 2.77651961, 2.87208574, 2.95761181, 3.06483932,
 3.17943047, 3.28330412, 3.42134852, 3.56487567, 3.71937857, 3.86079041,
 4.05060908, 4.25335118, 4.43775336, 4.68308841, 4.95732921, 5.22465983,
 5.58337317])

da_hat2 = np.array([1.04590997, 1.11357031, 1.25380993, 1.32194105, 1.4733614,  1.68129898,
 1.89451625, 2.17484146, 2.52752171, 3.03236085, 3.87914142, 5.5115418,
 8.70704097, 9.61813713, 8.56102501, 6.15520409, 4.96022204, 5.17158264,
 5.23630445, 3.03923164, 1.15135012, 0.48525671, 0.18955363, 0.1179105,
 0.06587606])

tu_hat = 10.452148768346103
tl_hat = 6.968099178897402

T_hat_new  = np.arange(tl_hat,tu_hat,0.01) # not inclusive of last value

f = interpolate.interp1d(T_hat2, da_hat2, kind = 'linear', fill_value = 'extrapolate')
da_hat_new = f(T_hat_new)

lambda1 = np.array([1.5784,
    1.6489,
    1.7382,
    1.8419,
    1.9326,
    2.0518,
    2.1844,
    2.3019,
    2.4537,
    2.6253,
    2.7837,
    2.9886,
    3.2151,
    3.4269,
    3.7174,
    4.0294,
    4.3753,
    4.6997,
    5.1443,
    5.6277,
    6.0720,
    6.6664,
    7.3309,
    7.9757,
    8.8330])

lambda2 = lambda1.tolist()
lambda2.insert(0, 'lambda')

data_list = []
t = 5
SA = ['SA',2, t]

file_name = "alves"
path = "Graphs/{0}.csv".format(file_name)


"""with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data_list)"""

filename = "/Users/simonluong/coding/Wave-Energy-Convertor/Data/Alves_2010.csv"
filename = filename.split("/")[-1].split(".")[0]