import symforce.symbolic as sf
import math as m
import matplotlib.pyplot as plt
from plot import plot_pose3_on_axes, set_axes_equal

o = sf.Pose3()

''' 
       a
      /|\            |y
     / |r\           |___x
    /  |  \ 
   /   o   \
b /_________\ c

'''
#base storey
r = 1.0
a0 = o.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(m.radians(90),0,0),
                        sf.V3(0, r, 0)))
b0 = o.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(m.radians(210),0,0),
                        sf.V3(-r * m.sin(m.radians(60)), -r * m.cos(m.radians(60)), 0)))
c0 = o.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(m.radians(-30),0,0),
                        sf.V3(+r * m.sin(m.radians(60)), -r * m.cos(m.radians(60)), 0)))


#first storey frames
l0 = 0.5
qa0 = qb0 = qc0 = m.radians(80)
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
l1 = 0.5
qa1 = qb1 = qc1 = m.radians(10)
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



fig = plt.figure(); 
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
#origin
plot_pose3_on_axes(ax, o)

#base storey
plot_pose3_on_axes(ax, a0)
plot_pose3_on_axes(ax, b0)
plot_pose3_on_axes(ax, c0)

#first storey, after link l0
plot_pose3_on_axes(ax, a1)
plot_pose3_on_axes(ax, b1)
plot_pose3_on_axes(ax, c1)

#second storey, after link l1
plot_pose3_on_axes(ax, a2)
plot_pose3_on_axes(ax, b2)
plot_pose3_on_axes(ax, c2)

set_axes_equal(ax)
plt.show()

