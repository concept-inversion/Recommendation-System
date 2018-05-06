from faker import Faker
import csv
import random
class generateFake():
    def Fake(self):
        self.id = 1
        self.fake = Faker ()
        self.interest = ['python','JS','QA','PHP']
        self.qualification = ['Bachelors','+2','Masters']
        csvfile = open('src/data/data.csv', 'wb')
        csvwriter = csv.writer(csvfile,delimiter = ',')
        for i in range(10):
            row = []
            row.append(self.id)
            row.append(random.randint(20,45))
            row.append(random.choice(self.interest))
            row.append(random.choice(self.qualification))
            self.id += 1
            csvwriter.writerow(row,.join())
        csvfile.close()

if __name__ == '__main__':
    fak = generateFake()
    fak.Fake()
    