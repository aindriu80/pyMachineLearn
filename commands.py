import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "year", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is pie python commander. How are you?")
        if "launch" or "open" in text:
            app = text.split(" ", 1)[-1]
            os.system("open -a" + app + ".app")

    def respond(self, response):
        print(response)
        subprocess.call("say "+ response, shell=True)
