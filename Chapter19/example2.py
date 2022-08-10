import time
from datetime import datetime
from apscheduler.schedulers.background import BlockingScheduler


def tick():
    print("Tick! The time is: {0}".format(datetime.now()))


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()

    try:
        while True:
            time.sleep(2)
            print("Printing in the main thread.")
    except KeyboardInterrupt:
        pass

    scheduler.shutdown()
