import datetime as dt
import random
import smtplib
now  = dt.datetime.now()
weekday = now.weekday()
monday_time = dt.datetime(year=2022,month=9,day=12,hour=0,minute=37)
#OPENING THE FIRST FILE THAT CONATAINS ALL THE QUOTES
with open("quotes.csv") as data:
  #READLINES MODULE IS USED TO CONVERT THE CONTENT TO A LIST
    data1 = data.readlines()
quotes_of_the_day = random.choice(data1)
with open("email.csv") as email_server:
    email_server1 = email_server.readlines()
    print(email_server1)
my_email = #YOUR_EMAIL_HERE
password = #PASSWORD GENERTATED FROM UR ISP 
receiver_email = "dumpstesting0@gmail.com"
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    #I AM ASKING THE CODE TO CHECK IF IT IS AT 23HOUR SO SEND THE QUOTE
    if now.hour == 23 and now.hour==0:
        for email in email_server1:
            connection.sendmail(from_addr=my_email,
                        to_addrs=email,
                        msg=f"Subject:Motivational_quote\n\n{quotes_of_the_day}")



