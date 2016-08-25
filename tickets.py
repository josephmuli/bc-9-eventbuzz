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
    tickets invalidate <ticket_id>
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


    @docopt_cmd
    def do_create(self, arg):
        """Usage: create <name> <start_date> <end_date> <venue>"""

        event  =  EventsCrud(arg['<name>'], arg['<start_date>'], arg['<end_date>'], arg['<venue>'])
    
        print(event.create_event())


    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Cheers!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)