#!/usr/bin/python2
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from cloudant.client import Cloudant

PORT_NUMBER = 8080
cred = {
  "username": "13119a46-72cc-4f66-ad4d-239cdb813e0c-bluemix",
  "password": "f992a4aa0b014e94f3029101c8c7923af6691343fabce39fc851b6c3c69cf943",
  "host": "13119a46-72cc-4f66-ad4d-239cdb813e0c-bluemix.cloudant.com",
  "port": 443,
  "url": "https://13119a46-72cc-4f66-ad4d-239cdb813e0c-bluemix:f992a4aa0b014e94f3029101c8c7923af6691343fabce39fc851b6c3c69cf943@13119a46-72cc-4f66-ad4d-239cdb813e0c-bluemix.cloudant.com"
}
client = Cloudant(cred['username'], cred['password'], url=cred['url'], account=cred['username'])
client.connect()
my_database = client['mydb']


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send the html message
        for document in my_database:
            self.wfile.write(document)
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()