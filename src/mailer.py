#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Mailer delivers emails for UltraViolet."""

import os
import smtplib
from email.message import EmailMessage
import markdown

import config


def generateLetter(letter):
    """
    Generate designated email from file.

    :param letter: The name of the email to be generated.
    :returns: The generated email.
    """
    filename = "/letter/" + letter + ".md"
    if not os.path.isfile(filename):
        print('Designated letter does not exist.')
        return None
    else:
        file = open(filename, 'r')
        return file.read()


def generateHTMLLetter(letter):
    """
    Generate designated HTML email from file.

    :param letter: The name of the email to be generated.
    :returns: The generated email.
    """
    filename = "/letter/" + letter + ".md"
    if not os.path.isfile(filename):
        print('Designated letter does not exist.')
        return None
    else:
        file = open(filename, 'r')
        return markdown.markdown(file.read())


def sendLetter(receiver, letter, subject):
    """
    Send designated email from file.

    :param receiver: The recipient's email address.
    :param letter: The name of the email to be sent.
    :param subject: The subject of the email to be sent.
    :returns: returns nothing
    """
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = config.SMTP_CONFIG['email']
        msg['To'] = receiver
        msg.set_content(generateLetter(letter))
        msg.add_alternative(
            generateHTMLLetter(letter), subtype='html'
        )
        smtpObj = smtplib.SMTP(config.SMTP_CONFIG['host'],
                               config.SMTP_CONFIG['port'])
        smtpObj.login(config.SMTP_CONFIG['username'],
                      config.SMTP_CONFIG['password'])
        smtpObj.send_message(msg)
        print('Successfully sent email')
    except smtplib.SMTPException:
        print('Error: unable to send email')
