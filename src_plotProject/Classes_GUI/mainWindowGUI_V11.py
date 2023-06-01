#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################

import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk )

###################################################################################
import os                      # to be able, to use module from 'Classes' folder
import sys
import pathlib 
sys.path.insert(0,os.path.join(pathlib.Path(__file__).parent.parent,"Classes")) 
###################################################################################

import ntpath
from config2dGUI    import Config2dGUI
from config3dGUI    import Config3dGUI
from projectionGUI  import ProjectionGUI
from inputFieldGUI  import InputFieldGUI
from menuBarGUI     import MenuBarGUI
from function3D     import Function3D     # ignor warning 
from function2D     import Function2D     # ignor warning
D_PROJECTION = '3D' # Constant don't change! 

""" This class is the main-programm, which is written in OOP style. Every own written module represent a Class.
    for more details please check 'Bericht' """
class MainProgramWindow:   
    def __init__(self):
        # build main window with the desired customization
        self.window = tk.Tk()    
        self.window.resizable(False,False)
        self.window.title("Abschlussaufgabe_WiSe22")
        
        # Create a mainframe with grid layout,it will contains leftframe and graphframe for managing there items 
        self.mainFrame = tk.Frame(self.window) 
        self.mainFrame.grid(column=0, row=0, sticky="nsew")

        self.graphFrame = tk.LabelFrame(self.mainFrame, padx=10,pady=10,text='Graph area',relief='sunken')
        self.graphFrame.configure(bg='#ffffff')
        self.graphFrame.grid(column=2, columnspan=6, row=0, rowspan=11)
        self.fig = Figure(figsize=(8,6))
        #add figure to the convas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphFrame)  # A tk.DrawingArea.
        self.canvas.draw()
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack()
        # create & put toolbar from "matplotlib.backends.backend_tkagg" library to the convas
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.graphFrame)
        self.toolbar.update()       
             
        # create member variable from MenuBarGUI class, put it to the mainWindow
        self.obj_MenuBarGUI = MenuBarGUI(self.window,self.toolbar,D_PROJECTION)     
         
        # create leftframe & put it to the left side of the mainframe
        self.leftFrame = tk.LabelFrame(self.mainFrame,pady=5,padx=10,height=200, width=200)
        self.leftFrame.grid(column=0,columnspan=2,row=0,rowspan=11,sticky="nsew")

        self.lbl_insideOfLeftFrame = tk.Frame(self.leftFrame,cursor="arrow",height=200,width=200)
        self.lbl_insideOfLeftFrame.grid(column=0, columnspan=5, row=0, sticky="ew")
        # create an Obj for projection-choise 2D or 3D, put it to the given lbl with the "plotGraph" callback function
        self.obj_projectionGUI = ProjectionGUI(self.lbl_insideOfLeftFrame,self.plotGraph)
        self.obj_projectionGUI.choice.set(D_PROJECTION)

        # create a labelFram inside of leftframe, load function expression's from 'obj_MenuBarGUI'  
        self.lblf_inputField = tk.LabelFrame(self.leftFrame,text="Inputfield\t\t\t")
        self.lblf_inputField.grid(column=0, columnspan=5, row=6, sticky="ew")
        defaulExpressionList = [self.obj_MenuBarGUI.obj_configuration.config_dictionary['3D']['f'],
                                self.obj_MenuBarGUI.obj_configuration.config_dictionary['2D']['i_properties']['f1']['f'],
                                self.obj_MenuBarGUI.obj_configuration.config_dictionary['2D']['i_properties']['f2']['f'],
                                self.obj_MenuBarGUI.obj_configuration.config_dictionary['2D']['i_properties']['f3']['f'],
                                self.obj_MenuBarGUI.obj_configuration.config_dictionary['2D']['i_properties']['f4']['f']]
        # create an "obj_inputFieldGUI" & put it to the created 'lblf_inputField'
        self.obj_inputFieldGUI = InputFieldGUI(self.lblf_inputField,\
                                               self.obj_projectionGUI.getProjectionChoice(),\
                                               defaulExpressionList)
        
        # programm will always start with '3D' view. so create an obj_config3dGUI     
        self.obj_config3dGUI = Config3dGUI(self.lbl_insideOfLeftFrame,self.plotGraph,\
                                self.obj_MenuBarGUI.obj_configuration.config_dictionary)
        self.id__config3dGUI = 1 # indication flag that the '3D' view is present
        self.obj_Config2dGUI = None 
        self.id__Config2dGUI = 0 # indication flag that the '3D' view is'nt present
        
        # create a button for upate
        btn_plot = tk.Button(self.mainFrame,text='Apply changes and update plot',command=self.plotGraph)
        btn_plot.grid(column=0,columnspan=2,row=10,sticky="sew")
        btn_plot.configure(padx=30,pady=15,background='#bbbbbb')     
        self.plotGraph()

        self.window.protocol("WM_DELETE_WINDOW", self.obj_MenuBarGUI.exit_application)
        pass

        
    def run(self):
        """method for runing of the application"""
        self.window.mainloop()

            
        
    def plotGraph(self):
        """ this is a callback function to update plot area """
        # update entries visibality and clear convas according to the chosed projection
        projectionStr = self.obj_projectionGUI.getProjectionChoice()
        self.obj_inputFieldGUI.setProjection(projectionStr)
        self.clearConvasForNewPlot()  
        # handle function regarding to the chosed function
        if projectionStr == '2D':
            self.obj_MenuBarGUI.projection = '2D'
            self.alternate_3D2D_View('2D',self.obj_MenuBarGUI.obj_configuration.config_dictionary)           
            self.handle2DFig()
        else:
            self.obj_MenuBarGUI.projection = '3D'
            self.alternate_3D2D_View('3D',self.obj_MenuBarGUI.obj_configuration.config_dictionary)
            self.handle3DFig()
        # put handled fig to the convas
        self.putFigToCanvas()
        
        
    def clearConvasForNewPlot(self):
        """ this function clear convas to make place for new plot """
        if(len(self.canvas.get_tk_widget().find_all())>0):
            for item in self.canvas.get_tk_widget().find_all():
                if(item > 0):
                    try:
                        self.canvas.get_tk_widget().destroy()
                        self.toolbar.destroy()
                    except ValueError:
                        print("Convas is already destroyed")
        else:
            return
        

        
                
    def putFigToCanvas(self):
        """(1) update canvas & add figure to the convas,
           (2) placing the canvas on the Tkinter window
           (3) add and bild function-toolbar from "matplotlib.backends.backend_tkagg" lib"""         
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphFrame) #(1)
        self.canvas.draw()      
        self.canvas.get_tk_widget().pack() #(2)       
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.graphFrame)#(3)
        self.toolbar.update()
        self.obj_MenuBarGUI.updateToolbar(self.toolbar)


    def alternate_3D2D_View(self,projectionStr,refToDictionary):
        """if user change view from 3D to 2D or otherwise  
           this function will be used to alternate view for 2D or 3D destory
           and create needed obj for the view  """
        if projectionStr=='2D':
            if (self.id__config3dGUI != 0):
                self.obj_config3dGUI.destroy()
                self.id__config3dGUI = 0
                self.obj_Config2dGUI = Config2dGUI(self.lbl_insideOfLeftFrame,self.plotGraph,refToDictionary)
                self.obj_Config2dGUI.choosedFunction.set(refToDictionary['2D']['i_properties']['f1']['legendname'])
                self.id__Config2dGUI = 1
                oldFunctionList = self.obj_inputFieldGUI.getFunStrList()
                oldCheckList = self.obj_inputFieldGUI.getListStateOfChecks()
                self.obj_inputFieldGUI.destroy()
                self.obj_inputFieldGUI = InputFieldGUI(self.lblf_inputField,'2D',oldFunctionList,self.plotGraph)
                self.obj_inputFieldGUI.setListStateOfChecks(oldCheckList)
        else:
            if (self.id__Config2dGUI != 0):
                self.obj_Config2dGUI.destroy()
                self.id__Config2dGUI = 0
                self.obj_config3dGUI = Config3dGUI(self.lbl_insideOfLeftFrame,self.plotGraph,refToDictionary)
                self.id__config3dGUI = 1
                oldFunctionList = self.obj_inputFieldGUI.getFunStrList()
                oldCheckList = self.obj_inputFieldGUI.getListStateOfChecks()
                self.obj_inputFieldGUI.destroy()
                self.obj_inputFieldGUI = InputFieldGUI(self.lblf_inputField,'3D',oldFunctionList)
                self.obj_inputFieldGUI.setListStateOfChecks(oldCheckList)
        return

