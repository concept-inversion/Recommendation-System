import pandas as pd

class preProcessor():
    def __init__(self, *args, **kwargs):
        pass
    
    def columnSelector (self,traindata,testdata):
        matching = set(traindata) - set(testdata)
        remove= list(matching)
        traindata.drop(remove,axis=1, inplace=True)
        order = list(traindata)
        testdata = testdata[order]
        return traindata,testdata
    
    def usertouser(self):
        pass

    def usertocompany(self):
        pass

    def companytocompany(self):
        pass
