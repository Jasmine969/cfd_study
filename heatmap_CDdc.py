import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt, colors
from scipy import io as sio


def comp_heatmap(ax):
    plt.rc('font', family='Times New Roman', size=15)
    plt.subplots_adjust(left=0.05, right=1)
    norm = colors.LogNorm()
    with sns.axes_style('white'):
        ax = sns.heatmap(
            data, ax=ax, vmax=.3,
            annot=True, fmt='.3e',
            annot_kws=font_annot,
            norm=norm,
            xticklabels=np.arange(0, 1.01, 0.1).round(1).astype(str),
            yticklabels=[0.5, 1, 2, 3, 5, 7, 10, 15, 20],
            cbar=False,
            cmap='RdYlGn'
        )
    cbar = ax.figure.colorbar(ax.collections[0])
    cbar.set_label('RMSE', fontdict=font_text)
    ax.set_xlabel(r'$\alpha_{\mathrm{DC}}$', fontdict=font_formula)
    ax.set_ylabel(r'$P_\Delta$', fontdict=font_formula)
    return ax


font_formula = {'math_fontfamily': 'cm', 'size': 22}
font_text = {'size': 22, 'fontfamily': 'Times New Roman'}
font_annot = {'size': 17, 'fontfamily': 'Times New Roman'}
font_tick = {'size': 18, 'fontfamily': 'Times New Roman'}
fig, axes = plt.subplots()
data = sio.loadmat('E:\\MATLAB_code_local\\NHT\\chap5\\RMSE_CDdc.mat')
data = data['error'].T
base_pos, base_neg = 5, 1.1
frac_b = 1.5
ax = comp_heatmap(axes)
fig.set_size_inches([15.36, 7.57])
plt.show()
