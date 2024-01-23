from py4cst.CST import Interface, Cylinder, Component
import time
import numpy as np

ifc = Interface(2023)
ifc.set_quiet_mode(False)

proj = ifc.new_microwave_studio_project()

component = Component(proj)
component.create('cylinders')

cylinder = Cylinder(proj)
cylinder.reset()
cylinder.set_axis(Cylinder.AXIS_Z)
cylinder.set_component('cylinders')
cylinder.set_inner_radius(0)
cylinder.set_outer_radius(0.2)
cylinder.set_smooth_geometry()
cylinder.set_z_range(0, 2)

time.sleep(2)

def add_cyl(id, x, y):
    cylinder.set_name(f'cylinder{id}')
    cylinder.set_x_center(x)
    cylinder.set_y_center(y)
    cylinder.create()

num_rounds = 5
num_elems = 200
angle_step = 2*np.pi*num_rounds/num_elems
min_radius = 10
max_radius = 20

for i in range(num_elems):
    angle = i*angle_step
    r = min_radius + (max_radius-min_radius)/num_elems*i
    x = r*np.cos(angle)
    y = r*np.sin(angle)
    add_cyl(i, x, y)