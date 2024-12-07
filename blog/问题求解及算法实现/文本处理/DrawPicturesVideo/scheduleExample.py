# import sched Python3 原生支持
# import time

# s = sched.scheduler(time.time,time.sleep)


# def job():
#     print(time.time(),"I'm working...")

# while True:
#     s.enter(5,1,job())
#     time.sleep(1)


import schedule
import time

# Api Link: https://schedule.readthedocs.io/en/stable/api.html
#           https://schedule.readthedocs.io/en/stable/
def job():
    print("I'm working...")
    
schedule.every(5).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)