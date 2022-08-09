import symforce.symbolic as sf
import sympy as sp
import math as m
from exp_rots import exp_roll

''' 
       a
      /|\            |y
     / |r\           |___x
    /  |  \ 
   /   o   \
b /____|____\ c


'''
roll = sf.Symbol('roll')
pitch = sf.Symbol('pitch')
yaw = sf.Symbol('yaw')

a2 = sf.Pose3(sf.Rot3.from_yaw_pitch_roll(yaw, pitch, roll), sf.V3(0, 0, 0))

#To continue....

#base storey
r = sf.Symbol('r')
o_base = sf.Pose3()
a0 = o_base.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(sf.pi/2,0,0), #90 degrees
                        sf.V3(0, r, 0)))
b0 = o_base.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(sf.pi *(1 +1/6),0,0), #210 degrees
                        sf.V3(-r * sf.sin(sf.pi/3), -r * sf.cos(sf.pi/3), 0))) #60 degrees
c0 = o_base.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(-sf.pi/6,0,0), #-30 degrees
                        sf.V3(r * sf.sin(sf.pi/3), -r * sf.cos(sf.pi/3), 0)))


#first storey frames
l0 = sf.Symbol('l0')
qa0 = sf.Symbol("qa0")
qb0 = sf.Symbol("qb0")
qc0 = sf.Symbol("qc0")

_, a_0_R_1 = exp_roll(qa0)
_, b_0_R_1 = exp_roll(qb0)
_, c_0_R_1 = exp_roll(qc0)
a_0_t_1 = sf.Matrix44.eye(); a_0_t_1[:3,3] = sf.V3(0,l0,0)
b_0_t_1 = sf.Matrix44.eye(); b_0_t_1[:3,3] = sf.V3(0,l0,0)
c_0_t_1 = sf.Matrix44.eye(); c_0_t_1[:3,3] = sf.V3(0,l0,0)
a_0_T_1 =  a_0_R_1 * a_0_t_1
b_0_T_1 =  b_0_R_1 * b_0_t_1
c_0_T_1 =  c_0_R_1 * c_0_t_1

a1 = a0.to_homogenous_matrix() * a_0_T_1
b1 = b0.to_homogenous_matrix() * b_0_T_1
c1 = c0.to_homogenous_matrix() * c_0_T_1


#second storey frames - assume all joints are at 90 degrees
l1 = sf.Symbol('l1')
qa1 = sf.Symbol("qa1")
qb1 = sf.Symbol("qb1")
qc1 = sf.Symbol("qc1")

roll90 = sf.Matrix44.eye(); roll90[:3,:3] = sf.Rot3.from_yaw_pitch_roll(0,0,sf.pi/2).to_rotation_matrix()
# _, a_1_R_2 = exp_roll(qa1)
# _, b_1_R_2 = exp_roll(qb1)
# _, c_1_R_2 = exp_roll(qc1 + sf.pi/2)
a_1_t_2 = sf.Matrix44.eye(); a_1_t_2[:3,3] = sf.V3(0,l1,0)
b_1_t_2 = sf.Matrix44.eye(); b_1_t_2[:3,3] = sf.V3(0,l1,0)
c_1_t_2 = sf.Matrix44.eye(); c_1_t_2[:3,3] = sf.V3(0,l1,0)
a_1_T_2 = roll90 * a_1_t_2
b_1_T_2 = roll90 * b_1_t_2
c_1_T_2 = roll90 * c_1_t_2

a2 = a1 * a_1_T_2
b2 = b1 * b_1_T_2
c2 = c1 * c_1_T_2

f_roll = sf.atan2(0.5 * (c2[2,3] - b2[2,3]), r * sf.tan(sf.pi/6))
f_pitch = sf.atan2((a2[2,3] - (b2[2,3]+c2[2,3])/2), r / sf.cos(sf.pi/6))

roll = sf.Symbol('roll')
pitch = sf.Symbol('pitch')

eq1 = sp.Eq(f_roll,roll)
eq2 = sp.Eq(f_pitch,pitch)
eq3 = sp.Eq(qb0, -qc0)

sol = sp.solve([eq1,eq2,eq3], [qa0,qb0,qc0])
print("inverse kinematics:")
print(sol)



