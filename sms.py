#!/usr/bin/python3

# import address, password, and sms_num variables from config file
from config import address, password, sms_num
import smtplib

mail = smtplib.SMTP( "smtp.gmail.com", 587 )
mail.ehlo()
mail.starttls()

content = "Turtle tank water leak detected!"

mail.login(address, password)
mail.sendmail(address, sms_num, content)
mail.close()
