
from twilio.rest import Client

account_sid = 'AC4f4be6c0e47a8d041615b22bff30044e'
auth_token = '1532cdc2a9cb656aebac65f3275dbc6d'

client = Client(account_sid, auth_token)

call = client.calls.create(
        from_ = '+12702761943',
        twiml = '<Response><Say>Turtle tank leak detected! Turtle tank leak detected!Say></Response>',
        to = '+17038960064'
        )

print(call.sid)
