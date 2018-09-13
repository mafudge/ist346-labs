import socket
import datetime
import time 
import flask 

app = flask.Flask(__name__)

def generate_output(auto=True):
    ip = socket.gethostbyname(socket.gethostname())
    host = socket.gethostname()
    now = datetime.datetime.now()
    app.logger.debug("host:{0} ip:{1} time:{2}".format(host,ip,now))
#    output = "<h1>Sample Web Application</h1>\n" 
#    output += "<p>We are all the same application, but here are my specifics: \n" 
#    output += "<ul>\n"
#    output += "<li>HOSTNAME: <b>" + host +  "</b>\n"
#    output += "<li>IP Address: <b>" + ip +  "</b>\n"
#    output += "<li>Current Date/Time: <b>" + str(now) +  "</b>\n"
#    output += "</ul>\n"
    return flask.render_template('index.html', host=host, ip=ip, now=now, auto=auto) 

@app.route('/')
def index():
    resp = flask.Response(generate_output(auto=True))
    return resp

@app.route('/slow/<int:factor>')
def slow(factor):
    x = 2
    for i in range(0,factor*500):
        for j in range(0,100000):
            x = 2-x
    #time.sleep(seconds)
    resp = flask.Response(generate_output(auto=False))
    return resp

@app.route('/<key>')
def header(key):
    resp = flask.Response(generate_output(auto=False))
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)