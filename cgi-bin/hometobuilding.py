#!C:\Python27\python.exe
import cgi
import sqlite3
import bs4
import shelve

def settingNLHroomcolor(room_id):
	str1="..\\htdocs\\ITT-P\\structure\\NLH_l.html"
	room_id="N"+str(room_id)
	#print room_id
	with open(str1) as inf:
		txt = inf.read()
		soup = bs4.BeautifulSoup(txt,"html.parser")
	
	soup.find("polygon",{"id":room_id})['style']="fill:rgb(255,0,0);"
	soup.find("polygon",{"id":room_id})['onclick']=""
	#<polygon onclick="toggleSelect(this)" id="N205" points="106.3 92.73 106.3 85.18 133.18 85.18 133.18 105.11 129.37 109.58 98.18 109.58 98.18 92.73 106.3 92.73"><title>205</title></polygon></svg>
	
	str1="..\\htdocs\\ITT-P\\structure\\NLH_ll.html"
	
	with open(str1, "w") as outf:
		outf.write(str(soup))

def cleanNLHroomcolor():
	str1="..\\htdocs\\ITT-P\\structure\\NLH_l.html"
	#print room_id
	with open(str1) as inf:
		txt = inf.read()
		soup = bs4.BeautifulSoup(txt,"html.parser")
	
	#soup.find("polygon",)['style']="fill:rgb(206,156,104);"
	#<polygon onclick="toggleSelect(this)" id="N205" points="106.3 92.73 106.3 85.18 133.18 85.18 133.18 105.11 129.37 109.58 98.18 109.58 98.18 92.73 106.3 92.73"><title>205</title></polygon></svg>
	
	str1="..\\htdocs\\ITT-P\\structure\\NLH_ll.html"
	
	with open(str1, "w") as outf:
		outf.write(str(soup))

		
"""
def settingAB5roomcolor(room_id):
	str1="..\\htdocs\\ITT-P\\structure\\AB5_l.html"
	with open(str1) as inf:
		txt = inf.read()
		soup = bs4.BeautifulSoup(txt,"html.parser")
	
	list1=soup.find("path")
	
	
	with open(str1, "w") as outf:
		outf.write(str(soup))
"""
				
s=shelve.open("temp");
form=cgi.FieldStorage()
con=sqlite3.connect("Room_Management.db")
building=str(form.getvalue('building'))		#set select in html to name=building
building="NLH"
date=str(form.getvalue('date'))
time=str(form.getvalue('time'))

s['date']=date
s['time']=time
s.close()
BuildingSelect=0;
if (building == "NLH"):
	BuildingSelect=1
	string= "select Room_ID from CheckStatus where Building_ID="+str(BuildingSelect)+" and Date='"+date+"' and Time='"+time+"';"
	#print string
	cleanNLHroomcolor()
	cursor=con.execute(string)
	for row in cursor:
		settingNLHroomcolor(row[0])
		#print row[0]
	
		
"""
elif (building =="AB-5"):
	BuildingSelect=2
	cursor=con.execute("select Room_ID from CheckStatus where Building_ID="+str(BuildingSelect)+";")
	for row in cursor:
		settingAB5roomcolor(row[1])
"""

con.close();
	
print "Content-type:text/html\r\n\r\n";
print "<html><head>"
redirectURL = "../ITT-P/structure/NLH_ll.html"
print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print "</head></html>"
