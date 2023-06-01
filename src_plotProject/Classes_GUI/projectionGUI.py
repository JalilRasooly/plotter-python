'''
Orignal Programm:
radiobutton_00.py
\citep[S497]{Steinkamp2021}
modified at 10.12.2022 by:
Jalil Rasooly and Otto Pascal
WiSe 2022
'''
#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################

from tkinter import *
""" this class is a subclass of Frame and handles projection issue, in variable "self.choice" user-interaction will be stored """
class ProjectionGUI(Frame):
    def __init__(self, master,commandMaster):
        Frame.__init__(self, master)
        self.pack()
        lblFrm = LabelFrame(self, padx=10,pady=10,text='Select projection\t\t\t',height=30,width=100)
        lblFrm.pack(side='left',pady=10)
        self.choice = StringVar()
        self.choice.set('2D')
        self.makeRadioBtn(lblFrm, self.choice,'2D','2D',commandMaster)
        self.makeRadioBtn(lblFrm, self.choice,'3D','3D',commandMaster)
        self.getProjectionChoice()

    def getProjectionChoice(self):
        """ return state of "self.choice" variable """
        return self.choice.get()
        
    def makeRadioBtn(self, root=None, cVar=None,txt='', val='', cmd=None):
        """ create button and pack it to the given root """
        chkbtn = Radiobutton(root,text=txt,variable=cVar,value=val,command=cmd)
        chkbtn.pack(anchor='w')