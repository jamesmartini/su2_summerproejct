#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:18:59 2018

@author: jamesmartini
"""
import numpy as np
import matplotlib.pyplot as plt

#newly generated mesh read in
data_elem = np.genfromtxt('mesh_out.su2',skip_header=4,skip_footer=5494)
data_vert =np.genfromtxt('mesh_out.su2',skip_header=10221,skip_footer=260)
data_elem = data_elem.astype(np.int)
x = data_vert[:,0]
y = data_vert[:,1]
triangles = data_elem[:,1:4]
plt.triplot(x,y,triangles)

#Old mesh read in
data_elemold = np.genfromtxt('mesh_old.su2',skip_header=4,skip_footer=5494)
data_vertold =np.genfromtxt('mesh_old.su2',skip_header=10221,skip_footer=260)
data_elemold = data_elemold.astype(np.int)
x = data_vertold[:,0]
y = data_vertold[:,1]
triangles = data_elemold[:,1:4]
plt.triplot(x,y,triangles)

#See if the meshes are equal
eq = np.array_equal(data_vert,data_vertold)
print(eq)
