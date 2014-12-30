#Step 3: run in terminal
#using full image links, download and save
import urllib2
import os

def download_image(l, i):
	url = urllib2.build_opener()
	url.addheaders = [('User-agent', 'Mozilla/5.0')]
	
	directory = 'images'
	#check if directory exists, otherwise create it
	if not os.path.exists(directory):
		os.makedirs(directory)

	filepath = directory + '/img_'+ str(i)
	print filepath
	print l
	try:
		resp = url.open(l)
		im = resp.read()
		with open(filepath, 'w') as f:
			f.write(im)
	except Exception, e:
		print "ERROR " + str(e.args) + ": Image " + str(i) 

count = 0
current = ""
with open('step2_Imagelinks.txt') as f:
	while True:
		c = f.read(1)
		if not c:
			print "End of step2_Imagelinks"
			break;
		if c == ',':
			download_image(current, count)
			current = ""
			count = count + 1
		else:
			current = current + c
