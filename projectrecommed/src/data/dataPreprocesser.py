import pandas as pd

class preProcessor():
    def __init__(self, *args, **kwargs):
        self.jobdata = args[0]
        self.test= args[1]
    
    def columnSelector (self,traindata,testdata):
        
        # remove same field form both datasets 
        uniquetrain = set(traindata) - set(testdata)
        # change set to list
        remove= list(uniquetrain)
        # remove fields in traindata i.e not in both dataset
        traindata.drop(remove,axis=1, inplace=True)

        uniquetest = set(testdata)- set(traindata)
        remove2= list(uniquetest)
        testdata.drop(remove2,axis=1, inplace=True)
        # get list of remaining columns from traindata
        order = list(traindata)

        # order testdata coulms same as traindata column
        testdata = testdata[order]
        #import ipdb; ipdb.set_trace()
        return traindata,testdata
    
    def makeList(self,similar):
        jobList=[]
        df= pd.DataFrame(similar)
        #frequency count
        #df['freq'] = df.groupby(0)[0].transform('count')
        data = df.drop_duplicates(0)
        similar= data.values.tolist()  
        #import ipdb; ipdb.set_trace()
        for each in similar:
            job = self.jobdata.loc[each[0]]
            similarity= self.similarityCalculator(each[0])
            jobdict= job.to_dict()
            jobdict['Jobid']= each[0]
            jobdict['similarity']= similarity
            jobList.append(jobdict)
        return jobList

    def similarityCalculator(self,data):
        job = self.jobdata.loc[[data]]
        job= job.drop(['company','jobtitle'],axis=1)
        missing = list(set(job)-set(self.test))
        for each in missing:
            self.test[each]=0 
        job,user = self.columnSelector(job,self.test)
        job= job.values.tolist()[0]
        user= user.values.tolist()[0]
        score = 0
        for i in range(len(job)):
            if user[i]== job[i]:
                score += 0.1428
            elif (job[i]-user[i])==1:
                score-=0.05
            elif (job[i]-user[i])==2:
                score-= 0.06

            elif (job[i]-user[i])==3:
                score-= 0.07
            
            elif (job[i]-user[i])> 3:
                score-= 0.1
        return round(score,4)


    def usertouser(self):
        pass

    def usertocompany(self):
        pass

    def companytocompany(self):
        pass
