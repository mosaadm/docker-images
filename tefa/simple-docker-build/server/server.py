from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import threading
import time

#======================================#
#     Custom print with timestamp      #
#======================================#
def printMsg(values):
    dateTimeObj = datetime.now()
    values = "[%s] %s" % (dateTimeObj, values)
    print(values)

#======================================#
#  Handles new clients registration    #
#======================================#
class Clients():
    def __init__(self):
       self.registeredNames = []
    
    def count(self):
        return len(self.registeredNames)

    def registerClient(self, name):
        if len(name) > 50:
            printMsg("\U0001F631 Sorry, client name cannot exceed 50 char. Yours have %d" % len(name))
            return False
        if name in self.registeredNames:
            printMsg("\U0000274C Sorry, client `%s` is already registered" % name)
            return False
        else:
            self.registeredNames.append(name)
            printMsg("\U00002705 Successfully registered client. Welcome `%s`" % name)
            return True

#=======================================#
#  Handles Clients HTTP POST Request    #
#=======================================#
class ClientsHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length')) # <--- Gets the size of data
        post_data = self.rfile.read(content_len) # <--- Gets the data itself

        clientName = post_data.decode('utf-8')
        isSuccessful = clients.registerClient(clientName)
        if isSuccessful:
            self.send_response(200)
        else:
            self.send_response(403)
        self.end_headers()

    def log_message(self, format, *args):
        return

#=======================================#
#        Handles HTTPS Server           #
#=======================================#
def startServer(httpHandler, port):
    # server address is localhost:port
    server_address = ('', port)

    # init new HTTP server with address and custom handler
    httpd = HTTPServer(server_address, httpHandler)
    printMsg('Starting server on port %s...\n' % (port))

    # listen until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # gracefully pass interruptions
        pass 
    printMsg('Stopping http server...\n')
    httpd.server_close()

#=======================================#
#    Handles periodic clients count     #
#=======================================#
def startClientsCountThread():
    clientsCount = clients.count()

    # Print clients count
    if clientsCount == 1:
        printMsg("\U00002139 %d client is registered so far" % clients.count())
    else:
        printMsg("\U00002139 %d clients are registered so far" % clients.count())

    # Invoke every 5 seconds
    threading.Timer(5, startClientsCountThread).start()


#=============================================#
#   Instantiate clients and start execution   # 
#=============================================#
def run():
    PORT = 8080
    startServer(ClientsHandler, PORT)
# new clients instance (initially empty)
clients = Clients()
# start periodic counting for the num of registered clients
startClientsCountThread()
run()