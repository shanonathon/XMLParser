The mechanism for parsing the application.xml data is comprised of a python script that uses the BeautifulSoup library to grab data in specified tags and write it to a new file.  The automator workflow allows this to be run as a service so that you can right click on the file and choose "Convert Application" to convert and launch the html document in a browser.

Requirements:

Install the BeautifulSoup library:
*sudo pip install BeautifulSoup*

* Clone/Download the repository.
* Move the convert.py script to the location of your choice.
* Double-click the "JIRA XML Parser.workflow" and install as a service.
* After installation is complete, open the workflow in Automator. 
* Replace the path in the first workflow step with the path you chose to save convert.py
* Save the workflow.
* ???
* Profit.