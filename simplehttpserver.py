from http.server import BaseHTTPRequestHandler, HTTPServer
from postcrd import Postgres
import re
from json import dumps

class Handler(BaseHTTPRequestHandler):

    def header(self):
        self.send_response(200)
        self.send_header('Content_type', '')
        self.end_headers()
    

    def do_GET(self):
        tbody = ''
        if self.path.endswith("index.html"):
            g= open('html/index.html')
            e = ''
            data = Postgres().read_db()
            
            e += g.read()
            
            for row in data:
                
                tbody += '<tr>'
                for field in row:
                    

                    tbody += '<td>' + str(field) + '</td>'
                tbody += '<td><a href="/' + str(row[0]) +'/ViewDetail/">view</a></td>'
                
                tbody += '</tr>'
            
            index_html = re.sub(r'##tbody##', tbody, e)
            
            self.header()
            self.wfile.write(index_html.encode())

        elif self.path.split('/')[2]=='ViewDetail':
            pid = self.path.split('/')[1]
            print(pid)
            data = Postgres().read_id(pid)
            print(data)
            e = ''
            e += open('html/view.html').read()

            for field in data:
                tbody +=  '<td>' + str(data[field]) + '</td>'
            view_html = re.sub(r'##vbody##', tbody, e)
            self.header()
            self.wfile.write(view_html.encode())

        
        

def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('',8000)
    httpd =server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__=='__main__':
    run()