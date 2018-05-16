import schedule
import time
import requests

def job():
    print("I'm working...")
    
schedule.every(5).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("12:00").do(job)

while True:
    schedule.run_pending()