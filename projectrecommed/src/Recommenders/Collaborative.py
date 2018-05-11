import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from Algorithms.Cosine import CosineSimilarity

class CollaborativeRec():
    def __init__(self, *args, **kwargs):
        self.userdata = args[0]
        # Information of jobs : key = jobId
        self.jobdata= args[1]
        self.test= args[2]
        self.preProcess()

    def preProcess(self):
            #jobMapper must be a (userId,jobId)
            self.jobMapper= self.userdata['Jobid']
            self.userdata.drop('Jobid',axis= 1, inplace= True)
            order =['experience','php','python','qa','js','level','qualification','age']
            self.test = self.test[order]
            # If Job is present
            #self.test.drop('Jobid',axis= 1, inplace= True)
            

    def getRecord(self):  
        self.similar= []
        self.cos= CosineSimilarity(self.userdata,self.test)
        self.similar = self.cos.calculate_cosine()
        jobList= []
        jobjson= {}
        for each in self.similar:
            #find the job Id from user Id
            jobId= self.jobMapper[each[0]]
            #find job in self.job
            job = self.jobdata.loc[jobId]
            #put job, value in dict
            jobdict= job.to_dict()
            jobdict['Jobid']= jobId
            jobjsontemp = {'jobdata':jobdict,'similarity':each[1]}
            jobList.append(jobjsontemp)
        return jobList
            
                   