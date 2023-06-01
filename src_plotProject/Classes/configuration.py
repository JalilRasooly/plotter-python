import json
import pathlib
import os

PROJECT_PATH = pathlib.Path(__file__).parent.parent      # .../src_project
CHILD_PATH_CONFIG = os.path.join(PROJECT_PATH,"config")  # .../src_project/config

#############################################################
#  Project: pyt_WS_22_23                                    #
#  Author : Jalil Rasooly                                   #
#  Date   : 02.01.2023                                      #
#############################################################
"""  all desired configuration is saved in "self.config_dictionary" , this attribute is used to handle 
    customizing issue und can save or manipulate properties according to the changes in GUI  """

class Configuration:
    def __init__(self):
        self.config_dictionary = 0
        self.setDefaultConfig()

    @classmethod
    def saveConfigAsJsonFile(self, fileName, dictionary):
        dic = 0
        if type(dictionary) == Configuration:
            dic = dictionary.config_dictionary
        else:
            dic = dictionary
        # Writing to configFile.json
        ConfigObject_json = json.dumps(dic, indent=4)
        with open(fileName, "w") as outfile:
            outfile.write(ConfigObject_json)

    @classmethod
    def loadUserChoosedConfig(self, filname, ref_ConfigObject,projection):
        # Opening JSON file
        with open(filname, 'r') as openfile:
            # Reading from json file and save it in refrenced object's attribute
            tmpDictionary = json.load(openfile)
            if(projection=='2D'):
                ref_ConfigObject.config_dictionary['2D'] = tmpDictionary['2D']
            else:
                ref_ConfigObject.config_dictionary['3D'] = tmpDictionary['3D']

    def setDefaultConfig(self):
        self.config_dictionary = {
            "3D": {
                "f": "sin(sqrt(x**2+y**2))",
                "graphtype": "surface",
                "properties": {
                    "xyMin": -10,
                    "xyMax": 10,
                    "xLabel": "x",
                    "yLabel": "y",
                    "zLabel": "z",
                    "title": "Demo 3D Function"
                }
            },
            "2D": {
                "g_properties": {
                    "xStep" : 0.01,
                    "xMin"  : 0,
                    "xMax"  : 10,
                    "xLabel": "x",
                    "yLabel": "y",
                    "title" : "Demo Default 2D Functions",
                    "grid"  : True,
                    "log"   : False,
                    "legend": True,
                },
                "i_properties": {
                    "f1": {"f"        : "2*sin(x)",
                           "legendname": "sin",
                           "color": 'g',
                           "linestyle": "solid",
                           "linewidth": "2"   
                           },
                    "f2": {"f"        : "2*cos(x)",
                           "legendname": "cos",
                           "color": 'b',
                           "linestyle": "dotted",
                           "linewidth": "2"   
                           },
                    "f3": {"f"        : "exp(-x)",
                           "legendname": "e",
                           "color": 'r',
                           "linestyle": "dashed",
                           "linewidth": "2"   
                           },
                    "f4": {"f"        : "0.5*(x-6)",
                           "legendname": "linear",
                           "color": 'y',
                           "linestyle": "solid",
                           "linewidth": "2"   
                           },
                }
            }
        }
        Configuration.saveConfigAsJsonFile(str(os.path.join(CHILD_PATH_CONFIG,"defaultConig.json")), self.config_dictionary)
        pass
