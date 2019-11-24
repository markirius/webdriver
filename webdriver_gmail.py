#!/usr/bin/python
import base64
import getpass
import time

from selenium import webdriver

username = input("Username: ")
password = getpass.getpass()

"""
set firefox as webbrowser and set gmail's as page
"""
browser = webdriver.Firefox()
browser.get("http://google.com/gmail")
browser.maximize_window()

"""
find on html the element with 'id' with name 'identifierId'
who is username form field
"""
email = browser.find_element_by_id("identifierId")
email.send_keys(username)

"""
find on html the elemento who matchs with the next button
"""
nextButton = browser.find_element_by_id("identifierNext")
nextButton.click()

"""
sip of coffee
"""
time.sleep(3)

"""
find on html an element with name equals password
"""
passwd = browser.find_element_by_xpath("//*[@name='password']")
coded = base64.b64encode(password.encode())
cypher = base64.b64decode(coded)
passwd.send_keys(cypher.decode())

"""
find on html element with id 'passwordNext' who matchs with
next button on password form
"""
nextButtonPass = browser.find_element_by_id("passwordNext")
nextButtonPass.click()

