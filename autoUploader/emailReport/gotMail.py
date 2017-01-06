import os,smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate


def yesterday():
    yesterday = datetime.date.today() - datetime.timedelta(1)
    yesterdayTargetDir = yesterday.strftime("%Y-%m-%d")
    return yesterdayTargetDir

def Message():
    return "hello"

def CSVFiles():
    return None

def send_mail(send_from, send_to, subject, text,
              files=CSVFiles(), server="127.0.0.1"):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Subject'] = subject
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(text))



    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