#####################################################################################################################
#                    3D Handling section , 3D can only handle func Expression not data from table                   #
#####################################################################################################################
    def handle3DFig(self):
        """ function for handling 3D expression """
        # remove old plots
        for item in self.fig.axes:
            self.fig.delaxes(item)
        #init new figure           
        self.fig = Figure(figsize=(6,6), dpi=100)   
        ax = self.fig.add_subplot(projection='3d')
        #create a locale Function3D object to genarate x,y,z data
        ob3D = Function3D()
        # read function expression from inputFieldGUI object, 
        funStr = self.obj_inputFieldGUI.getFunStrList()[0]
        refToDictionary = self.obj_MenuBarGUI.obj_configuration.config_dictionary
        # check wheather user want to plot from ConfigFile? 
        if(self.obj_MenuBarGUI.loadFlag==True):        
            self.obj_config3dGUI.set3Dproperties(refToDictionary)
            funStr = refToDictionary['3D']['f']  
            self.obj_inputFieldGUI.f3Dstr.set(funStr)
            self.obj_MenuBarGUI.loadFlag = 0
        else:
            refToDictionary['3D'] = self.obj_config3dGUI.get3DProperties(funStr)['3D']
        p = refToDictionary['3D']['properties']
        if funStr != '':
            try:               
                ob3D.generateDataFromExpression(funStr,float(p['xyMin']),float(p['xyMax']))
                if(self.obj_config3dGUI.getChoice()=='wireframe'):
                    ax.plot_wireframe(ob3D.x,ob3D.y,ob3D.z,color='black')
                if(self.obj_config3dGUI.getChoice()=='scatter'):
                    ax.scatter3D(ob3D.x,ob3D.y,ob3D.z,color='black')
                if(self.obj_config3dGUI.getChoice()=='surface'):
                    ax.plot_surface(ob3D.x,ob3D.y,ob3D.z,cmap=plt.cm.jet)
                if(self.obj_config3dGUI.getChoice()=='binary'):
                    ax.plot_surface(ob3D.x,ob3D.y,ob3D.z,cmap='binary')
                if(self.obj_config3dGUI.getChoice()=='conour3D'):
                    ax.contour3D(ob3D.x,ob3D.y,ob3D.z,cmap='binary')                                 
                ax.set_xlabel(p['xLabel'])
                ax.set_ylabel(p['yLabel'])
                ax.set_zlabel(p['zLabel'])
                ax.set_title(p['title'])
            except Exception:
                msg_box = tk.messagebox.showinfo( 'Invalid input Error!',\
                                                  'xyMin, xyMax must be a num! also pay attention \
                                                   that functionexpression contians only x and y',icon='warning')
        else :
            msg_box = tk.messagebox.showinfo( 'Invalid input Error!','Inputfield is empty please type a 3D function in it',icon='warning')     
        return None 

