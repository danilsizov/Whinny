from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import requests

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        response = requests.get('http://localhost:80')
        print(response.content)
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        url = "http://uploads.ru/api?upload"
        file = {"file": open("start.jpg", "rb")}
        my_session = requests.Session()
        log = my_session.post(url, files=file)
        print(log.text)
        self.wfile.write('hi')

serv = HTTPServer(("localhost",80),HttpProcessor)
serv.serve_forever()