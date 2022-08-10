import symforce
symforce.set_symbolic_api("sympy")
import symforce.symbolic as sf
import sympy as sp
from sympy import S


p = sf.V2.symbolic('p')
theta = sf.Symbol('theta')

r1 = sf.Symbol('r1'); alpha1 = sf.Symbol('alpha1')
r2 = sf.Symbol('r2'); alpha2 = sf.Symbol('alpha2')

o = sf.Pose2_SE2()
a = o.compose(sf.Pose2_SE2(sf.Rot2.from_angle(alpha1), sf.V2()))
a = a.compose(sf.Pose2_SE2(sf.Rot2(), sf.V2(r1,0)))
b = a.compose(sf.Pose2_SE2(sf.Rot2.from_angle(alpha2), sf.V2()))
b = b.compose(sf.Pose2_SE2(sf.Rot2(), sf.V2(r2,0)))

print(f'b.t = {b.t.simplify()}')
print(f'b.R = {b.R.to_rotation_matrix().simplify()}')

Eq1 = sp.Eq(p[0],b.t[0]).expand(trig = True)
Eq2 = sp.Eq(p[1],b.t[1]).expand(trig = True)
system = [Eq1,Eq2]

# solution = sp.solve([Eq1,Eq2],[alpha1,alpha2])
solution = sp.nonlinsolve(system,[alpha1,alpha2])
print(solution)
print('done')
