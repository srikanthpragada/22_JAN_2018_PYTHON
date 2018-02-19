import socket
from datetime import datetime

s = socket.socket()
# host = socket.gethostname()
port = 2000
s.bind(("localhost", port))
s.listen(5)
print("Server is waiting for clients")

while True:
    c, addr = s.accept()
    ctime = datetime.now().strftime("%H:%M:%S")
    print('Got connection from', addr)
    c.send(ctime.encode())
    c.close()