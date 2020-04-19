import datetime
import time

def convert_time_to_string(dt):
	if dt.hour <= 9:
		return f"0{dt.hour}:{dt.minute:02}"
	else:
		return f"{dt.hour}:{dt.minute:02}"

def time_has_changed(prev_time):
	now = time.time()
	now = now + (60*60*3) #+3 hours to my Virtual Machine time. You may add or sub any amount of time
	now = now % (60*60*24)						#depending on your local time.
	now = time.strftime('%H:%M', time.localtime(now))
	return now != prev_time
