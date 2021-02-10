#!/usr/bin/python3

# import address and password variables from config file
from config import address, password
import smtplib

mail = smtplib.SMTP( "smtp.gmail.com", 587 )
mail.ehlo()
mail.starttls()

content = "Turtle tank water leak detected!"
recipient = ['7038960064@vtext.com', '7038350187@vtext.com', '7038352749@vtext.com', '7032688643@vtext.com']

mail.login(address, password)
mail.sendmail(address, recipient, content)
mail.close()
