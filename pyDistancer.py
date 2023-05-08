#! /bin/env python

import serial   # Needed for serial Communication
import time     # Needed for sleep function
import smtplib  # Needed for emailing
from twilio.rest import Client # Needed for SMS messaging

## CHANGE USER INFO SECTION ##
usr = "EMAIL@gmail.com"            # Your Email
psw = "password"                   # Your Password
rcp = "EMAIL@yahoo.com"            # The recipient
msg = "Someone just knocked!"      # The Message to Send
com = "COM4"                       # The Com your Arduino Is on

account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
twilio_number = '+1234567890'
recipient_number = '+1234567890'
## END OF USER INFO SECTION ##

msg_sent = False

ser = serial.Serial(com, 9600, timeout=1)
while True:
    try:
        # Read the Distance from Serial as an int
        knock = int(ser.readline())
        print(knock)
        
        if knock < 80 and not msg_sent:
            print("Knock detected!")
            
            # Send email
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(usr, psw)
            server.sendmail(usr, rcp, msg)
            server.close()
            print("Email sent!")
            
            # Send SMS message using Twilio
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=msg,
                from_=twilio_number,
                to=recipient_number
            )
            print("SMS sent!")
            
            # Set message sent flag
            msg_sent = True
            time.sleep(1)
        
        elif knock >= 80:
            msg_sent = False

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
