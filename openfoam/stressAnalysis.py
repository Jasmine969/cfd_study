from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def rmse(y, t):
    return np.sqrt(np.mean((y - t) ** 2))


path1 = 'F:\\openfoam\\plateHole_series\\plateHole\\'
path2 = 'F:\\openfoam\\plateHole_series\\plateHoleFine\\'
path3 = 'F:\\openfoam\\plateHole_series\\plateGrade\\'
path4 = 'F:\\openfoam\\plateHole_series\\plateLarge\\'
filename = 'postProcessing\\graphUniform\\100\\line_sigmaxx.xy'
data1 = pd.read_table(path1 + filename, header=None, names=['y', 'sigmaxx'])
data2 = pd.read_table(path2 + filename, header=None, names=['y', 'sigmaxx'])
data3 = pd.read_table(path3 + filename, header=None, names=['y', 'sigmaxx'])
data4 = pd.read_table(path4 + filename, header=None, names=['y', 'sigmaxx'])
# yy = np.linspace(data4.iloc[0, 0], data4.iloc[-1, 0], 500)
r1 = 0.5
r2 = 50
sigmaxx_ana1 = 1e4 * (1 + r1 ** 2 / 2 / data1['y'] ** 2 + 3 * r1 ** 4 / 2 / data1['y'] ** 4)
sigmaxx_ana2 = 1e4 * (1 + r2 ** 2 / 2 / data4['y'] ** 2 + 3 * r2 ** 4 / 2 / data4['y'] ** 4)
plt.figure(1)
plt.plot(data1['y'], data1['sigmaxx'], 'C0', label='coarse')
plt.plot(data1['y'], sigmaxx_ana1, 'C2', label='analytical')
plt.title(rmse(data1['sigmaxx'], sigmaxx_ana1))
# plt.plot(data2['y'], data2['sigmaxx'], 'C1', label='fine')
# plt.plot(data3['y'], data3['sigmaxx'], 'C2', label='grade')
plt.figure(2)
plt.plot(data4['y'], data4['sigmaxx'], 'C3', label='large')
plt.plot(data4['y'], sigmaxx_ana2, 'C4', label='analytical')
plt.title(rmse(data4['sigmaxx'], sigmaxx_ana2))
plt.legend(loc='best')
plt.show()
