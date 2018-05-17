import schedule
import time
import requests
import json
import csv
from ast import literal_eval
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
endpoint = 'https://b7f7c9c9-a10f-47fe-8d88-6efdfe76df0e.mock.pstmn.io/test2'
print(os.getcwd())
def addtoCsv(data):
    f = csv.writer(open("projectrecommed/src/data/test.csv", "w+"))
    print('loaded')
    
    #Jobid,Experience,php,python,qa,js,level,qualification,company,jobtitle
    #data['Jobid']
    
    f.writerow([
        
        data["Experience"],
        data["php"],
        data["python"],
        data["qa"],
        data["js"],
        data["level"],
        data["qualification"],
        data["company"],
        data["jobtitle"]
         ])


def job():
    response =requests.get(endpoint)
    js= response.content
    temp= literal_eval(js.decode('utf8'))

    data = json.loads(temp)
    addtoCsv(data)
schedule.every(1).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("12:00").do(job)

while True:
    schedule.run_pending()



