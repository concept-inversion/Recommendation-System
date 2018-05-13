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
        self.csvReader()
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


    def csvReader(self):
        #Define relative path for csv files
        self.userdata = pd.read_csv('src/data/finalUser.csv')
        self.userdata.set_index('UserId',inplace = True)
        self.jobdata = pd.read_csv('src/data/finalJob.csv')
        self.jobdata.set_index('Jobid',inplace = True)

if __name__== '__main__':
    testdata = {'php': 1, 'python': 1, 'qualification': 2, 'xperience': 5,'level': 2, 'age': 25}
    frame = pd.DataFrame.from_dict([testdata])
    a= Recommend(testdata)
    print(a)