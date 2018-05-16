from faker import Faker
import csv
import random
import pandas as pd
class generateFake():
    def Fake(self):
        self.id = 1
        self.fake = Faker ()
        self.interest = ['python','JS','QA','PHP']
        self.qualification = ['Bachelors','+2','Masters']
        self.level = ['Entry','Mid','Senior']
        self.companylist = ['Leapfrog','Aayulogic','Deerwalk', 'F1soft']
        self.labels = ['Id','Age','Interest','Qualification','Experience','Level','Company']
        self.data = pd.DataFrame(columns=self.labels, index=None)
        for i in range(1000):
            row = []
            row.append(self.id)
            row.append(random.randint(20,45))
            self.f_interest= random.choice(self.interest)
            row.append(self.f_interest)
            row.append(random.choice(self.qualification))
            row.append(random.randint(0,5))
            if row[4]==0:
                self.f_level= self.level[0]
                row.append(self.f_level)
            elif row[4]<=2:
                self.f_level= self.level[1]
                row.append(self.f_level)
            else:
                self.f_level= self.level[2]
                row.append(self.f_level)
            self.id += 1
            
            row.append(random.choice(self.companylist))
            self.data.loc[i]= row
        return(self.data)
if __name__ == '__main__':
    fak = generateFake()
    df=fak.Fake()
    df.set_index('Id',inplace=True)
    #df.to_csv('src/data/data.csv', sep=',')