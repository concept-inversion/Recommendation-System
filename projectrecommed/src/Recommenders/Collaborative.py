import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from Algorithms.Cosine import CosineSimilarity
from data.dataPreprocesser import preProcessor

class CollaborativeRec():
    def __init__(self, *args, **kwargs):
        self.userdata = args[0]
        # Information of jobs : key = jobId
        self.jobdata= args[1]
        self.test= args[2]
        #jobMapper must be a (userId,jobId)
        self.jobMapper= self.userdata['Jobid']
        self.preProcessor = preProcessor()
    
    # function that ineract with Recommend.py
    def getRecord(self):  
        joblist1=self.user2user()
        joblist2=self.user2company()
        joblist = joblist1 + joblist2
        for each in joblist2:
            print(each)
        #filter the list

        
        
        
        
    def user2user(self):
        self.similar= []
        #need to slice userdata according to the test data
        self.userdata, self.test= self.preProcessor.columnSelector(self.userdata, self.test)
        #get user similarity data
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
            
    #item to item based
    def user2company(self):
        self.similar= []
        self.jobdata, self.test= self.preProcessor.columnSelector(self.jobdata, self.test)
        #get user to company similarity data
        self.cos= CosineSimilarity(self.jobdata,self.test)
        self.similar = self.cos.calculate_cosine()
        jobList=[]
        jobjson={}
        for each in self.similar:
            job = self.jobdata.loc[each[0]]
            jobdict= job.to_dict()
            jobdict['Jobid']= each[0]
            jobjsontemp = {'jobdata':jobdict,'similarity':each[1]}
            jobList.append(jobjsontemp)
        return jobList
           