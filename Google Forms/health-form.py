# -*- coding: utf-8 -*-

###
# usage:
# health-form.py "kid name in English", "kid name in Hebrew", "grade in Number", "Parent name in Hebrew"
# E.g. health-form.py "Adi", "עדי בנר", "4", "טל"
###

import requests
import logging
import datetime
import sys
import math

is_test = False

class kid:
    log_name: str
    name: str
    house: str

houses = ["כחל (א'-ב')", "דרור (ג'-ד')", "שחף (ה'-ו')"]

def init():
    logging.basicConfig(filename="log.log", level=logging.INFO, format='%(asctime)s: %(message)s', datefmt='%d/%m/%Y %H:%M')

def log(kid: kid, response):
    logging.info("%s - %s (%s)", kid.log_name, response, response.reason)
    print(kid.log_name, response, response.reason)
    if response.status_code != 200:
        print("***** ERROR")
        open("ERROR ON %s.err" % datetime.datetime.now().strftime("%d-%m"),"w+")
    


def submit(kid: kid, parent: str):
    url = "https://docs.google.com/forms/d/e/1FAIpQLSe9pbfJ59iyZgGNvSxSTIRk3YWgELf2_4n0R1H-B9Hh15xDWw/formResponse"

    form_data = {
        'entry.634058393': kid.name,
        'entry.254435542': parent,
        'entry.1738413463': kid.house,
        'entry.1848196357': 'נכון',
        'draftResponse': [],
        'fvv': 1,
        'pageHistory': 0,
        'fbzx': 2170144735828914929
    }

    response = requests.post(url, data=form_data)
    log(kid, response)


def main():
    init()

    k = kid()
    k.log_name = sys.argv[1]
    k.name = sys.argv[2]
    grade = int(sys.argv[3])
    k.house = houses[math.floor((grade-1)/2)]
    parent = sys.argv[4]

    submit(k, parent)
    

if __name__ == "__main__":
    main()