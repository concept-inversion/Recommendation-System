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
        self.preProcessor = preProcessor(self.jobdata,self.test)
    
    # function that ineract with Recommend.py
    def getRecord(self):  
        #joblist1=self.user2user()
        joblist2=self.user2company()
        #logic to combine both result
        #joblist = joblist1 + joblist2
        return self.preProcessor.makeList((joblist2))
        
    def user2user(self):
        self.similar= []
        #need to slice userdata according to the test data
        self.userdata, self.test= self.preProcessor.columnSelector(self.userdata, self.test)
        #get user similarity data
        self.cos= CosineSimilarity(self.userdata,self.test)
        self.similar = self.cos.calculate_cosine()
        #import ipdb; ipdb.set_trace()
        jobList= []
        for each in self.similar:
            #find the job Id from user Id
            jobId= self.jobMapper[each[0]]
            Similarity= each[1]
            jobList.append((jobId,Similarity))
            #find job in self.job
        return jobList

    #item to item based
    def user2company(self):
        self.similar= []
        jobdata= self.jobdata.copy()
        testdata=  self.test.copy() 
        self.jobdata_train, self.test_train= self.preProcessor.columnSelector(jobdata,testdata)
        #get user to company similarity data
        self.cos= CosineSimilarity(self.jobdata_train,self.test_train)
        self.similar = self.cos.calculate_cosine()
        return self.similar
   
