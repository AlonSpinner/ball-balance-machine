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


fig = plt.figure(); 
ax = fig.add_subplot(projection='3d')
plot_pose3_on_axes(ax, o)
plot_pose3_on_axes(ax, a0)
plot_pose3_on_axes(ax, b0)
plot_pose3_on_axes(ax, c0)

set_axes_equal(ax)
plt.show()


# sf.Rot3.from_angle_axis
# sf.V3(0, 0, 0)
# sf.Pose3(R,t)
# b1 = b0.compose()
# b1 = b0.compose(sf.)

