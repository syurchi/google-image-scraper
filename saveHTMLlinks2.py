#Step 2: run in terminal
#using detailed image links from google image search, find and save full image link.
import urllib2
import re

def find_html_link2(l):
	if re.match(urlpattern, l):
		urlData = url.open(l)
		data = urlData.read()

		match = re.search(urlpattern, data)
		strLinkList.append(urllib2.unquote(match.group()))
	

def save_html_to_text(list):
	str = ','.join(list)

	# save html to temp file
	with open('step2_Imagelinks.txt', 'a') as f:
		f.write(str)
	print "Data successfully saved."
	return


url = urllib2.build_opener()
url.addheaders = [('User-agent', 'Mozilla/5.0')]
urlpattern = "(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?"

strLinkList = []

current = ""
with open('step1_Imagelinks') as f:
	while True:
		c = f.read(1)
		if not c:
			print "End of step1_Imagelinks"
			break;
		if c == ',':
			find_html_link2(current)
			current = ""
		else:
			current = current + c

	#save list of links to file
	save_html_to_text(strLinkList)
