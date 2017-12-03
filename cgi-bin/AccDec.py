#!C:\Python27\python.exe
import cgi
import sqlite3
import bs4
import shelve
import smtplib


smtpgmail='smtp.gmail.com'
port_values=[587,465]

try:
    smtpObj=smtplib.SMTP(smtpgmail,port_values[0])
except:
    smtpObj=smtplib.SMTP_SSL(smtpgmail,port_values[1])

smtpObj.ehlo()
smtpObj.starttls()



def mail(status,app):	                         
	Usr="temporarymailforittlab@gmail.com";passwrd="ittlabfortemporarymail"                         
	smtpObj.login(Usr,passwrd)
	Subject="Subject: "+ app +" "+" status"
	Text="\n"+status
	Mail=Subject+""+Text
	
	query1= "select * from Application where Application_ID='"+app+"';"
	cursor=con.execute(query1)
	for row in cursor:
		Recepient=row[9]		
	smtpObj.sendmail(Usr,Recepient,Mail)
	smtpObj.close()      	
		

print "Content-type:text/html\r\n\r\n";
print "<html><head>"

form=cgi.FieldStorage()
res=str(form.getvalue("ans"));
app=str(form.getvalue("application"));
con=sqlite3.connect("Room_Management.db")
if res=="Accept":
	query1= "select * from Application where Application_ID='"+app+"';"
	cursor=con.execute(query1)
	building_id=[]
	room_id=[]
	date=[]
	time=[]

	for row in cursor:
		building_id.append(str(row[1]))
		room_id.append(str(row[2]))
		date.append(str(row[3]))
		time.append(str(row[4]))
		
	query2 = "update Application set approve1='"+"accepted"+"' where Application_ID='"+app+"';"
	con.execute(query2)
	con.commit()
	for i in range(0,len(date)):
		query3 = "insert into CheckStatus values("+building_id[i]+","+room_id[i]+",'"+date[i]+"','"+time[i]+"',1);"
		con.execute(query3)
	con.commit()	
	mail("Your request has been accepted",app);
	redirectURL = "../ITT-P/home_dl.html"
	print '<script type=text/javascript>\
	alert("Done Accepting")\
	</script>'
	print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
else:
	query2 = "update Application set approve1='"+"decline"+"' where Application_ID='"+app+"';"
	con.execute(query2)
	con.commit()
	mail("Your request has been declined",app);
	redirectURL = "../ITT-P/home_dl.html"
	print '<script type=text/javascript>\
	alert("Done Declining")\
	</script>'
	print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print "</head></html>"