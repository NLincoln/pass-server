class HTTPResponse:
    def __init__(self, payload, headers=None, status_code=200):
        if headers is None:
            headers = []
        self.headers = headers
        self.payload = payload
        self.status_code = status_code

    @staticmethod
    def create_status_line(status_code):
        return 'HTTP/1.1 {}'.format(status_code)

    @staticmethod
    def create_header(key, value):
        return '{}:{}'.format(key, value)

    def create_headers(self):
        return '\r\n'.join(self.create_header(*h) for h in self.headers)

    def create_response_string(self):
        status_line = self.create_status_line(self.status_code)
        print(status_line)
        return """
{}
{}

{}
""".format(status_line, self.create_headers(), self.payload)


class HTTPRequest:
    def __init__(self, headers=None, method='GET', path='/', http_version='HTTP/1.1', payload=None):
        if headers is None:
            headers = {}
        self.headers = headers
        self.method = method
        self.path = path
        self.http_version = http_version
        self.payload = payload


def parse_first_line(line):
    return line.split(' ')


def parse_header(header):
    return header.split(':', 1)


def parse_headers(header_array):
    headers = {}
    for line in header_array:
        key, value = parse_header(line)
        headers[key] = value
    return headers


def parse_http_request(request_string):
    head, payload = request_string.split('\r\n\r\n')
    lines = head.splitlines()
    method, path, http_version = parse_first_line(line=lines[0])
    headers = parse_headers(header_array=lines[1:])
    return HTTPRequest(headers=headers,
                       method=method,
                       path=path,
                       http_version=http_version,
                       payload=payload)
