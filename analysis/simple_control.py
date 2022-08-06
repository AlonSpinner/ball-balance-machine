from binascii import a2b_base64, b2a_base64
from turtle import Vec2D
import symforce.symbolic as sf
import symforce
import math as m

''' 
       a
      /|\            |y
     / |r\           |___x
    /  |  \ 
   /   o   \
b /___|r/2_\ c


'''
o = sf.Pose3()

#base storey
r = sf.Symbol('r')
a0 = o.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(m.radians(90),0,0),
                        sf.V3(0, r, 0)))
b0 = o.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(m.radians(210),0,0),
                        sf.V3(-r * m.sin(m.radians(60)), -r * m.cos(m.radians(60)), 0)))
c0 = o.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(m.radians(-30),0,0),
                        sf.V3(r * m.sin(m.radians(60)), -r * m.cos(m.radians(60)), 0)))


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


roll = 0.5 * (c2.t[2] - b2.t[2]) / (0.5 *r)
pitch = (a2.t[2] - (b2.t[2]+c2.t[2])/2) / r *(1 + m.sin(m.radians(30)))



