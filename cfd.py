import numpy as np
import subprocess
from scipy import interpolate
import shutil
import fileinput
import sys
import os
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

#Parameter values
p= [.001,.01]

#Replace line function
def replaceLine(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

shutil.copyfile('config_template.cfg','config_current.cfg')
replaceLine('config_current.cfg','DV_KIND= HICKS_HENNE','DV_KIND= HICKS_HENNE, HICKS_HENNE')
replaceLine('config_current.cfg','DV_PARAM= (1, 0.5)','DV_PARAM= (1, 0.5); (0, 0.5)')
replaceLine('config_current.cfg','DV_VALUE= 0.0','DV_VALUE= '+str(p[0])+', '+str(p[1]))
replaceLine('config_current.cfg','MESH_FILENAME= mesh_rae2822_inv.su2','MESH_FILENAME= mesh_out.su2')

#Things that we had to change in the SU2 cfg file
replaceLine('config_current.cfg','SPATIAL_ORDER_FLOW= 2ND_ORDER_LIMITER','MUSCL_FLOW= YES')
replaceLine('config_current.cfg','REF_LENGTH_MOMENT= 1.0','REF_LENGTH= 1.0')
replaceLine('config_current.cfg','AD_COEFF_FLOW= ( 0.15, 0.5, 0.02 )','JST_SENSOR_COEFF= ( 0.15, 0.5)')
replaceLine('config_current.cfg','SPATIAL_ORDER_ADJFLOW= 2ND_ORDER','MUSCL_ADJFLOW= YES')
replaceLine('config_current.cfg','AD_COEFF_ADJFLOW= ( 0.15, 0.5, 0.02 )','ADJ_JST_SENSOR_COEFF= (0.15, 0.5)')
replaceLine('config_current.cfg','MOTION_FILENAME= mesh_motion.dat','DV_FILENAME= mesh_motion.dat')

#Creates a deformed mesh
p1 = subprocess.Popen(['SU2_DEF', 'config_current.cfg'], stdout=subprocess.PIPE)
p1.communicate()


#Runs SU2 on the deformed mesh
#p1 = subprocess.Popen(['SU2_CFD', 'config_current.cfg'], stdout=subprocess.PIPE)
#p1.communicate()

