# client.py
import socket
import threading

# Choose a nickname
nickname = input("Choose your nickname: ")

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

# Listening to server and sending messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Starting threads for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
