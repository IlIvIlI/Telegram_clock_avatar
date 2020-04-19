from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon import TelegramClient, sync, types
from telethon.tl.types import InputPhoto
from config import *
import time
from datetime import datetime
from datetime import timedelta
from utils import *

client = TelegramClient('Moscow_time', api_id, api_hash) #If you want, you may replace Moscow_time to any other name
client.start()

now = ''

while True:
	if time_has_changed(now):
		now = time.time()
		now = now + (60*60*3) #+3 hours to my Virtual Machine time. You may add or sub any amount of time
		now = now % (60*60*24)						#depending on your local time.
		now = time.strftime('%H:%M', time.localtime(now))
		file = client.upload_file(f"time_images_unix/{now}.jpg")
		client(UploadProfilePhotoRequest(file))
		time.sleep(2)
		p = client.get_profile_photos("me")[1]
		client(DeletePhotosRequest(id=[InputPhoto(id=p.id, access_hash=p.access_hash, file_reference=p.file_reference)]))
		now = time.time()
		now = now + (60*60*3) #+3 hours to my Virtual Machine time. You may add or sub any amount of time
		now = now % (60*60*24)						#depending on your local time.
		now = time.strftime('%H:%M', time.localtime(now))
