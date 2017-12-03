#!C:\Python27\python.exe
import bs4

# load the file
with open("..\\htdocs\\bs4test.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt,"html.parser")

# create new link
list=soup.find("p",{"id":"w"})

#new_link = soup.new_tag("p" ,id="w")
# insert it into the document
list.clear()
list.insert(0,"kuch bhi")

# save the file again
with open("..\\htdocs\\bs4test.html", "w") as outf:
    outf.write(str(soup))