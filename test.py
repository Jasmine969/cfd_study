import matplotlib.pyplot as plt
from fipy import CellVariable, Grid1D, DiffusionTerm, \
    ExponentialConvectionTerm, Viewer, CentralDifferenceConvectionTerm, \
    UpwindConvectionTerm, HybridConvectionTerm, PowerLawConvectionTerm
from fipy.tools import numerix

diffCoeff = 0.1
convCoeff = (0.1,)
L = 1.
nx = 5
mesh = Grid1D(dx=L / nx, nx=nx)

valueLeft = 1.
valueRight = 0.

var = CellVariable(mesh=mesh, name="variable")
var.constrain(valueLeft, mesh.facesLeft)
var.constrain(valueRight, mesh.facesRight)

eq = (DiffusionTerm(coeff=diffCoeff)
      + CentralDifferenceConvectionTerm(coeff=convCoeff))
eq.solve(var=var)

axis = 0
x = mesh.cellCenters[axis]
# 求解析解
CC = 1. - numerix.exp(-convCoeff[axis] * x / diffCoeff)
DD = 1. - numerix.exp(-convCoeff[axis] * L / diffCoeff)
analyticalArray = CC / DD
print(var.allclose(analyticalArray))

viewer = Viewer(vars=var)
viewer.plot()
plt.show(block=True)
