
from tkinter import *
from tkinter import colorchooser 
import copy

#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################
""" this class provides a GUI and some functions for customizing 2D-functionsproperties"""
class Config2dGUI(Frame):
    def __init__(self, master, commandMaster, configDataDictionary):
        Frame.__init__(self, master)
        self.pack()
        self.configData2D = configDataDictionary['2D']
        self.xStep   = StringVar()
        self.xMinVar = StringVar()
        self.xMaxVar = StringVar()
        self.xLabelVar = StringVar()
        self.yLabelVar = StringVar()
        self.title = StringVar()
        self.color = StringVar()
        self.menuLinstyle = StringVar()
        self.menuLinwidth = StringVar()
        self.legendName = StringVar()
        self.menuLinstyle.set('style')
        self.menuLinwidth.set('width')
        # shared variable "self.choosedFunction" for checking which radiobutton was chosen
        self.choosedFunction = StringVar()
        self.choosedFunction.set('f1')

        # create some label & labelframe for structuring properties items
        lblFrm = LabelFrame(self, text='2D Properties Config\t\t')
        lblFrm.pack(pady=5)
        generalPP_frm = LabelFrame(lblFrm, text="General function properties")
        generalPP_frm.pack()       
        inividualFuncProperties_frm = LabelFrame(lblFrm, text="Individual function Properties")
        inividualFuncProperties_frm.pack(pady=10)
        frm_inside_GeneralFrm = Frame(generalPP_frm, pady=5)
        frm_inside_GeneralFrm.grid(row=6, column=0, rowspan=3, columnspan=4, sticky='nesw', pady=10)
        # create labels with corresponding entries und put them to the generalPP_frame
        Label(generalPP_frm, text='xStep:').grid(row=0, column=0, sticky='e')
        Label(generalPP_frm, text='xMin:').grid(row=1, column=0, sticky='e')
        Label(generalPP_frm, text='xMax:').grid(row=2, column=0, sticky='e')
        Label(generalPP_frm, text='xLabel:').grid(row=3, column=0, sticky='e')
        Label(generalPP_frm, text='yLabel:').grid(row=4, column=0, sticky='e')
        Label(generalPP_frm, text='title:').grid(row=5, column=0, sticky='e')
        Entry(generalPP_frm, textvariable=self.xStep, width=15).grid(row=0, column=1, columnspan=3, sticky='w', padx=5)
        Entry(generalPP_frm, textvariable=self.xMinVar, width=15).grid(row=1, column=1, columnspan=3, sticky='w', padx=5)
        Entry(generalPP_frm, textvariable=self.xMaxVar, width=15).grid(row=2, column=1, columnspan=3, sticky='w', padx=5)
        Entry(generalPP_frm, textvariable=self.xLabelVar, width=15).grid(row=3, column=1, columnspan=3, sticky='w', padx=5)
        Entry(generalPP_frm, textvariable=self.yLabelVar, width=15).grid(row=4, column=1, columnspan=3, sticky='w', padx=5)
        Entry(generalPP_frm, textvariable=self.title, width=15).grid(row=5, column=1, columnspan=3, sticky='w', padx=5)

        self.var_checkGrid = IntVar()
        self.var_checkLog = IntVar()
        self.var_checkLegend = IntVar()
        self.chkbtnGrid = Checkbutton(frm_inside_GeneralFrm, text='Grid', command=commandMaster, variable=self.var_checkGrid)
        self.chkbtnLog = Checkbutton(frm_inside_GeneralFrm, text='Log', command=commandMaster, variable=self.var_checkLog)
        self.chkbtnLegend = Checkbutton(frm_inside_GeneralFrm, text='Legend', command=commandMaster, variable=self.var_checkLegend)
        self.chkbtnGrid.grid(column=0, row=0)
        self.chkbtnLog.grid(column=1, row=0)
        self.chkbtnLegend.grid(column=2, row=0)

        self.rbtn1 = self.makeRadioBtn(inividualFuncProperties_frm, self.choosedFunction, 'f1', 'f1')
        self.rbtn2 = self.makeRadioBtn(inividualFuncProperties_frm, self.choosedFunction, 'f2', 'f2')
        self.rbtn3 = self.makeRadioBtn(inividualFuncProperties_frm, self.choosedFunction, 'f3', 'f3')
        self.rbtn4 = self.makeRadioBtn(inividualFuncProperties_frm, self.choosedFunction, 'f4', 'f4')
        self.rbtn1.grid(column=0, row=2, padx=5)
        self.rbtn2.grid(column=1, row=2, padx=5)
        self.rbtn3.grid(column=2, row=2, padx=5)
        self.rbtn4.grid(column=3, row=2, padx=5, pady=10)

        Label(inividualFuncProperties_frm, text='legendname: ').\
              grid(row=0, column=0, columnspan=2, sticky='ew', pady=5)
        Entry(inividualFuncProperties_frm, textvariable=self.legendName, width=15).\
              grid(row=0, column=2, columnspan=2, sticky='ew', pady=5, padx=5)

        self.btnColorChooser = Button(inividualFuncProperties_frm, text='color',\
                                      command=self.chooseColor, background='#bbbbbb')
        self.btnColorChooser.grid(row=1, column=0, sticky='e')

        # Create dropdown Menus
        self.dropMenuLinestyle = OptionMenu(inividualFuncProperties_frm, self.menuLinstyle, *['solid', "dotted", "dashed", "dashdot"])
        self.dropMenuLinestyle.grid(row=1, column=1, columnspan=2, sticky='ew')
        self.dropMenuLineWidth = OptionMenu(inividualFuncProperties_frm, self.menuLinwidth, *['1', "2", "3", "4", "5", "6"])
        self.dropMenuLineWidth.grid(row=1, column=3, sticky='ew')
        self.__setGeneralProperties()
        pass
    

    def makeRadioBtn(self, root=None, cVar=None, txt='', val='', cmd=None):
        return Radiobutton(root, text=txt, variable=cVar, value=val, command=cmd)

    def __setGeneralProperties(self):
            self.xStep.set(self.configData2D['g_properties']['xStep'])
            self.xMinVar.set(self.configData2D['g_properties']['xMin'])
            self.xMaxVar.set(self.configData2D['g_properties']['xMax'])
            self.xLabelVar.set(self.configData2D['g_properties']['xLabel'])
            self.yLabelVar.set(self.configData2D['g_properties']['yLabel'])
            self.title.set(self.configData2D['g_properties']['title'])
            self.var_checkGrid.set(self.configData2D['g_properties']['grid'] == True)
            self.var_checkLog.set(self.configData2D['g_properties']['log'] == True)
            self.var_checkLegend.set( self.configData2D['g_properties']['legend'] == True)
            self.legendName.set(self.configData2D["i_properties"]['f1']['legendname'])
            self.color.set(self.configData2D["i_properties"]['f1']['color'])

    def __saveChangesToLocalDictionary(self):      
        self.configData2D["g_properties"] = {
            'xStep': self.xStep.get(),
            'xMin': self.xMinVar.get(),
            'xMax': self.xMaxVar.get(),
            'xLabel': self.xLabelVar.get(),
            'yLabel': self.yLabelVar.get(),
            'title': self.title.get(),
            "grid": self.var_checkGrid.get() == 1,
            "log": self.var_checkLog.get() == 1,
            "legend": self.var_checkLegend.get() == 1,
        }
        if (self.choosedFunction.get() == 'f1'):
            self.__helperMethod('f1')
        if (self.choosedFunction.get() == 'f2'):
            self.__helperMethod('f2')
        if (self.choosedFunction.get() == 'f3'):
            self.__helperMethod('f3')
        if (self.choosedFunction.get() == 'f4'):
            self.__helperMethod('f4')
             
    def __helperMethod(self,str):
        if(self.menuLinstyle.get()=='style'):
            self.menuLinstyle.set('solid')
        if(self.menuLinwidth.get()=='width'):
            self.menuLinwidth.set('1')
        self.configData2D["i_properties"][str]['legendname'] = self.legendName.get()
        self.configData2D["i_properties"][str]['color']      = self.color.get()
        self.configData2D["i_properties"][str]['linestyle']  = self.menuLinstyle.get()
        self.configData2D["i_properties"][str]['linewidth']  = self.menuLinwidth.get()

    def chooseColor(self):
        (rgb, hx) = colorchooser.askcolor()
        self.color.set(str(hx))
        self.btnColorChooser.configure(background=str(hx))

    def get2DProperties(self):
        self.__saveChangesToLocalDictionary()
        return self.configData2D
    
    def set2Dproperties(self,ConfigDataDictionary):
        self.configData2D = copy.deepcopy(ConfigDataDictionary['2D'])
        self.__setGeneralProperties()
        
            
            

