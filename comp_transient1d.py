from scipy import io as sio
from matplotlib import pyplot as plt
import numpy as np

py_data = np.load('transient1d_ret.npz', allow_pickle=True)
py_ret = py_data['arr_0']
pos, time_point, py_ret = py_ret
mat_data = sio.loadmat('E:\\MATLAB_code_local\\NHT\\chap5\\transient1d_phi_ret.mat')
mat_implicit = mat_data['phi_implicit'].T
mat_CN = mat_data['phi_CN'].T
mat_explicit = mat_data['phi_explicit'].T
fig2, ax2 = plt.subplots(3, 3, sharex='all', sharey='row')
steps = mat_CN.shape[0]
for ind, tp in enumerate(time_point):
    interval = steps // 3 ** 2 + 1
    if ind % interval == 0:
        r, c = divmod(ind // interval, 3)
        ax2[r, c].plot(pos[ind], py_ret[ind], '.--', label='FiPy')
        ax2[r, c].plot(pos[ind], mat_implicit[ind], 'o-', label='implicit')
        ax2[r, c].plot(pos[ind], mat_CN[ind], '*-',label='CN')
        ax2[r, c].plot(pos[ind], mat_explicit[ind],'s-', label='explicit')
        ax2[r, c].set_title(f'{tp[0]} s')
handles, labels = ax2[0, 0].get_legend_handles_labels()
fig2.legend(handles, labels, loc='upper right', prop={'size': 18})
plt.show()