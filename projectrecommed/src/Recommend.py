import csv
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.Recommenders.Collaborative import CollaborativeRec
from src.Recommenders.Content import ContentRec
class Recommend():
    def __init__(self, *args, **kwargs):
        self.test= args[0]
        self.category= args[1]
        self.csvReader(self.category)
        self.collab= CollaborativeRec(self.userdata,self.jobdata, self.test) 
        #self.content= ContentRec(self.jobdata,self.test)
    
    def readData(self,id):
        #Read test,user,job json data or csv data
        #call collab
        #return json
        pass

    def getData(self):
        data = self.collab.getRecord()
        return data


    def csvReader(self,path):
        #Define relative path for csv files
        self.userdata = pd.read_csv(f'src/data/{path}/finalUser.csv')
        self.userdata.set_index('UserId',inplace = True)
        self.jobdata = pd.read_csv(f'src/data/{path}/finalJob.csv')
        self.jobdata.set_index('Jobid',inplace = True)
