# -*- coding: utf-8 -*-
"""
Created on Sat May  8 10:44:46 2021

@author: Sambodhi
"""

import smtplib         #Simple mail transfer protocol
from email.message import EmailMessage
import speech_recognition as sr    #used to convert voice to text
import pyttsx3                     #used to convert text to voice
listener = sr.Recognizer()          #listens and recognize the text
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
server = smtplib.SMTP('smtp.gmail.com', 587)  #create the serverto send mail
server.starttls()
server_login_mail = 'username@gmail.com'
server_login_password = 'userpassword'
server.login(server_login_mail, server_login_password)

def say(text):       #this function readd the text and convert it to voice
    engine.say(text)     
    engine.runAndWait()
    
say("Hello, Myself Email Assistant. How can I help you?")



def assistant_listener():    #this function is used to recognize voice using microphone
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.record(source, duration=6)
            try:
                info = listener.recognize_google(voice,language="en-in").lower()
                print(info)
                print('finished')
                return info
            except:
                print('could not recognize')
                return 0
    except:
        print('error')
        return 0
def send_email(rec,subject,message): #Accept the receiver name subject and text to be sent
    email = EmailMessage()
    email['From'] = server_login_mail
    email['To'] = rec
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    
contact = {
        "friend1" : "friend1@gmail.com",
        "friend2" : "friend2@gmail.com",
        "friend3" : "friend3@gmail.com",
        "friend4" : "friend4@gmail.com",
       
        }
def whattodo():
    listen_me = assistant_listener()
    if 'assistant' in listen_me:
        if 'write mail' in listen_me:
            say('To whom you want to send mail?')
            try:
                user =assistant_listener()
                email = contact[user]
            except:
                say(user+'not found in your contacts')
                return 0
            say('What is the subject?')
            subject = assistant_listener()
            say('What shoould be the message?')
            message = assistant_listener()
            send_email(email, subject, message)
            say('Email send successfully!')
while True:
    whattodo()
            

    
