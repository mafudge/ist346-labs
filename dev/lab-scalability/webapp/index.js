var http = require('http');
var os = require('os');
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(`<h1>I'm ${os.hostname()}</h1><p>We are part of the same web application.`);
}).listen(8080);