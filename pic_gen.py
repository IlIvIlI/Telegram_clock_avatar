from utils import *
import cv2
import numpy as np
from datetime import datetime, timedelta

def get_black_background():
	return np.zeros((200, 200)) #image size (200px*200px)
	
start_time = datetime.strptime("2020-02-21", "%Y-%m-%d")  # Any date may be applied
end_time = start_time + timedelta(days=1)

def generate_image_with_text(text):
	image = get_black_background()
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(image, text, (int(image.shape[0]*0.15), int(image.shape[1]*0.55)), font, 1.5, (255, 255, 0), 2, cv2.LINE_AA)
	return image

while start_time < end_time:
	text = convert_time_to_string(start_time)
	image = generate_image_with_text(text)
	cv2.imwrite("time_images_unix/{}.jpg".format(text), image)
	start_time += timedelta(minutes=1)
