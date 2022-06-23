from http.server import HTTPServer, SimpleHTTPRequestHandler

def run()
    """Entrypoint for python server"""
    server_address = ("0.0.0.0", 8000)
    httpd = server_class(server_address, handler_class)
    print("launching server...")
    httpd.serve_forever()

def main():
    run()

if __name__=="__main__":
    main()