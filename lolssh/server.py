import BaseHTTPServer
import urllib
import re
import sys

from lolcommits import commit, InvalidSHA


HOST_NAME = '0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 17363 # Maybe set this to 9000.

class LolSSHHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    _path_parse = re.compile("^/commit/(?P<repo>[^/]+)/(?P<sha>[^/]+)/(?P<msg>.+)$")
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
        s.wfile.write("\n")

    def log_message(self, *args, **kwargs):
        return None

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = None
    try:
        httpd = server_class((HOST_NAME, PORT_NUMBER), LolSSHHandler)
        httpd.serve_forever()
    except BaseHTTPServer.socket.error:
        sys.exit(-1)
        pass
    except KeyboardInterrupt:
        if httpd:
            httpd.server_close()
        sys.exit(1)
    sys.exit(0)

