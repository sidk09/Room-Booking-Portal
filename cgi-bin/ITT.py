import smtplib
import getpass
import cgi
form=cgi.FieldStorage()

smtpgmail='smtp.gmail.com'
port_values=[587,465]

try:
    smtpObj=smtplib.SMTP(smtpgmail,port_values[0]
except:
    smtpObj=smtplib.SMTP_SSL(smtpgmail,port_values[1])

smtpObj.ehlo()
smtpObj.starttls()

                         
Usr="temporarymailforittlab";passwrd="ittlabfortemporarymail"                         
Subject="Subject: User Response "+str(form.getvalue('subject_h'))
Text=form.getvalue('message_h')
Mail=Subject+""+Text
Recipient=form.getvalue('email_h')

smtpObj.sendmail(Usr,Recepient,Mail)
smtpObj.close()                         
