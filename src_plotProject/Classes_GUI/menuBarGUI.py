#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################

import tkinter as tk
import sys
from tkinter.filedialog import askopenfilename # for finding the desired file
from tkinter.filedialog import asksaveasfilename # for finding the desired file
from pathlib import Path

###################################################################################
import os                      # to be able, to use module from Classes folder
import pathlib 
sys.path.insert(0,os.path.join(pathlib.Path(__file__).parent.parent,"Classes")) 
###################################################################################

from configuration import Configuration

""" this class is responsable for handling menubar and provides correspondig functionality  """
class MenuBarGUI:
    #static variable as a shared memmory, this object has a member variable 'dictionary' 
    obj_configuration = Configuration()
    
    def __init__(self, masterWindow,toolbar,projection):
        self.loadFlag = False
        self.window = masterWindow
        self.toolbar = toolbar
        self.projection = projection
        self.filename = None
        self.fileOpenedFlag = 0
   
        menu = tk.Menu(self.window)
        masterWindow.config(menu=menu)
        # 1.file menu with its component 
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label="New plott", command=self.startNewPlott)  # TODO for new Plott
        filemenu.add_separator()
        filemenu.add_command(label="2D.Plot-> file.txt ", command=self.OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="save plott", command=self.savePlott)    # TODO for new Plott
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_application)
        
        # 2.Help menu with its component
        configMenu = tk.Menu(self.window)
        menu.add_cascade(label="Config", menu=configMenu)
        #configMenu.add_command(label="color", command=self.chooseColor)
        configMenu.add_separator()
        configMenu.add_command(label="Save current config", command=self.handleSaveConfig)  # TODO for new Plott
        configMenu.add_separator()
        configMenu.add_command(label="Load config", command=self.handleLoadConfig)
 
        # 3.Help menu with its component
        helpmenu = tk.Menu(self.window)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label=" reserved for the future :) ", command=self.aboutProgramm) 
        pass

       #****************************************CALLBACK FUNCITONS****************************  
    def handleLoadConfig(self):
        # `cwd`: current working directory 
        fileName = askopenfilename(initialdir=Path.cwd(),
                                   filetypes=(("Json File", "*.json"),),
                                    title="Choose a configuration file.")
        if fileName != '':
            try:
                # call by refrence, self.Obj_configuration will change
                Configuration.loadUserChoosedConfig(fileName,self.obj_configuration,self.projection)
                self.loadFlag = True
                print("LOAD DONE : -------------------------")
            except:
                print("Error handleloadConfig")
        return
    
    def handleSaveConfig(self):
        fileName = asksaveasfilename(initialdir=Path.cwd(),
                                     defaultextension=".json",
                                     filetypes=(("Json File", "*.json"),),
                                     title="Save your Configuration",
                                     confirmoverwrite=True)                          
        if fileName != '':
            try:
                Configuration.saveConfigAsJsonFile(fileName,self.obj_configuration.config_dictionary)
            except:
                print("Error handleSaveConfig")
    
    
    # planed for future  
    def startNewPlott(self):      
        msg_box = tk.messagebox.showinfo( 'Futur method','This function is not yet available "unemplemented" :(',icon='info')
              
    def savePlott(self):
        self.toolbar.save_figure()
    
    def updateToolbar(self,refToToolbar):
        self.toolbar = refToToolbar
    
    # get filename to plot from it 
    def OpenFile(self):
        try:         
            self.filename = askopenfilename(initialdir=Path.cwd(),
                                    filetypes=(("Txt File", "*.txt"),),
                                    title="Choose a txt.file to plot the data")
            self.fileOpenedFlag = True
        except FileNotFoundError:
            print("File not found error")
           
                             
    def aboutProgramm(self): 
        print(" help methode is reserved for the future development .... ")
        
    def exit_application(self):     
        msg_box = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',icon='warning')
        if msg_box == 'yes':
            self.window.destroy()
            sys.exit()
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')
            

    

