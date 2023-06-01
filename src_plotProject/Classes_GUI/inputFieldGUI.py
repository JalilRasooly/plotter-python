import tkinter as tk

#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################

""" this class is responsable for handling the inputfield and provides functionalty for manipulation 
    of the inputfield. Like creating needed entries according to the projection etc....  """
class InputFieldGUI(tk.Frame):
    def __init__(self, master,projection,strListFuncDefaultExpres,commandPlot = None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master = tk.Frame(self, padx=10, pady=0)
        self.master.pack()

        self.f3Dstr= tk.StringVar()
        self.f1str = tk.StringVar()
        self.f2str = tk.StringVar()
        self.f3str = tk.StringVar()
        self.f4str = tk.StringVar()
        self.setFuncStr(strListFuncDefaultExpres)

        self.var_check1 = tk.IntVar()
        self.var_check2 = tk.IntVar()
        self.var_check3 = tk.IntVar()
        self.var_check4 = tk.IntVar()
        self.var_check1.set('1')
        self.chkbtn1 = tk.Checkbutton(self.master,text='f1',variable=self.var_check1,command=commandPlot)
        self.chkbtn2 =tk.Checkbutton(self.master,text='f2',variable=self.var_check2,command=commandPlot)
        self.chkbtn3 =tk.Checkbutton(self.master,text='f3',variable=self.var_check3,command=commandPlot)
        self.chkbtn4 =tk.Checkbutton(self.master,text='f4',variable=self.var_check4,command=commandPlot)
        #create entry for function
        self.entry_f3D = tk.Entry(self.master,width=30,textvariable=self.f3Dstr)
        self.entry_f1  = tk.Entry(self.master,textvariable=self.f1str)
        self.entry_f2  = tk.Entry(self.master,textvariable=self.f2str)
        self.entry_f3  = tk.Entry(self.master,textvariable=self.f3str)
        self.entry_f4  = tk.Entry(self.master,textvariable=self.f4str)

         # default projection
        self.__projektion = projection
        if self.__projektion == '3D':
            self.__place_3dInputField_to_GUI()
        else:
            self.__place_2dInputField_to_GUI()
    
    
    def getFunStrList(self):
        return [  self.f3Dstr.get(),
                  self.f1str.get(),
                  self.f2str.get(),
                  self.f3str.get(),
                  self.f4str.get()]

    def getListStateOfChecks(self):
         return[self.var_check1.get(),\
                self.var_check2.get(),\
                self.var_check3.get(),\
                self.var_check4.get(), ]

    def setListStateOfChecks(self,listChecksVar):
        self.var_check1.set(listChecksVar[0])
        self.var_check2.set(listChecksVar[1])
        self.var_check3.set(listChecksVar[2])
        self.var_check4.set(listChecksVar[3])


    def get2DFunStrPlusCheck(self):
        return [  (self.f1str.get(),self.var_check1.get()),
                  (self.f2str.get(),self.var_check2.get()),
                  (self.f3str.get(),self.var_check3.get()),
                  (self.f4str.get(),self.var_check4.get())]


    def __place_2dInputField_to_GUI(self):
        #self.__destroy_3d_inputfield() 
        self.entry_f3D.destroy() 
        self.chkbtn1.grid(column=0, row=0,sticky="w")
        self.chkbtn2.grid(column=0, row=1,sticky="w")
        self.chkbtn3.grid(column=0, row=2,sticky="w")
        self.chkbtn4.grid(column=0, row=3,sticky="w")
        # put entries on the grid
        self.entry_f1.grid(column=1, row=0,sticky="ew")
        self.entry_f2.grid(column=1, row=1,sticky="ew")
        self.entry_f3.grid(column=1, row=2,sticky="ew")
        self.entry_f4.grid(column=1, row=3,sticky="ew")

    def __place_3dInputField_to_GUI(self):
        self.entry_f3D.grid(column=0, row=0,pady=10)
  
    def setProjection(self,strProjection):
        if( strProjection =='3D' or strProjection =='2D'):
            self.__projektion = strProjection

    def setFuncStr(self,strList):
        self.f3Dstr.set(strList[0])
        self.f1str.set(strList[1])
        self.f2str.set(strList[2])
        self.f3str.set(strList[3])
        self.f4str.set(strList[4])

        

