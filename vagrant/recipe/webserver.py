from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#the following is going to be the handler for the server the rest of the applications will use

class webserverHandler(BaseHTTPReqestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                #the following will send a success message
                self.send_respose(200)
                #the following will send an html header in text
                self.send_header('Content-type', 'text/html')
                #the following will signal the end of the header
                self.end_headers()

                #the following will just be a output for the developer to test
                output = ""
                output += "<html><body>Hello!</body></html>"
                self.wfile.write(output)
                print output
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

# the following is the main fuction that will be used to create the server ports
def main():
    #the try key word will attempt to execute a perice of code and if there is an event,
    #then the except will run
    try:
        #set the port number that you would like to run the project on
        port = 8888
        #instantiate the server with httpserver and include the port variable as well as webserverHandler
        server = HTTPServer(('',port), webserverHandler)
        print "Web Server running on port %s" % port

        #this will cause the server to keep running until you close the application or connection
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C entered, stopping the web server..."
        sever.socket.close()

if __name__ == '__main__':
    main()
