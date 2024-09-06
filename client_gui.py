# client_gui.py
import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

# Choose a nickname
nickname = input("Choose your nickname: ")

# GUI setup
root = tk.Tk()
root.title("Chat Application")

chat_label = tk.Label(root, text="Chat:")
chat_label.pack()

chat_area = scrolledtext.ScrolledText(root)
chat_area.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

def send_message():
    message = f'{nickname}: {message_entry.get()}'
    client.send(message.encode('utf-8'))
    message_entry.delete(0, tk.END)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Networking setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                chat_area.insert(tk.END, message + '\n')
        except:
            print("An error occurred!")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

root.mainloop()
