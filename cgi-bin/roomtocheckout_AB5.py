#!C:\Python27\python.exe
import cgi
import sqlite3
import bs4
def changeHtml(str1,name):
	global email
	with open(str1) as inf:
		txt = inf.read()
		soup = bs4.BeautifulSoup(txt,"html.parser")
	
	list=soup.find("",{"id":"login"})
	list.clear()
	list.insert(0,name)
	
	with open(str1, "w") as outf:
		outf.write(str(soup))
form=cgi.FieldStorage()
con=sqlite3.connect("Room_Management.db")
print "Content-type:text/html\r\n\r\n";
print "<html><head>"
redirectURL = "../ITT-P/user/checkout.html"
print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print "</head><body></body></html>"
con.close();