import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# The \r\n\r\n sequence indicates the end of the header
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

# Send the command
mysock.send(cmd)

while True:
    # Receive up to 512 characters
    data = mysock.recv(512)

    if len(data) < 1:
        break
        
    # Decode the data
    print(data.decode(), end='')
    
mysock.close()