#####################################################################################################################
#                        2D handling section , 2D can  handle func Expression and data from table                   #
#####################################################################################################################
    def handle2DFig(self):
        """ this function handle 2Dfunction in general, wheather the data is given or the expression. 
            it use member variable 'fileOpenedFlag' from 'obj_Menubar' to detect, wheather to call 
            'handle2DFromExpression' or 'handle2DFromFile' function """         
        refToDictionary = self.obj_MenuBarGUI.obj_configuration.config_dictionary
        self.update2DConfigDictionaryIfUserUploadedConfigFile(refToDictionary)       
        # remove old plots
        for item in self.fig.axes:
            self.fig.delaxes(item)

        # indication that the user uploaded data for plotting
        if(self.obj_MenuBarGUI.fileOpenedFlag==True):
            legendList = self.handle2DFromFile(self.obj_MenuBarGUI.filename,refToDictionary)
            self.obj_MenuBarGUI.fileOpenedFlag=False    
        else:
            # if all check-buttons from 'obj_inputFieldGUI' is unchecked & filename is still present
            # its allso an indication that the user want to plott data from detected filname, 
            # it will be the case, like changing title,color, linestyle etc.. while filename is present
            if(self.obj_inputFieldGUI.var_check1.get()==0 and\
               self.obj_inputFieldGUI.var_check2.get()==0 and\
               self.obj_inputFieldGUI.var_check3.get()==0 and\
               self.obj_inputFieldGUI.var_check4.get()==0 and\
               self.obj_MenuBarGUI.filename!= None ):
                    legendList = self.handle2DFromFile(self.obj_MenuBarGUI.filename,refToDictionary)
            else:       
                self.handle2DFromExpression(refToDictionary)
                legendList = self.handleLegend(refToDictionary)
     
        if(self.obj_Config2dGUI.var_checkLog.get()):
            plt.yscale('log')
        if(self.obj_Config2dGUI.var_checkGrid.get()):
            plt.grid('on')        
        if(self.obj_Config2dGUI.var_checkLegend.get()):        
            plt.legend(legendList) 
        plt.xlabel(refToDictionary['2D']['g_properties']['xLabel'])
        plt.ylabel(refToDictionary['2D']['g_properties']['yLabel'])
        plt.title(refToDictionary['2D']['g_properties']['title'])
        return

    def update2DConfigDictionaryIfUserUploadedConfigFile(self,refToDictionary):
        """ to update all 2D properties & 'self.obj_inputFieldGUI'
            from refrenced dictionary json.file """
        if(self.obj_MenuBarGUI.loadFlag==True):                 
             self.obj_Config2dGUI.set2Dproperties(refToDictionary)
             # update inputfield entries from refrenced dictionary json file
             funStrList = [refToDictionary['3D']['f'],\
                           refToDictionary['2D']['i_properties']['f1']['f'],\
                           refToDictionary['2D']['i_properties']['f2']['f'],\
                           refToDictionary['2D']['i_properties']['f3']['f'],\
                           refToDictionary['2D']['i_properties']['f1']['f'] ] 
             self.obj_inputFieldGUI.setFuncStr(funStrList)
                # update all 2D properties from GUI "2D View widget"
        else:
            refToDictionary['2D'] = self.obj_Config2dGUI.get2DProperties()
        return


    def handle2DFromExpression(self,refToDictionary):
        """ this function handle user expression und save changes to the refreced dicitonary"""
        # create 4 obj from Function2D class  
        tmpObjF2D = [Function2D() for i in range(1,5)] 
        # get expression and Check-button status from inputfield-objekt   
        tupelOfFuncExpressionWithCheckStatus = self.obj_inputFieldGUI.get2DFunStrPlusCheck()
        self.fig = plt.figure(figsize=(6,6), dpi=100)
        for i in range(1,5):
            funExp,check = tupelOfFuncExpressionWithCheckStatus[i-1]
            # save func-expression changes from GUI to the refreced dictionary
            refToDictionary['2D']['i_properties']['f'+str(i)]['f'] = funExp
            if(funExp!='' and check !=0):
                l = refToDictionary['2D']['i_properties']['f'+str(i)]['linestyle']
                w = refToDictionary['2D']['i_properties']['f'+str(i)]['linewidth']
                c = refToDictionary['2D']['i_properties']['f'+str(i)]['color'] 
                try:
                    x_Start =  float(refToDictionary['2D']['g_properties']['xMin'])
                    x_End   =  float(refToDictionary['2D']['g_properties']['xMax'])
                    x_step  =  float(refToDictionary['2D']['g_properties']['xStep'])
                except:
                    tk.messagebox.showinfo( 'Invalid input Error!','xStep, xMin & xMax must be a number! :)',icon='info')
                    plt.plot(0,0)
                    return
                log =  self.obj_Config2dGUI.var_checkLog.get()
                tmpObjF2D[i-1].generateDataFromExpression(funExp,x_Start,x_End,x_step,log)     
                plt.plot(tmpObjF2D[i-1].x,tmpObjF2D[i-1].y,linestyle=l,linewidth=w,color=c)
                plt.xlabel(refToDictionary['2D']['g_properties']['xLabel'])
                plt.ylabel(refToDictionary['2D']['g_properties']['yLabel'])
                plt.title(refToDictionary['2D']['g_properties']['title'])
        return

    def handle2DFromFile(self,dataFileName,refToDictionary):
        """this function handle user data und save changes to the refreced dicitonary"""
        # create an obj form Function2D class to use it's function to handle data from file
        tmpObj2D = Function2D()
        # create a figure for plotting & uncheck all check-button's  
        self.fig = plt.figure(figsize=(6,6), dpi=100)
        self.obj_inputFieldGUI.var_check1.set(0)
        self.obj_inputFieldGUI.var_check2.set(0)
        self.obj_inputFieldGUI.var_check3.set(0)
        self.obj_inputFieldGUI.var_check4.set(0)
        # extract only file name for viewing issu, the path will be ignored
        # for example C:blalba\bjala\data.txt -> data.txt 
        filename_only = ntpath.basename(dataFileName)
        # calling tmObj2D.generat... will create to numpy arrays und record it in
        # member variable of tmpObj2D.x und tmpObj2D.y
        tmpObj2D.generateDataFromFileTxt(dataFileName)
        # save changes to the refrenced dictionary and plot data 
        try:            
            xStep = round(tmpObj2D.x[1]-tmpObj2D.x[0],3)
            refToDictionary['2D']['g_properties']['xStep']   = xStep
            refToDictionary['2D']['g_properties']['xMin']    = tmpObj2D.x[0]
            refToDictionary['2D']['g_properties']['xMax']    = round(tmpObj2D.x[-1] + xStep,1)
            refToDictionary['2D']['g_properties']['title']   = filename_only
            refToDictionary['2D']['i_properties']['f1']['f'] = filename_only
            self.obj_inputFieldGUI.entry_f1.delete(0,tk.END)
            self.obj_inputFieldGUI.entry_f1.insert(0,filename_only)
            refToDictionary['2D']['i_properties']['f1']['legendname'] = filename_only
            refToDictionary['2D']['i_properties']['f1']['color'] = self.obj_Config2dGUI.color.get()
            self.obj_Config2dGUI.set2Dproperties(refToDictionary)
            l = self.obj_Config2dGUI.menuLinstyle.get()
            w = self.obj_Config2dGUI.menuLinwidth.get()
            c = self.obj_Config2dGUI.color.get()
            plt.plot(tmpObj2D.x,tmpObj2D.y,'ro')
            plt.plot(tmpObj2D.x,tmpObj2D.y,linestyle=l,linewidth=w,color=c)          
        except:
            self.obj_Config2dGUI.menuLinstyle.set('solid')
            self.obj_Config2dGUI.menuLinwidth.set('1')
            self.obj_Config2dGUI.color.set('#07f73b')
            self.obj_Config2dGUI.btnColorChooser.configure(background='#07f73b')
            l = 'solid'
            w = '1'
            c = '#07f73b'
            plt.plot(tmpObj2D.x,tmpObj2D.y,'ro')
            plt.plot(tmpObj2D.x,tmpObj2D.y,linestyle=l,linewidth=w,color=c)
        finally:
            return [self.obj_Config2dGUI.legendName.get(),'linear Interpolation']
            

    def handleLegend(self,refToDictionary):
        """ its a helper method for handling legend-list, this function try to create a 
            legend-list from refrenced dictionary und return the created legend-list """     
        legendList = []
        try:
            if(self.obj_inputFieldGUI.var_check1.get()):
                legendList.append(refToDictionary['2D']['i_properties']['f1']['legendname'])
            if(self.obj_inputFieldGUI.var_check2.get()):
                legendList.append(refToDictionary['2D']['i_properties']['f2']['legendname'])
            if(self.obj_inputFieldGUI.var_check3.get()):
                legendList.append(refToDictionary['2D']['i_properties']['f3']['legendname'])
            if(self.obj_inputFieldGUI.var_check4.get()):
                legendList.append(refToDictionary['2D']['i_properties']['f4']['legendname'])
        except KeyError:
            print("Some Legendname not found! ")
        finally:
            return legendList  
            