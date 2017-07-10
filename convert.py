from bs4 import BeautifulSoup
import sys, re

soup = BeautifulSoup(open(sys.argv[1], 'r'), 'xml')

doc = open('/Users/sseaver/Desktop/application-extract.html','w')

tags = []

max_heap_str = soup.find('max-heap').text.strip()
heap_convert = re.sub("[^\d\.]", "",max_heap_str)
heap_int = int(heap_convert)
heap_second = (heap_int / 1000000)
heap_final = str(heap_second)

doc.write('<link href="/Users/sseaver/Documents/Dev/Converter/assets/bootstrap.min.css" rel="stylesheet"> ')
doc.write('<link href="/Users/sseaver/Documents/Dev/Converter/assets/converter.css" rel="stylesheet"> ')

for tag in soup.find_all('java-runtime-environment'):
	doc.write('<body>')
	doc.write('<div class="container">')
	doc.write('<div class="col-md-3">')
	doc.write('<h3>JAVA CONFIGURATION</h3>')
	doc.write('<b>JAVA HOME: </b>')
	doc.write(tag.find('java.home').text)
	doc.write('<br>')
	doc.write("<b>JAVA VERSION: </b>")
	doc.write(tag.find('java.runtime.version').text)
	doc.write('<br>')
	doc.write('<b>HEAP USED: </b>')
	doc.write(tag.find('percent-heap-used').text)
	doc.write('<br>')
	doc.write('<b>MAX HEAP: </b>')
	doc.write(heap_final)
	doc.write('MB')
	doc.write('<br>')
	doc.write('</div>')
	

for tag in soup.find_all('operating-system'):
	doc.write('<div class="col-md-3">')
	doc.write('<h3>OS CONFIGURATION</h3>')	
	doc.write('<b>SYSTEM CPU LOAD: </b>')
	doc.write(tag.find('system-cpu-load').text)
	doc.write('<br>')
	doc.write('<b>PROCESS CPU LOAD: </b>')
	doc.write(tag.find('process-cpu-load').text)
	doc.write('<br>')
	

for tag in soup.find_all('system-information'):

	doc.write('<b>OS TYPE: </b>')
	doc.write(tag.find('Operating-System').text)
	doc.write('<br>')	
	doc.write('<b>DATABASE TYPE: </b>')
	doc.write(tag.find('Database-type').text)
	doc.write('<br>')
	doc.write('<b>DATABASE VERSION: </b>')
	doc.write(tag.find('Database-version').text)
	doc.write('<br>')
	doc.write('</div>')


for tag in soup.find_all('database-statistics'):
	doc.write('<div class="col-md-3">')
	doc.write('<h3>INSTANCE STATS</h3>')
	doc.write('<b>ATTACHMENTS: </b>')
	doc.write(tag.find('Attachments').text)
	doc.write('<br>')
	doc.write('<b>COMMENTS: </b>')
	doc.write(tag.find('Comments').text)
	doc.write('<br>')
	doc.write('<b>CUSTOM FIELDS: </b>')
	doc.write(tag.find('Custom-Fields').text)
	doc.write('<br>')
	doc.write('<b>ISSUES: </b>')
	doc.write(tag.find('Issues').text)
	doc.write('<br>')
	doc.write('<b>PROJECTS: </b>')
	doc.write(tag.find('Projects').text)	
	doc.write('<br>')
	doc.write('<b>SCREENS: </b>')
	doc.write(tag.find('Screens').text)
	doc.write('<br>')
	doc.write('<b>USERS: </b>')
	doc.write(tag.find('Users').text)
	doc.write('<br>')
	doc.write('<b>WORKFLOWS: </b>')
	doc.write(tag.find('Workflows').text)
	doc.write('</div>')

baseurl = soup.find('jira.baseurl').text
doc.write('<div class="col-md-3">')
doc.write('<h3>JIRA CONFIGURATION</h3>')
doc.write('<b>JIRA HOME: </b>')
for tag in soup.find_all('path-information'):
    doc.write(tag.find('location-of-jira-home').text)
doc.write('<br>')
doc.write('<b>BASE URL: </b>')
doc.write(baseurl)
doc.write('</div>')
doc.write('</div>')
doc.write('</body>')






