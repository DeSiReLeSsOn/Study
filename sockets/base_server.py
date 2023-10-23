import socket 



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))

#server = socket.create_sever(('127.0.0.1', 2000)) 

server.listen(4)
print('working...')
client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print(data)
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
content = 'Well done, great job buddy...'.encode('utf-8')
client_socket.send(HDRS.encode('utf-8') + content)
print('some text')