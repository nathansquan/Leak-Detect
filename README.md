# Leak-Detect
Leak detection project for Raspberry Pi using Python 3. This project was used to monitor leaks from an aquarium tank external canister filter. When a leak is detected using a water level sensor, the RPi will send an SMS text to provided phone numbers using the smtplib library. A Twilio phone number was also created to send outgoing calls to provided phone numbers using the twilio library.

## sms.py

Requires the smtplib library:

```
pip install smtplib
```

## voice.py

Requires the twilio library:

```
pip install twilio
```
