import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 8080

s.connect( (host, port) )

while True:
    msg = s.recv(512)
    print(f'From Server: {msg.decode("utf-8")}')

    toMsg = input("Client: \n\t")
    s.send( bytes(toMsg, 'utf-8') )
    '''
    servInput = ""
    while True:
        msg = s.recv(10)
        if len(msg) <= 0:
            break
        servInput += msg.decode('utf-8')
    if len(servInput) > 0:
        print(servInput)
    '''
#s.send( bytes("General Kenobi", 'utf-8') )