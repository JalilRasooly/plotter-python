import sys
import os
import pathlib
sys.path.insert(0,os.path.join(pathlib.Path(__file__).parent,"Classes"))
sys.path.insert(1,os.path.join(pathlib.Path(__file__).parent,"Classes_GUI"))

from mainWindowGUI_V11 import MainProgramWindow as plottApp
# ******************* INFO *****************************
# make sure that your virtuale envirument is activated! 
# and your in the current directory where test.py is located
# your terminal should look like this:
#        (plotProject_venv) PS C:\......\src_plotproject>
# to run the aplicaiton just write : 'py test.py' or 'python test.py'
#        (plotProject_venv) PS C:\......\src_plotproject>py test.py
#        or
#        (plotProject_venv) PS C:\......\src_plotproject>py test.py
# and hit the 'Enter' keyboard

strOut =\
" #############################################################\n\
  #  pyt_WS_22_23                                             #\n\
  #  Jalil Rasooly                                            #\n\
  #  25.Dez.2022 Version V.11                                 #\n\
  #############################################################\n"

print(strOut,"\n")

# proof of concept 
print("#############################################################")
print("#   Program started.....                                   #")
print("#############################################################\n")
myPlotter = plottApp()
myPlotter.run()
