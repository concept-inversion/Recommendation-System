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
        for i in range(2):
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
            company = []
            company.append(random.choice(self.companylist))
            company.append(self.f_interest)
            
            company.append(self.f_level)
            row.append(company)
            data.append(row)

if __name__ == '__main__':
    fak = generateFake()
    fak.Fake()
    