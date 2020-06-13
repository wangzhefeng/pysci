

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule
import time

def job_ten_min():
	print("I'm working ten min.")

def job_hour():
	print("I'm working per hour")

def job_day_ten_thirty():
	print("I'm working per day at 10:30")

def job_per_monday():
	print("I'm working per monday")

def job_per_wednesday():
	print("I'm working per wednesday at 13:15")

def job_per_min():
	print("I'm wroking per min at 17 sec")



schedule.every(10).minutes.do(job_ten_min)
schedule.every().hour.do(job_hour)
schedule.every().day.at("10:30").do(job_day_ten_thirty)
schedule.every().monday.do(job_per_monday)
schedule.every().wednesday.at("13:15").do(job_per_wednesday)
schedule.every().minute.at(":17").do(job_per_min)

while True:
	schedule.run_pending()
	time.sleep(1)
```