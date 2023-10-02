import schedule
import time
import datetime

def task_minute():
    print("task based on minutes gets schedule at:",datetime.datetime.now())

def task_hour():
    print("task based on hour gets schedule at:",datetime.datetime.now())

def task_sunday():
    print("task based on day gets schedule at:",datetime.datetime.now())
    

    

def main():
    print("inside task scheduler")
    print("Current time is:",datetime.datetime.now())

    schedule.every(1).minutes.do(task_minute)
    schedule.every(1).hour.do(task_hour)
    schedule.every().sunday.at("15:58").do(task_sunday)


    

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()


