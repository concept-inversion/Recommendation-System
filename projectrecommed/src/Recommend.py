import csv
import pandas as pd
import os
from Recommenders.Collaborative import CollaborativeRec

class Recommend():
    def __init__(self, *args, **kwargs):
        self.userId= args[0]
        self.csvReader()
        self.collab= CollaborativeRec(self.userdata,self.jobdata, self.test,self.userId)

    def getData(self,id):
        #Read test,user,job json data or csv data
        #call collab
        #return json
        pass

    def csvReader(self):
        self.userdata = pd.read_csv('projectrecommed/src/data/finalUser.csv')
        self.userdata.set_index('UserId',inplace = True)
        self.jobdata = pd.read_csv('projectrecommed/src/data/finalJob.csv')
        self.jobdata.set_index('Jobid',inplace = True)
        self.test= self.userdata.iloc[[1]]
        print(self.userdata.head())

if __name__ == '__main__':
    print(os.getcwd())
    a = Recommend(23)
