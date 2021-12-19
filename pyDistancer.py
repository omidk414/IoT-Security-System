#! /bin/env python

import serial   # Needed for serial Communication
import time     # Needed for sleep function
import smtplib  # Needed for emailing
#import imaplib  # Needed for emailing (receiving)

## USER INFO SECTION ##
usr = "omidk414@gmail.com"         # Your Username
psw = "password"                   # Your Password
rcp = "omid414@yahoo.com"          # The recipient
msg = "Someone just knocked!"      # The Message to Send
com = "COM4"                       # The Com your Arduino Is on
## END OF SECTION ##

msg_sent = 0

ser = serial.Serial(com, 9600, timeout=1)
while 1:
    try:
        # Read the Distance from Serial as an int
        knock = int(ser.readline());
        print(knock)
        if(knock < 80) and msg_sent is 0:
            print ("knock read")
            server = smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login(usr, psw)
            server.sendmail(usr, rcp, msg)
            server.close()
            print("MSG SENT!")
            time.sleep(1)
        msg_sent = (msg_sent + 1) % 1 # Used to limit number of messages sent at once

    except :#ser.SerialTimeoutException:
        print('Data could not be read')
        time.sleep(1)
