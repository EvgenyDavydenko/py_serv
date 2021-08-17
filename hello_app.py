import wsgiref.simple_server

def application(environ, start_response):
    output = b'Hello, World!\n'
    status = '200 OK'    
    response_headers = [
        ('Content-type', 'text/plain; charset=utf-8'),
        ('Content-Length', str(len(output)))
    ]
    
    start_response(status, response_headers)
    return [output]

with wsgiref.simple_server.make_server('', 8000, application) as server:
        print("Serving on port 8000...")
        server.serve_forever()
