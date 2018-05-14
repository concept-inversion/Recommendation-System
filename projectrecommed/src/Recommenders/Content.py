import os
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from Algorithms.Cosine import CosineSimilarity
from data.dataPreprocesser import preProcessor

class ContentRec():
    def __init__(self, *args, **kwargs):
        # Information of jobs : key = jobId
        self.jobdata= args[1]
        self.test= args[2]
        #jobMapper must be a (userId,jobId)
        self.preProcessor = preProcessor(self.jobdata)
    
    def company2company(self):
        self.similar= []
        self.jobdata, self.test= self.preProcessor.columnSelector(self.jobdata, self.test)
        #get company to company similarity data
        self.cos= CosineSimilarity(self.jobdata,self.test)
        #would not work for multiple row
        self.similar = self.cos.calculate_cosine()
        jobList=[]
        # extract maximum from each row