#!/usr/bin/python3
from twilio.rest import Client
from config import account_sid, auth_token, twi_num, voice_num

client = Client(account_sid, auth_token)

call = client.calls.create(
        from_ = twi_num,
        twiml = '<Response><Say>Turtle tank leak detected! Turtle tank leak detected!Say></Response>',
        to = voice_num
        )

print(call.sid)
