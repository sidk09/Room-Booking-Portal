#!C:\Python27\python.exe
import cgi,cgitb
print "Content-type: text/html\r\n\r\n"

import sha, time, Cookie, os
cookie = Cookie.SimpleCookie()
existent = os.environ.get('HTTP_COOKIE')
print '<html><head></head><body>'
# If new session
if not existent:
	print "<h1>kuch bhi</h1>"
    #The sid will be a hash of the server time
	sid = sha.new(repr(time.time())).hexdigest()
    # Set the sid in the cookie
	cookie['sid'] = sid
    # Will expire in a year
	cookie['sid']['expires'] = 12 * 30 * 24 * 60 * 60
    # print new cookie header
	print cookie
    
	print "<h1>kuch bhi</h1>"
    
	print '<p>New session</p>'    
	print '<p>SID =', cookie['sid'], '</p>'
else:
    # If already existent session  
	cookie.load(existent)
	sid = cookie['sid'].value
	#print str(cookie)
	print "<h1>kuch bhi</h1>"
	print '<p>Already existent session</p>'
	
print '</body></html>'