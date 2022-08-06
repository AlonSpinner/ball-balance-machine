import symforce.symbolic as sf
import math as m
import matplotlib.pyplot as plt
from plot import plot_pose3_on_axes, set_axes_equal, plot_triangle, plot_line
import numpy as np 


''' 
       a0
      /|\            |y
     / |r\           |___x
    /  |  \ 
   /   o   \
b0 /_________\ c0

'''
#base storey
r = 1.0
o_base = sf.Pose3()
a0 = o_base.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(sf.pi/2,0,0), #90 degrees
                        sf.V3(0, r, 0)))
b0 = o_base.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(sf.pi *(1 +1/6),0,0), #210 degrees
                        sf.V3(-r * sf.sin(sf.pi/3), -r * sf.cos(sf.pi/3), 0))) #60 degrees
c0 = o_base.compose(sf.Pose3(
                        sf.Rot3.from_yaw_pitch_roll(-sf.pi/6,0,0), #-30 degrees
                        sf.V3(+r * sf.sin(sf.pi/3), -r * sf.cos(sf.pi/3), 0)))


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
qa1 = qb1 = qc1 = m.radians(60)
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

t_plane = (a2.t + b2.t + c2.t)/3
v = (a2.t - t_plane).normalized()
u = (c2.t - t_plane).normalized()
w = u.cross(v).normalized()
u = -w.cross(v)
r_plane = sf.Rot3.from_rotation_matrix(np.asarray([u.evalf(),v.evalf(),w.evalf()]).T)

o_plane = sf.Pose3(R = r_plane, t = t_plane)
print('plane yaw - pitch - roll in degrees')
print([m.degrees(num.evalf()) for num in r_plane.to_yaw_pitch_roll()])

fig = plt.figure(); 
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
#origin
plot_pose3_on_axes(ax, o_base); ax.text(*o_base.t, 'o_base')

#base storey
plot_pose3_on_axes(ax, a0); ax.text(*a0.t,'a0')
plot_pose3_on_axes(ax, b0); ax.text(*b0.t,'b0')
plot_pose3_on_axes(ax, c0); ax.text(*c0.t,'c0')
plot_triangle(ax, np.asarray([a0.t,b0.t,c0.t], dtype = float), 'red')

#first storey, after link l0
plot_pose3_on_axes(ax, a1); ax.text(*a1.t,'a1')
plot_pose3_on_axes(ax, b1); ax.text(*b1.t,'b1')
plot_pose3_on_axes(ax, c1); ax.text(*c1.t,'c1')

#first links:
plot_line(ax, a0.t, a1.t)
plot_line(ax, b0.t, b1.t)
plot_line(ax, c0.t, c1.t)

#second storey, after link l1
plot_pose3_on_axes(ax, a2); ax.text(*a2.t,'a2')
plot_pose3_on_axes(ax, b2); ax.text(*b2.t,'b2')
plot_pose3_on_axes(ax, c2); ax.text(*c2.t,'c2')
plot_pose3_on_axes(ax,o_plane); ax.text(*o_plane.t,'o_plane')
plot_triangle(ax, np.asarray([a2.t,b2.t,c2.t], dtype = float), 'yellow')

#second links:
plot_line(ax, a1.t, a2.t)
plot_line(ax, b1.t, b2.t)
plot_line(ax, c1.t, c2.t)

set_axes_equal(ax)
plt.show()

