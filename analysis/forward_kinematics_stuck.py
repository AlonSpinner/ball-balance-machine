import symforce.symbolic as sf
import sympy as sp
import math as m
import matplotlib.pyplot as plt
from plot import plot_pose3_on_axes, set_axes_equal

o_base = sf.Pose3()

''' 
       a
      /|\            |y
     / |r\           |___x
    /  |  \ 
   /   o   \
b /_________\ c

'''
#base storey
r = sf.Symbol('r')
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
a1 = a0.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(0,0,qa0),
                        sf.V3()))
a1 = a1.compose(sf.Pose3(
                        sf.Rot3(),
                        sf.V3(0, l0, 0)))
b1 = b0.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(0,0,qb0),
                        sf.V3()))
b1 = b1.compose(sf.Pose3(
                        sf.Rot3(),
                        sf.V3(0, l0, 0)))
c1 = c0.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(0,0,qc0),
                        sf.V3()))
c1 = c1.compose(sf.Pose3(
                        sf.Rot3(),
                        sf.V3(0, l0, 0)))

#second storey frames
l1 = sf.Symbol('l1')
qa1 = sf.Symbol("qa1")
qb1 = sf.Symbol("qb1")
qc1 = sf.Symbol("qc1")
a2 = a1.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(0,0,qa1),
                        sf.V3()))
a2 = a2.compose(sf.Pose3(
                        sf.Rot3(),
                        sf.V3(0, l1, 0)))
b2 = b1.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(0,0,qb1),
                        sf.V3()))
b2 = b2.compose(sf.Pose3(
                        sf.Rot3(),
                        sf.V3(0, l1, 0)))
c2 = c1.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(0,0,qc1),
                        sf.V3()))
c2 = c2.compose(sf.Pose3(
                        sf.Rot3(),
                        sf.V3(0, l1, 0)))

d_sqrd = 3 * r**2
eq_a2b2 = sp.Eq((a2.t - b2.t).squared_norm(), d_sqrd)
eq_a2c2 = sp.Eq((a2.t - c2.t).squared_norm(), d_sqrd)
eq_b2c2 = sp.Eq((b2.t - c2.t).squared_norm(), d_sqrd)

sol = sp.solve([eq_a2b2, eq_a2c2, eq_b2c2],[qa1,qb1,qc1])