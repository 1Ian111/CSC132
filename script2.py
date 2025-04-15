#script for the remote machine 
# shibu oli
# 2025-04-14
# This script runs on the computer, receives keystrokes from Pi over Wi-Fi, and types them

import socket
from pynput.keyboard import Controller

# Initialize keyboard controller
keyboard = Controller()

# Set up socket to receive data
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 65432      # Use the same port as the Pi is sending to

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[+] Listening on port {PORT} for incoming key data...")
    
    conn, addr = s.accept()
    with conn:
        print(f"[+] Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            for char in data.decode():
                print(f"Typing: {char}")
                keyboard.type(char)
