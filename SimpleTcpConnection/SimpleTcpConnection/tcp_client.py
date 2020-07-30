import socket

target_host = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

message = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
message2 = "this is for test"
client.send(message2.encode())

while True:
    response = client.recv(4096)
    print(response)
    if len(response):
        break
    else:
        print("no response!")
