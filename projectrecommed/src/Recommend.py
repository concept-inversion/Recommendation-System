import csv
import pandas as pd
#from src.Recommenders.Collaborative import CollaborativeRec
from .Recommenders.Collaborative import CollaborativeRec
class Recommend():
    def __init__(self, *args, **kwargs):
        self.userId= args[0]
        self.csvReader()
        #self.collab= CollaborativeRec()
        
    
    def getData(self,id):
        #Read test,user,job json data or csv data
        #call collab
        #return json
        pass
    def csvReader(self):
        userdata = pd.read_csv('/data/finalUser.csv')
        jobdata = pd.read_csv('/data/finalJob.csv')

if __name__ == '__main__':
    a = Recommend()