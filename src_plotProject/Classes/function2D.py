
import  numpy as np
import math
import tkinter as tk

"""
https://realpython.com/python-eval-function/ , s. Bericht [1]
"""
#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################
""" this class provide useful methode for handling functionsexpression or data from file 
    the result is than saved in member variable self.x and self.y """

class Function2D():
    def __init__(self):
        self.ALLOWED_NAMES = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        self.x = 0
        self.y = 0
             
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
        
    def generateDataFromExpression(self,f_str,x_start=1 ,x_end = 100,x_step = 0.01,log=False):
        """turn function expression to a numpy array and save it in member variable self.x und self.y """
        #switch if startvalue is bigger than endvalue
        if x_start > x_end:
            x_start,x_end = x_end,x_start
        # check that the step varible is fit inside the given interval
        if x_step > abs(x_start-x_end):
            tk.messagebox.showinfo( 'Invalid input Error!','Step was to big in the given interval, I changed it to 0.01',icon='info')
            x_step = 0.01
        
        if log == False:
            self.x = np.arange(x_start,x_end,x_step)
        else:
            if(x_start<=0):
                x_start = 0.01
            self.x = np.logspace(x_start,x_end,int((x_end-x_start)*2))
        
        tmpList = [] 
        for  x_val in self.x:       
            self.ALLOWED_NAMES['x'] = x_val
            tmpList.append(self.__evaluate(f_str))  # create tupel (x,y)
            pass
        # make a numpy array and save it to the member variable self.y
        self.y = np.array(tmpList)   
        if np.sum(self.y) == 0.0:
            tk.messagebox.showinfo( 'Invalid input Error!','I can only evalute functionexpression which contians x as a variable!',icon='info')


    def generateDataFromFileTxt(self,fileName):
        """load data from given file name, turn it to a numpy array and save it in member variable self.x und self.y """
        with open(fileName,'r') as filestream:
            line  = filestream.readline()
            x, ylist = line.split(";")
            y,funcName = ylist.split(',')
            xList = []
            yList = []
            try:
                for line in filestream:
                    x,y = line.split(';')
                    xList.append(float(x))
                    yList.append(float(y))
                self.x = np.array(xList)
                self.y = np.array(yList)
            except ValueError:
                print("Data structur is not readable! ")
        return funcName



    