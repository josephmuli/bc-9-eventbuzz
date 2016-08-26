#!/usr/bin/env python
"""
This program uses docopt with the built in cmd module to demonstrate an
interactive ticket generating command application.
Usage:
    tickets create <name> <start_date> <end_date> <venue>
    tickets delete <event_id>
    tickets edit <event_id> <new_event_details>
    tickets list
    tickets view <event_id>
    tickets generate <email>
    tickets invalidate <t_id>
    tickets (-i | --interactive)
    tickets (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from operations import EventsCrud
from ticket_crud import TicketsCrud
import requests


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = '(event_buzz) '
    file = None
    global event_id

    @docopt_cmd
    def do_create(self, arg):
        """Usage: create <name> <start_date> <end_date> <venue>"""

        event  =  EventsCrud()
        # event_id = arg['<event_id>']
    
        print(event.create_event(arg))


    @docopt_cmd
    def do_list(self, arg):
        """Usage: list """

        event  =  EventsCrud()
        event.list_events()
    
        print(event.list_events())


    @docopt_cmd
    def do_delete(self, event_id):
        """Usage: delete <event_id> """

        event  =  EventsCrud()
        event.delete_event(event_id)

    @docopt_cmd
    def do_invalidate(arg):
        """Usage: invalidate <t_id> """

        ticko = Ticket()
        ticko.ticket_invalidate(arg['<t_id>'])

        return 'Ticket is now invalid!'


    @docopt_cmd
    def do_generate(self, arg):
        """Usage: generate <email> """

        ticket_type = raw_input("Enter A for VVIP, B for VIP and C for regular: ")
        if ticket_type == 'A':
            ticket_type = 'VVIP'
        elif ticket_type == 'B':
            ticket_type = 'VIP'
        elif ticket_type == 'C':
            ticket_type = 'Regular'

        event_name = raw_input("Enter the Event you're signing up for: ")
        
        ticket = TicketsCrud()
        ticko = ticket.create_ticket(ticket_type, event_name)
        ticket_id = ticko.id

        print('Your ticket is being processed, please check your email')
        return requests.post(
            "https://api.mailgun.net/v3/samples.mailgun.org/messages",
            auth=("api", "key-6649005511b2ba6f97d95f7120732e0d"),
            data={"from": "Excited User <excited@samples.mailgun.org>",
                    "to": ["email"],
                    "subject": "EventBuzz Ticket Information",
                    "text": "Hey There! here's your ticket info:  Ticket id:%s and Event registered: %s " %(ticket_id, event_name)})


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Cheers!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)