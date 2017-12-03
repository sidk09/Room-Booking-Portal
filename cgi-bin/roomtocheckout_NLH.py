#!C:\Python27\python.exe
import cgi
import sqlite3
import bs4
import shelve
room_list=""

def findSelectedRoom(str1,str2):
	global room_list
	global date
	global time
	global email
	
	with open(str2) as inf:
		txt = inf.read()
		soup = bs4.BeautifulSoup(txt,"html.parser")
	
	soup.find("input",{"id":"building_id"})['value']=1
	soup.find("input",{"id":"room_id"})['value']=room_list
	soup.find("input",{"id":"date"})['value']=date
	soup.find("input",{"id":"time"})['value']=time
	soup.find("input",{"id":"email"})['value']=email
	
	with open(str2, "w") as outf:
		outf.write(str(soup))
		
		
form=cgi.FieldStorage()
if str(form.getvalue('N101'))=="1":
	room_list=room_list+"101"+","
	print room_list
if str(form.getvalue('N102'))=="1":
	room_list=room_list+"102"
	print room_list

con=sqlite3.connect("Room_Management.db")
s=shelve.open("temp")
email=s['email']
date=s['date']
time=s['time']
s.close()
findSelectedRoom("..\\htdocs\\ITT-P\\structure\\NLH_ll.html","..\\htdocs\\ITT-P\\user_checkout\\checkout.html")
print "Content-type:text/html\r\n\r\n";
print "<html><head>"
redirectURL = "../ITT-P/user_checkout/checkout.html"
print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print "</head><body></body></html>"
con.close();