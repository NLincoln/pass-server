from server import Server

server_addr = ('127.0.0.1', 8081)
print("Starting server on {}:{}".format(*server_addr))

httpd = Server(bind_options=server_addr)

print('Server has started!')


def generate_response(request):
    print(request.decode('utf8'))
    return '''\
HTTP/1.1 200 OK

{}'''.format(request)


while True:
    httpd.handle_request(generate_response)
