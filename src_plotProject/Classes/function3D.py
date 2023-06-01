import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

"""
https://realpython.com/python-eval-function/ , s. Bericht [1]
"""
#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################
""" this class provide useful methode for handling 3D functionsexpression  
    the result will be saved in member variable self.x, self.y, and self.z """

class Function3D():
    def __init__(self):
        self.ALLOWED_NAMES = {'sin':np.sin,'cos':np.cos,'sqrt':np.sqrt,'abs':np.abs,'exp':np.exp,'log':np.log}  
        self.x = 0
        self.y = 0
        self.z = 0
        
    #private methode
    def __evaluate(self,expression):
        """Evaluate a math expression and return the numaric result"""
        # Compile the expression
        code = compile(expression, "<string>", "eval")
        # Validate allowed names
        for name in code.co_names:
            if name not in self.ALLOWED_NAMES:               
                return 0                 
        return eval(code, {"__builtins__": {}}, self.ALLOWED_NAMES)

    def generateDataFromExpression(self,fxy,xy_start=-6 ,xy_end = 6):
        """turn 3D-function's expression to a numpy array and save it in member variable self.x und self.y,self.z """
        x = np.linspace(xy_start,xy_end)
        y = np.linspace(xy_start,xy_end)
        X,Y = np.meshgrid(x,y)
        #print(self.ALLOWED_NAMES)
        self.ALLOWED_NAMES['x'] = X
        self.ALLOWED_NAMES['y'] = Y
        Z = self.__evaluate(fxy)
        self.x = X
        self.y = Y
        self.z = Z
        
    def generateDataFromFileTxt(self,fileName):
        """ unimplemented methode reserved for future :)"""
        return   