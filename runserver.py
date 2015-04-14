#!/usr/bin/env python

import CGIHTTPServer
import BaseHTTPServer
from optparse import OptionParser

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
    cgi_directories = ["/"]

PORT = 8880

def main():
    parser = OptionParser()
    opts, args = parser.parse_args()
    if args:
        httpd = BaseHTTPServer.HTTPServer((args[0], int(args[1])), Handler)
        print "Collectd-web server running at http://%s:%s/" % (args[0], args[1])
    else:
        httpd = BaseHTTPServer.HTTPServer(("0.0.0.0", PORT), Handler)
        print "Collectd-web server running at http://%s:%s/" % ("0.0.0.0", PORT)
    httpd.serve_forever()

if __name__ == "__main__":
    main()

