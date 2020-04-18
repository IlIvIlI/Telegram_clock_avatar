The main idea how it works:
1. You generate 1440 photos with specific text(time) on it.
2. Every minute, this script will check time and if it has changed -- new profile photo will be uploaded within current time. If the time
did not change -- script will not upload new photo.

SET UP:
1. Make sure you have Python 3 installed (not sure if it works on Python 2, have not checked)
2. Run pic_gen.py file, it will create (if not, create this folder manually) new directory /time_images_unix (in pic_gen.py you may set any
other name for your directory). In a few seconds this script will generate 1440 photos (.jpg) in the directory you have provided.
3. In config.py you have to paste your own api_id and api_hash values. Visit https://core.telegram.org/api/obtaining_api_id to obtain them.
Once you obtained api_id and api_hash, paste them instead of ur_id and 'ur_hash'. FOR NEWBIES: Its important to paste api_id without
apostrophies('), because its int variable, and api_hash between two apostrophies, because its string variable.
4. In actual_time.py set correct time for your region (currently it is UTC+3:00) and set name for your session (this is optional, but
by default, name will be set 'Moscow_time').
5. Run actual_time.py file. Follow simple instructions from console (input your mobile phone, which is connected to your telegram account. 
The security code will be sent to you from Telegram. Input recieved code). Have fun!
