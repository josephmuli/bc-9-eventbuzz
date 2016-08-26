## Event Buzz  :ticket: :ticket:

### Introduction  

**Event Buzz** is a console application that facilitates a ticket booking service  
**Event Buzz** allows a user to do the following:  
 * Create a new event with a name, start date, end date and venue  
 * Generate tickets for events and send an email update
 * Invalidate a ticket 
 * View an event's tickets  
 * Delete an event  
 * Edit a specific event's details  
 * List out all events  
 * Send email updates on an event's schedule  


### Dependencies  
#### Backend Dependencies:
1. [Docopt](http://docopt.org/) - This is a Pythonic package that allows creating the command-line interface for eventbuzz.  
2. [SQlite](https://www.sqlite.org/) - This is a light-weight relational database that eventbuzz uses to store event data.  
3. [SQL Alchemy](http://www.sqlalchemy.org/) - This is a python SQL toolkit and Object relational mapper.  
4. [smtplib](https://docs.python.org/2/library/smtplib.html) - This is a python library that handles sending of emails via python modules.  
5. [python-crontab](https://pypi.python.org/pypi/python-crontab/) - This is a python library that enables scheduling of various tasks.  
6. [mailgun](https://mailgun.com/) - Mailgun offers an API for sending emails. 

### Installation and setup:  

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
* Run the app  
	* ` python filename.py function_name argument(s) `  

### Tests  
* Tests have been written using the python [unittest](https://docs.python.org/2/library/unittest.html) framework.  
* To run the tests, navigate to the project's root folder,  
* issue the following command on terminal.  
	* ` python buzz_tests.py `  
* If the tests are successful, they will not display any error or failure.  

## To-Do:  

* Cron jobs to be assigned email addresses  
* User profiles for user identification  