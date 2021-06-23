from http.server import *
import os
import sys
import yagmail

APP_PW = "lmlovnpixsfcyoip"
FROM_USER = "mafudge@g.syr.edu"
SMTP_TO_EMAIL = os.environ.get("SMTP_TO_EMAIL", None)

def send_alert():

    with yagmail.SMTP(FROM_USER, APP_PW, host="smtp.gmail.com") as yag:
        subject = "IST346 IoT Alert: Empty Glass Condition!"
        content = ["The pint glass is empty.", "Time for a refill!"] 
        try:
            yag.send(SMTP_TO_EMAIL, subject, content)
            print("Successfully sent email")
        except Exception as e:
            print(f"Error: unable to send email ERROR {e}")

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