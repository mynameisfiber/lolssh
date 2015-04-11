import time
import BaseHTTPServer
import urllib
import re

from lolcommits import commit, InvalidSHA


HOST_NAME = '0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 17363 # Maybe set this to 9000.

class LolSSHHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    _path_parse = re.compile("/commit/(?P<repo>[^/]+)/(?P<sha>[^/]+)/(?P<msg>.+)")
    def do_GET(s):
        """Respond to a GET request."""
        path_search = s._path_parse.search(urllib.unquote_plus(s.path))
        if path_search is None:
            s.send_response(400)
            s.end_headers()
            s.wfile.write("Invalid Request to lolssh")
        else:
            params = path_search.groupdict()
            try:
                if commit(params['repo'], params['sha'], params['msg']):
                    s.send_response(200)
                    s.end_headers()
                    s.wfile.write("lolcommited!")
                else:
                    s.send_response(500)
                    s.end_headers()
                    s.wfile.write("Failed to lolcommit")
            except InvalidSHA:
                s.send_response(400)
                s.end_headers()
                s.wfile.write("Invalid SHA")

    def log_message(self, *args, **kwargs):
        return None

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    try:
        httpd = server_class((HOST_NAME, PORT_NUMBER), LolSSHHandler)
        print time.asctime(), "started lolssh server - %s:%s" % (HOST_NAME, PORT_NUMBER)
        httpd.serve_forever()
    except BaseHTTPServer.socket.error:
        print "lolssh already running"
    except KeyboardInterrupt:
        httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
