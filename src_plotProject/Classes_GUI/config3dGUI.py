#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################

""" this class provides a GUI and some functions for customizing 3D-functionsproperties"""
from tkinter import *
class Config3dGUI(Frame):
    def __init__(self, master, commandMaster, configDataDictionary):
        Frame.__init__(self, master)
        self.pack()
        lblFrm = LabelFrame(self, padx=10, pady=20,text='3D interactive Config\t\t')
        lblFrm.pack(pady=10)
        # Configuration variable from JSON file for 3d Function
        self.configData3D = configDataDictionary['3D']
        self.choice = StringVar()
        self.choice.set(self.configData3D['graphtype'])
        self.makeRadioBtn(lblFrm, self.choice, 'Wireframe','wireframe', commandMaster)
        self.makeRadioBtn(lblFrm, self.choice, 'Scatter','scatter', commandMaster)
        self.makeRadioBtn(lblFrm, self.choice, 'Surface','surface', commandMaster)
        self.makeRadioBtn(lblFrm, self.choice, 'Sur.Binary ','binary', commandMaster)
        self.makeRadioBtn(lblFrm, self.choice, 'Contour3D ','conour3D', commandMaster)

        inputFrame = LabelFrame(lblFrm, text='Plot properties\t\t')
        inputFrame.pack(pady=5)
        # Label( inputFrame,text='\t\t').grid(row=0,column=0,sticky='we')
        Label(inputFrame, text='xyMin\t:').grid(row=1, column=0, sticky='w')
        Label(inputFrame, text='xyMax\t:').grid(row=2, column=0, sticky='w')
        Label(inputFrame, text='xLabel\t:').grid(row=3, column=0, sticky='w')
        Label(inputFrame, text='yLabel\t:').grid(row=4, column=0, sticky='w')
        Label(inputFrame, text='zLabel\t:').grid(row=5, column=0, sticky='w')
        Label(inputFrame, text='P.title\t:').grid(row=6, column=0, sticky='w')

        self.xyMinVar = StringVar()
        self.xyMaxVar = StringVar()
        self.zLabelVar = StringVar()
        self.xLabelVar = StringVar()
        self.yLabelVar = StringVar()
        self.title = StringVar()
        self.setDefaultProperties()
    
        Entry(inputFrame, textvariable=self.xyMinVar,
              width=15).grid(row=1, column=1, sticky='we')
        Entry(inputFrame, textvariable=self.xyMaxVar,
              width=15).grid(row=2, column=1, sticky='we')
        Entry(inputFrame, textvariable=self.xLabelVar,
              width=15).grid(row=3, column=1, sticky='we')
        Entry(inputFrame, textvariable=self.yLabelVar,
              width=15).grid(row=4, column=1, sticky='we')
        Entry(inputFrame, textvariable=self.zLabelVar,
              width=15).grid(row=5, column=1, sticky='we')
        Entry(inputFrame, textvariable=self.title,
              width=15).grid(row=6, column=1, sticky='we')
        self.getChoice()

    def getChoice(self):
        return self.choice.get()

    def makeRadioBtn(self, root=None, cVar=None, txt='', val='', cmd=None):
        chkbtn = Radiobutton(root, text=txt, variable=cVar,
                             value=val, command=cmd)
        chkbtn.pack(anchor='w')

    def setDefaultProperties(self):
        try:
            self.xyMinVar.set(self.configData3D['properties']['xyMin'])
            self.xyMaxVar.set(self.configData3D['properties']['xyMax'])
            self.xLabelVar.set(self.configData3D['properties']['xLabel'])
            self.yLabelVar.set(self.configData3D['properties']['yLabel'])
            self.zLabelVar.set(self.configData3D['properties']['zLabel'])
            self.title.set(self.configData3D['properties']['title'])
        except:
            print(" data could 3d loading error")
    
    def set3Dproperties(self,ConfigDataDictionary):
        self.configData3D = ConfigDataDictionary['3D']
        self.xyMinVar.set(self.configData3D['properties']['xyMin'])
        self.xyMaxVar.set(self.configData3D['properties']['xyMax'])
        self.xLabelVar.set(self.configData3D['properties']['xLabel'])
        self.yLabelVar.set(self.configData3D['properties']['yLabel'])
        self.zLabelVar.set(self.configData3D['properties']['zLabel'])
        self.title.set(self.configData3D['properties']['title'])

    def get3DProperties(self, entryfunStr):
        self.configData3D = {"3D":0}
        self.configData3D['3D'] = {
            "f": entryfunStr,
            "graphtype": str(self.getChoice()),
            "properties": {
                "xyMin":   str(self.xyMinVar.get()),
                "xyMax":   str(self.xyMaxVar.get()),
                "xLabel": str(self.xLabelVar.get()),
                "yLabel": self.yLabelVar.get(),
                "zLabel": self.zLabelVar.get(),
                "title": self.title.get()
            }
        }
        return self.configData3D

