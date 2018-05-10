#from Algorithms.Cosine import CosineSimilarity
#from src.Algorithms.Cosine import CosineSimilarity
#from Algorithms import Cosine
#from Cosine import CosineSimilarity
from src import CosineSimilarity

class CollaborativeRec():
    def __init__(self, *args, **kwargs):
        self.userdata = args[0]
       # Information of jobs : key = jobId
        self.job = args[1]
        self.test = args[2]
        
    def preProcess(self):
            self.getRecord()
            #jobMapper must be a touple of (userId,jobId)
            self.jobMapper = []
            pass 

    def getRecord(self):  
        self.similar = []  
        self.similar = CosineSimilarity(self.userdata,self.test)
        jobList = []
        for each in self.similar:
            #find the job Id from user Id
            jobId = self.jobMapper[each[0]]
            #find job in self.job
            jobList.append((self.job[jobId],each[1]))
            #put job, value in json
            pass