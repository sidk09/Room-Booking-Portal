#!C:\Python27\python.exe
import cgi
import sqlite3
import bs4
import shelve



			
def changeHtml(str1,name):
	global email
	with open(str1) as inf:
		txt = inf.read()
		soup = bs4.BeautifulSoup(txt,"html.parser")
	
		# create new link
	list=soup.find("a",{"id":"login"})
	#new_link = soup.new_tag("a" , href="icon", id="login")
	# replace it into the document
	#list.replaceWith(new_link)
	# save the file again
	list.clear()
	list.insert(0,name)
	
	#list1=soup.find("p",{"id":"data"})
	#list1.clear()
	
	#list1.insert(0,email)
	
	with open(str1, "w") as outf:
		outf.write(str(soup))

def userdetailfillup(str1,str2,str3):
	with open(str1) as inf:
		txt = inf.read()
		soup = bs4.BeautifulSoup(txt,"html.parser")
	list=soup.find("input",{"id":"name1"})
	new_link = soup.new_tag("input" , type="text", id="name1", placeholder=str2 )
	list.replaceWith(new_link)
	list=soup.find("input",{"id":"email1"})
	new_link = soup.new_tag("input" , type="text", id="email1", placeholder=str3 )
	list.replaceWith(new_link)
	with open(str1, "w") as outf:
		outf.write(str(soup))







def directorHtml():
		#changeHtml("..\\htdocs\\ITT-P\\home_dl.html","Director")
		changeHtml("..\\htdocs\\ITT-P\\about_d.html","Director")
		changeHtml("..\\htdocs\\ITT-P\\contact_d.html","Director")	
		changeHtml("..\\htdocs\\ITT-P\\director\\P1.html","Director")
		#userdetailfillup("..\\htdocs\\ITT-P\\director\\P1.html","Director","director@mail.com")
		global con
		query='select * from Application where approve1="pending"'
		cursor=con.execute(query);
		with open("..\\htdocs\\ITT-P\\home_d.html") as inf:
			txt = inf.read()
			soup = bs4.BeautifulSoup(txt,"html.parser")
			
		string="..\\htdocs\\ITT-P\\home_dl.html"
	
		with open(string, "w") as outf:
			outf.write(str(soup))
		
		with open("..\\htdocs\\ITT-P\\home_d.html") as inf:
			txt = inf.read()
			soup = bs4.BeautifulSoup(txt,"html.parser")
			
		for row in cursor:
			new_option = soup.new_tag("option",value=row[0])
			new_option.clear()
			new_option.insert(0,row[0])
			list1=soup.find("select",{"id":"build"})	
			list1.append(new_option)
			
		with open(string, "w") as outf:
			outf.write(str(soup))
				
				
				
				
				
				
	
form=cgi.FieldStorage()
email=str(form.getvalue("email"));

password=str(form.getvalue("password"));

s=shelve.open("temp")
s['email']=email
s.close()

con=sqlite3.connect("Room_Management.db")
cursor=con.execute("select Password from Student where Email='"+email+"'")
print "Content-type:text/html\r\n\r\n";
print "<html><head>"
notPresent=True;
Name=""
for row in cursor:
	notPresent=False;
	if password==row[0]:
		if email=="director@mail.com":
			directorHtml()
			redirectURL = "../ITT-P/home_dl.html"
			print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
		else:		
			cur=con.execute("select Name from Student where Email='"+email+"'")
			for r in cur:
				Name=str(r[0])	
			changeHtml("..\\htdocs\\ITT-P\\home_l.html",Name)
			changeHtml("..\\htdocs\\ITT-P\\about_l.html",Name)
			changeHtml("..\\htdocs\\ITT-P\\contact_l.html",Name)	
			changeHtml("..\\htdocs\\ITT-P\\structure\\NLH_ll.html",Name)
			changeHtml("..\\htdocs\\ITT-P\\structure\\AB5_ll.html",Name)
			changeHtml("..\\htdocs\\ITT-P\\user\\P1.html",Name)
			changeHtml("..\\htdocs\\ITT-P\\user_checkout\\checkout.html",Name)
			userdetailfillup("..\\htdocs\\ITT-P\\user\\P1.html",Name,email)
			con.close();
			redirectURL = "../ITT-P/home_l.html"
			print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
	else:
		con.close();
		redirectURL = "../ITT-P/login.html"
		print '<script type=text/javascript>\
		alert("Incorrect pasword")\
		</script>'
		print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
		
if notPresent:
	con.close();
	redirectURL = "../ITT-P/login.html"
	print '<script type=text/javascript>\
	alert("User doesn\'t exist")\
	</script>'
	print '<meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
print "</head></html>"
