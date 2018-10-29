from http.server import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys

SMTP_HOST = os.environ.get("SMTP_HOST", None)
SMTP_PORT = os.environ.get("SMTP_PORT", None)
SMTP_USER = os.environ.get("SMTP_USER", None)
SMTP_PASSWD = os.environ.get("SMTP_PASSWD", None)
SMTP_FROM_EMAIL = os.environ.get("SMTP_FROM_EMAIL", None)
SMTP_TO_EMAIL = os.environ.get("SMTP_TO_EMAIL", None)

def send_alert():
    sender = SMTP_FROM_EMAIL
    receivers = [SMTP_TO_EMAIL]

    msg = MIMEMultipart()

    msg['From'] = SMTP_FROM_EMAIL
    msg['To'] = SMTP_TO_EMAIL
    msg['Subject'] = "Someone is Thirsty!!"

    message = "Your need to fill up their beer!"

    msg.attach(MIMEText(message, 'plain'))

    try:
        smtpObj = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
        smtpObj.login(SMTP_USER, SMTP_PASSWD)
        smtpObj.sendmail(sender, receivers, msg.as_string())         
        print("Successfully sent email")
        smtpObj.close()
    except smtplib.SMTPException as err:
        print("Error: unable to send email" + err)

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        send_alert()
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b'success')
        return

        

def run(server_class=HTTPServer, handler_class=MyServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
    sys.exit(0)