import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

class KNNeighbour():
    def __init__(self,*args, **kwargs):
       self.test = args[0]
       self.train = args[1] 
       self.calculate_Knn()
    
    def calculate_Knn(self):
        knn = KNeighborsClassifier()
        knn.fit(self.test,self.train)
        knn.predict(self.t)