from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>TCP/IP Protocols Table</title>
    <style>
        table {
            width: 70%;
            border-collapse: collapse;
            margin: 20px auto;
            font-family: Arial, sans-serif;
        }
        th, td {
            border: 1px solid #444;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #007BFF;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        caption {
            caption-side: top;
            font-size: 1.5em;
            margin-bottom: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <table>
        <caption>Common TCP/IP Protocols and Their Explanation</caption>
        <thead>
            <tr>
                <th>Protocol</th>
                <th>Explanation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>HTTP (HyperText Transfer Protocol)</td>
                <td>Used for transmitting web pages over the Internet.</td>
            </tr>
            <tr>
                <td>HTTPS (HyperText Transfer Protocol Secure)</td>
                <td>Secure version of HTTP that encrypts data for safe communication.</td>
            </tr>
            <tr>
                <td>FTP (File Transfer Protocol)</td>
                <td>Used to transfer files between computers on a network.</td>
            </tr>
            <tr>
                <td>SMTP (Simple Mail Transfer Protocol)</td>
                <td>Protocol for sending emails across networks.</td>
            </tr>
            <tr>
                <td>POP3 (Post Office Protocol version 3)</td>
                <td>Used by email clients to retrieve emails from a server.</td>
            </tr>
            <tr>
                <td>IMAP (Internet Message Access Protocol)</td>
                <td>Allows email clients to access and manage emails directly on the mail server.</td>
            </tr>
            <tr>
                <td>TCP (Transmission Control Protocol)</td>
                <td>Ensures reliable, ordered, and error-checked delivery of data.</td>
            </tr>
            <tr>
                <td>IP (Internet Protocol)</td>
                <td>Handles addressing and routing of packets between devices.</td>
            </tr>
            <tr>
                <td>UDP (User Datagram Protocol)</td>
                <td>Connectionless protocol used for low-latency transmissions.</td>
            </tr>
            <tr>
                <td>DNS (Domain Name System)</td>
                <td>Translates domain names to IP addresses.</td>
            </tr>
        </tbody>
    </table>
</body>
</html>           
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()