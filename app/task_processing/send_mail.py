#!/usr/bin/env python3
import smtplib
import app.mail_config as config


message_template = """From: {0}>
To: {1}
Subject: MD5 hash file

MD5: {2}
URL: {3}
"""


def smtp_mail(mail_to, md5, url):
    message = message_template.format(
        config.smtp_mail, mail_to, md5, url)
    try:
        smtpObj = smtplib.SMTP_SSL(
            config.smtp_address, config.smtp_port)
        smtpObj.login(config.smtp_mail,
                      config.smtp_password)
        smtpObj.sendmail(config.smtp_mail,
                         mail_to, message)
        responce = "(successfully send mail)"
    except Exception as e:
        responce = str(e)
    return responce
