import pandas as pd

class preProcessor():
    def __init__(self, *args, **kwargs):
        self.jobdata = args[0]
        pass
    
    def columnSelector (self,traindata,testdata):
        matching = set(traindata) - set(testdata)
        remove= list(matching)
        traindata.drop(remove,axis=1, inplace=True)
        order = list(traindata)
        testdata = testdata[order]
        return traindata,testdata
    
    def makeList(self,similar):
        jobList=[]
        df= pd.DataFrame(similar)
        df['freq'] = df.groupby(0)[0].transform('count')
        df.drop_duplicates(0)
        df.sort_values(1, ascending=False)
        df.values.tolist()
        for each in similar:
            job = self.jobdata.loc[each[0]]
            jobdict= job.to_dict()
            jobdict['Jobid']= each[0]
            jobdict['similarity']= each[1]
            jobList.append(jobdict)
        return jobList

    def usertouser(self):
        pass

    def usertocompany(self):
        pass

    def companytocompany(self):
        pass
