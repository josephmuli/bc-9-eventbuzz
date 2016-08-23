## Event Buzz  

### Introduction  

**Event Buzz** is a console application that facilitates a ticket booking service  
Event Buzz allows a user to do the following:  
1. Create a new event with a name, start date, end date and venue  
2. Generate tickets for events and send an email update
3. Invalidate a ticket 
4. View an event's tickets  
5. Delete an event  
6. Edit a specific event's details  
7. List out all events  
8. Send email updates on an event's schedule  


## Dependencies  
#### Backend Dependencies:
1. [Docopt](http://docopt.org/) - This is a Pythonic package that allows creating the command-line interface for eventbuzz.  
2. [Firebase](https://www.firebase.com) - This is the nosql database that eventbuzz uses to store event data.  
3. [python-firebase 1.2](https://pypi.python.org/pypi/python-firebase/1.2) - This is a pythonic package that handles request data from Firebase.  
4. [smtplib](https://docs.python.org/2/library/smtplib.html) - This is a python library that handles sending of emails via python modules.  
5. [python-crontab](https://pypi.python.org/pypi/python-crontab/) - This is a python library that enables scheduling of various tasks.  

## Installation and setup:  

* Navigate to a directory of choice on terminal.  

* Clone this repository from Github on that directory.  

	* Using SSH;
 		> ` git@github.com:josephmuli/bc-9-eventbuzz.git `  

	* Using HTTP;
		>  ` https://github.com/josephmuli/bc-9-eventbuzz.git `  


* Navigate to the repo's folder on your computer  
	* ``` cd bc-9-eventbuzz ```  

* Install the app's dependencies. I advice using a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)  
	* ``` pip install -r requirements.txt ```