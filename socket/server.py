import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 8080

s.bind( (host, port) )

s.listen(4)

while True:
    client, addr = s.accept()
    print("connected...")
    while True:
        servInput = input("Server: \n\t")
        client.send( bytes(servInput, 'utf-8') )
        fromMsg = client.recv(512)
        print(f'From Client: {fromMsg.decode("utf-8")}')
    #print( s.recv(100).decode('utf-8') )