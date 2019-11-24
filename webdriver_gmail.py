#!/usr/bin/python
import base64
import getpass
import time

from selenium import webdriver

username = input("Username: ")
password = getpass.getpass()

browser = webdriver.Firefox()
browser.get("http://google.com/gmail")
browser.maximize_window()

email = browser.find_element_by_id("identifierId")
email.send_keys(username)

nextButton = browser.find_element_by_id("identifierNext")
nextButton.click()

time.sleep(3)

passwd = browser.find_element_by_xpath("//*[@name='password']")
coded = base64.b64encode(password.encode())
cypher = base64.b64decode(coded)
passwd.send_keys(cypher.decode())

nextButtonPass = browser.find_element_by_id("passwordNext")
nextButtonPass.click()
