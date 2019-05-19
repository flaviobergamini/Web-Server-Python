from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "10.0.0.108"
hostPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):    
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        Station = '{\"username\":\"iPhone Bergamini\",\"password\":\"12345678\"}'                   #String JSON com as credenciais de rede
        #self.wfile.write(bytes(Station, "utf8"))                                                   #Publica string JSON
        self.wfile.write(bytes("<html><head><title>HTTP server TESTE</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>Flavio Bergamini</p>", "utf-8"))
        self.wfile.write(bytes("<p>My HTTP server with JSON </p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))