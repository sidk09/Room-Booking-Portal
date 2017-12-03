#!C:\Python27\python.exe
import cgi
import sqlite3
form=cgi.FieldStorage()
emailId=str(form.getvalue("email"));
name=str(form.getvalue("name"));
password=str(form.getvalue("password"));
confirmPassword=str(form.getvalue("confirmPassword"));
con=sqlite3.connect("Room_Management.db")
print "Content-type:text/html\r\n\r\n";
print "<html><head>"
fl=0
cr1=con.execute("select Email from Student where Email = '"+ emailId +"'")
for runner in cr1:
	if (runner[0]==emailId):	
		fl=1
if password==confirmPassword and fl==0:
	cmd="insert into student values('"+password+"','"+name+"','"+emailId+"')"
	con.execute(cmd)
	fl=1
	con.commit()
	redirectURL = "../ITT-P/login.html"
	print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
elif password!=confirmPassword:
	redirectURL = "../ITT-P/login.html"
	print '<script type=text/javascript>alert("Password doesn\'t match")</script>'
	print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
else:
	redirectURL = "../ITT-P/login.html"
	print '<script type=text/javascript>\
	alert("Email ID already exists")\
	</script>'
	print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
con.close()
print "</head></html>"