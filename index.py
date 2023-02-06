import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]

message= OTP + " is your OTP"
# bxfxzjnosseuyaei
gmailid=input("Enter Gmail ID")
# print(message)
s= smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('gungungupta1404@gmail.com','ovpujdslpbmxaubz')
s.sendmail(gmailid,gmailid,message)
s.quit()

a=input("enter your OTP>>: ")
if a==OTP:
    print("verified")
else:
    print("Please check the  OTP Again")