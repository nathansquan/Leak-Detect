#!/usr/bin/python3
from twilio.rest import Client
from config import account_sid, auth_token, twi_num, voice_num
from time import sleep

client = Client(account_sid, auth_token)

# iterate through voice_num list of recipient phone numbers
for i in voice_num:
    call = client.calls.create(
            from_ = twi_num,
            twiml = '<Response><Say>Turtle tank leak detected! Please check for water. Turtle tank leak detected! Please check for water.</Say></Response>',
            to = i
            )
    print(call.sid)
    sleep(10)
