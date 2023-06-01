#############################################################
#  pyt_WS_22_23                                             #
#  Team: Pascal Otto (1587414) & Jalil Rasooly (1550961)    #
#  02.01.2023                                               #
#############################################################

import os
import sys
import pathlib 
sys.path.insert(0,os.path.join(pathlib.Path(__file__).parent.parent,"Classes"))

print("myModulePath---------> ",myModulePath)
#sys.path.insert()

CURRENT_PATH = pathlib.Path(__file__).parent
sys.path.append(CURRENT_PATH)

from function2D import Function2D

f = Function2D()
express = 'x**3+x+1'
f.generateDataFromExpression(express,-6,6,0.2)
filename = "M.Data9.txt"
with open(os.path.join(CURRENT_PATH,filename), "w") as filestream:
    filestream.write("'x' ; 'y',"+express+"\n")
    for i in range(len(f.x)):
        filestream.write(str(round(f.x[i],3))+';'+ str(round(f.y[i],3))+'\n')