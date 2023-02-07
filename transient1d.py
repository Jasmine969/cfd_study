from fipy import Grid1D, CellVariable, \
    DiffusionTerm, HybridConvectionTerm, TransientTerm, Viewer, ConvectionTerm
from fipy.tools import numerix
from matplotlib import pyplot as plt
import gmsh
import matplotlib
import time
from tqdm import tqdm
from mpl_toolkits import mplot3d
from matplotlib import cm

diffCoeff = 0.1  # 扩散系数
convCoeff = (-0.1,)  # 流速
Lx = 2.  # 长度

nx = 10  # 节点数
mesh = Grid1D(dx=Lx / nx, nx=nx)  # 一维网格

phi = CellVariable(mesh=mesh, value=numerix.linspace(-1, 3, nx), hasOld=1, name='phi')

valueLeft = 1
valueRight = 0
phi.constrain(valueLeft, mesh.facesLeft)
phi.constrain(valueRight, mesh.facesRight)

eqn = TransientTerm() + HybridConvectionTerm(coeff=convCoeff) == DiffusionTerm(coeff=diffCoeff)
# timeStepDuration = 10 * 0.9 * (Lx / nx) ** 2 / (2 * diffCoeff)
timeStepDuration = 0.05
steps = 100
time_point = []
result = []
for step in tqdm(range(steps)):
    phi.updateOld()
    eqn.solve(var=phi,
              dt=timeStepDuration)
    time_point.append(((step + 1) * timeStepDuration).__round__(2))
    result.append(phi.value.copy())
    # viewer = Viewer(vars=phi,title=time_point[-1])
    # viewer.plot()
    # plt.show(block=True)
    # time.sleep(0.1)
    # plt.close()
result = numerix.asarray(result)
pos, time_point = numerix.meshgrid(mesh.x.value, time_point)
ax1 = plt.axes(projection='3d')
fig2, ax2 = plt.subplots(3, 3, sharex='all', sharey='row')
plt.subplots_adjust(hspace=0.2)
colors = cm.get_cmap('jet')
color_vals = numerix.linspace(0, 1, steps)
for ind, tp in enumerate(time_point):
    ax1.plot(pos[ind], tp, result[ind], color=colors(color_vals[ind]))
    interval = steps // 3 ** 2 + 1
    if ind % interval == 0:
        r, c = divmod(ind // interval, 3)
        ax2[r, c].plot(pos[ind], result[ind])
        ax2[r, c].set_title(f'{tp[0]} s')
ax1.set_xlabel('x')
ax1.set_ylabel('t')
ax1.set_zlabel(r'$\phi$')
numerix.savez('transient1d_ret', [pos, time_point, result])
plt.show()
