from http.server import HTTPServer
from server import RequestHandler

server_addr = ('127.0.0.1', 8081)
print("Starting server on {}:{}".format(*server_addr))

httpd = HTTPServer(server_address=server_addr, RequestHandlerClass=RequestHandler)

print('Server has started!')

while True:
    httpd.handle_request()
