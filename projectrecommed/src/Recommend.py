import csv
import pandas as pd
import os
from Recommenders.Collaborative import CollaborativeRec

class Recommend():
    def __init__(self, *args, **kwargs):
        self.test= args[0]
        self.csvReader()
        self.collab= CollaborativeRec(self.userdata,self.jobdata, self.test,self.userId)

    def getData(self,id):
        #Read test,user,job json data or csv data
        #call collab
        #return json
        pass

    def csvReader(self):
        #Define relative path for csv files
        self.userdata = pd.read_csv('data/finalUser.csv')
        self.userdata.set_index('UserId',inplace = True)
        self.jobdata = pd.read_csv('data/finalJob.csv')
        self.jobdata.set_index('Jobid',inplace = True)

if __name__ == '__main__':
    print(os.getcwd())
    a = Recommend(test)
