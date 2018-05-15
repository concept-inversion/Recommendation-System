import pandas as pd

class preProcessor():
    def __init__(self, *args, **kwargs):
        self.jobdata = args[0]
        pass
    
    def columnSelector (self,traindata,testdata):
        
        # remove same field form both datasets 
        matching = set(traindata) - set(testdata)

        # change set to list
        remove= list(matching)

        # remove fields in traindata i.e not in both dataset
        traindata.drop(remove,axis=1, inplace=True)

        # get list of remaining columns from traindata
        order = list(traindata)

        # order testdata coulms same as traindata column
        testdata = testdata[order]

        return traindata,testdata
    
    def makeList(self,similar):
        jobList=[]
        df= pd.DataFrame(similar)
        df['freq'] = df.groupby(0)[0].transform('count')
<<<<<<< HEAD
        a= df.drop_duplicates(0)
        a.sort_values(1, ascending=False)
        a.values.tolist()
=======
        df.drop_duplicates(0)
        ### only shows duplicate donot impact in dataframe
        df.sort_values(1, ascending=False)
        ## why to list not impacting aything on dataframe
        df.values.tolist()
>>>>>>> documentation
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
