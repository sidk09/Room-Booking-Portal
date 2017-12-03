#!C:\Python27\python.exe
import cgi
import sqlite3
import bs4


form=cgi.FieldStorage()
building_id=str(form.getvalue('building_id'));
#building_id="111"
room_ids=str(form.getvalue('room_id'))
#room_ids="101,102"
room_list=room_ids.split(",");
##room_id="111"
##capacity=str(form.getvalue('capacity'))
##capacity_list=room_ids.split(",");
##capacity="50"
date=str(form.getvalue('date'))
#date="2017"
time=str(form.getvalue('time'))
#time="0615"
approve1="pending"
approve2="pending"
approve3="pending"
reason=str(form.getvalue('reason'))
#reason="maa randi"
email=str(form.getvalue('email'))
#email="sxsssdsdsd"
application_id= email+str(date)+str(time)
con=sqlite3.connect("Room_Management.db")

#print "insert into Application values('"+application_id+"',"+building_id+","+room_id+","+capacity+","+date+","+time+",'"+approve1+"','"+approve2+"','"+approve3+"','"+reason+"','"+email+"');"
for room_no in room_list:
	con.execute("insert into Application values('"+application_id+"',"+building_id+","+room_no+",'"+date+"','"+time+"','"+approve1+"','"+approve2+"','"+approve3+"','"+reason+"','"+email+"');")
con.commit();
con.close();
string1="Request has been forwarded and your application id is: "+ application_id
print "Content-type:text/html\r\n\r\n"		
print "<html><head>"


print '<script>'
print 'alert("'+string1+'")'
print '</script>'

redirectURL = "../ITT-P/home_l.html"
print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print "</head></html>"
